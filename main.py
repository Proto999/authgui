import hashlib
import re
import subprocess
import sys
import os

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QLineEdit, QComboBox, QFileDialog, \
    QTextEdit, QTableWidgetItem

from auth import Ui_AuthWindow
from reg import Ui_reg
from uuid import Ui_MainWindow
from redactor import Ui_RedWindow
from adminpanel import Ui_AdminPanelWidget

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("DRIVER={SQL Server};SERVER=DESKTOP-A320SRA;DATABASE=users;UID=admin;PWD=1234")


class AdminPanelWindow(QMainWindow):
    def __init__(self):
        super(AdminPanelWindow, self).__init__()
        self.ui = Ui_AdminPanelWidget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.load_data_from_database)

    def load_data_from_database(self):
        # Получаем данные из базы данных
        query = QSqlQuery("SELECT login, role FROM users")

        # Очищаем таблицу
        self.ui.tableWidget.clearContents()

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget.setRowCount(query.size())
        self.ui.tableWidget.setColumnCount(2)

        # Заполняем таблицу данными из базы данных
        row = 0
        while query.next():
            login = query.value(0)
            role = query.value(1)

            # Создаем элементы QTableWidgetItem и устанавливаем их значения
            login_item = QTableWidgetItem(login)
            role_item = QTableWidgetItem(role)

            # Устанавливаем элементы QTableWidgetItem в таблицу
            self.ui.tableWidget.setItem(row, 0, login_item)
            self.ui.tableWidget.setItem(row, 1, role_item)

            row += 1


class RedWindow(QMainWindow):
    def __init__(self):
        super(RedWindow, self).__init__()
        self.ui = Ui_RedWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.update_file_list)
        self.ui.pushButton_3.clicked.connect(self.save_file)
        self.ui.comboBox.currentIndexChanged.connect(self.load_file_content)
        self.ui.pushButton_2.clicked.connect(self.create_file)
        self.ui.pushButton_6.clicked.connect(self.open_admin_panel)

        self.admin_panel = None

    def update_file_list(self):
        # Очищаем ComboBox
        self.ui.comboBox.clear()

        # Получаем список txt файлов из папки проекта
        file_list = [file for file in os.listdir() if file.endswith(".txt")]

        # Добавляем файлы в ComboBox
        self.ui.comboBox.addItems(file_list)

    def load_file_content(self):
        # Получаем выбранный файл из ComboBox
        selected_file = self.ui.comboBox.currentText()

        if selected_file:
            # Открываем выбранный файл и считываем его содержимое
            with open(selected_file, "r") as file:
                file_content = file.read()

            # Обновляем текст в строке self.ui.lineEdit.text()
            self.ui.lineEdit_2.setText(file_content)

    def save_file(self):
        # Получаем текст из строки self.ui.lineEdit.text()
        text = self.ui.lineEdit_2.text()

        # Получаем выбранный файл из ComboBox
        selected_file = self.ui.comboBox.currentText()

        if selected_file:
            # Сохраняем текст обратно в выбранный файл
            with open(selected_file, "w") as file:
                file.write(text)

            # Выводим сообщение об успешном сохранении
            QMessageBox.about(self, "Успех", "Файл успешно сохранен.")

    def create_file(self):
        # Получаем название файла из строки self.ui.lineEdit.text()
        filename = self.ui.lineEdit.text()

        if filename:
            # Создаем новый txt файл с указанным названием
            with open(filename + ".txt", "w") as file:
                pass

            # Обновляем список файлов в ComboBox
            self.update_file_list()

            # Выводим сообщение об успешном создании файла
            QMessageBox.about(self, "Успех", "Файл успешно создан.")
        else:
            QMessageBox.about(self, "Ошибка", "Введите название файла.")

    def open_admin_panel(self):
        if self.admin_panel is None:
            self.admin_panel = QDialog(self)
            admin_ui = Ui_AdminPanelWidget()
            admin_ui.setupUi(self.admin_panel)
            self.admin_panel.show()
        else:
            self.admin_panel.show()

class RegWindow(QMainWindow):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.ui = Ui_reg()
        self.auth_window = None
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.register_user)
        self.ui.pushButton_2.clicked.connect(self.update_ui)

        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(2147483647)
        self.ui.horizontalSlider.valueChanged.connect(self.updateLineEdit)

    def register_user(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_2.text()
        phone = self.ui.lineEdit_4.text()
        address = self.ui.lineEdit_8.text()
        first_name = self.ui.lineEdit_5.text()
        last_name = self.ui.lineEdit_6.text()
        patronymic = self.ui.lineEdit_7.text()

        if not login.isdigit() or len(login) != 4:
            QMessageBox.about(self, "Ошибка", "Ошибка. Имя пользователя введено неверно.")
            return

        if not re.match(r"^\d{6}[a-zA-Z]$", password):
            QMessageBox.about(self, "Ошибка",
                              "Ошибка. Пароль должен состоять как минимум из 6 цифр и хотя бы одной буквы.")
            return

        if "@" not in email:
            QMessageBox.about(self, "Ошибка", "Ошибка. Email введен неверно.")
            return

        if not re.match(r"^\d{10}$", phone):
            QMessageBox.about(self, "Ошибка", "Ошибка. Номер телефона должен состоять из 10 цифр.")
            return

        if first_name and not first_name.isalpha():
            QMessageBox.about(self, "Ошибка", "Ошибка. Имя должно содержать только буквы.")
            return

        if last_name and not last_name.isalpha():
            QMessageBox.about(self, "Ошибка", "Ошибка. Фамилия должна содержать только буквы.")
            return

        if patronymic and not patronymic.isalpha():
            QMessageBox.about(self, "Ошибка", "Ошибка. Фамилия должна содержать только буквы.")
            return

        if address and "%" in address:
            QMessageBox.about(self, "Ошибка", "Ошибка. Адрес регистрации не может содержать символ процента (%)")
            return

        if db.open():
            query = QSqlQuery()
            select_query = "SELECT * FROM users WHERE login = ?"
            query.prepare(select_query)
            query.bindValue(0, login)

            if query.exec() and query.next():
                QMessageBox.about(self, "Ошибка", "Пользователь с таким логином уже существует.")
            else:
                hashed_password = self.calculate_md5_hash(password)  # Хеширование пароля
                insert_query = (
                    'INSERT INTO users (login, password, email, phone, first_name, last_name, patronymic, address, message) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)')
                values = [login, hashed_password, email, phone, first_name, last_name, patronymic, address,
                          "Еще ничего не написал"]
                query.prepare(insert_query)
                for i, value in enumerate(values):
                    query.bindValue(i, value)
                if query.exec():
                    db.commit()
                    QMessageBox.about(self, "Успех", "Пользователь успешно зарегистрирован!")
                else:
                    print("Ошибка выполнения запроса на вставку нового пользователя.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось выполнить запрос к базе данных.")

    @staticmethod
    def calculate_md5_hash(data):
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()

    def updateLineEdit(self, value):
        self.ui.lineEdit_4.setText(str(value))

    def update_ui(self):
        self.close()
        self.auth_window = AuthWindow()
        self.auth_window.show()


class AuthWindow(QMainWindow):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)

        self.failed_attempts = 0  # Счетчик неудачных попыток входа
        self.ui.lcdNumber.display(self.failed_attempts)  # Отображение счетчика на QLCDNumber

        self.ui.pushButton.clicked.connect(self.check_credentials)
        self.ui.pushButton_2.clicked.connect(self.open_reg_window)

    def check_credentials(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT * FROM users WHERE login=:login AND password=:password")
            query.bindValue(":login", login)
            query.bindValue(":password", self.calculate_md5_hash(password))

            if query.exec():
                if query.next():
                    QMessageBox.about(self, "Успех!", "Авторизация успешна.")
                    self.open_red_window()
                else:
                    QMessageBox.about(self, "Ошибка", "Неправильные учетные данные.")
                    self.failed_attempts += 1
                    if self.failed_attempts >= 3:
                        QMessageBox.about(self, "Ошибка", "Превышено количество попыток.")
                        self.close()
                    else:
                        self.update_failed_attempts(login)
            else:
                QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

        self.ui.lcdNumber.display(self.failed_attempts)

    @staticmethod
    def calculate_md5_hash(data):
        data = str(data)
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()

    def open_reg_window(self):
        self.close()
        self.reg_window = RegWindow()
        self.reg_window.show()

    def open_red_window(self):
        self.close()
        self.red_window = RedWindow()
        self.red_window.show()

    def update_failed_attempts(self, login):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT failed_attempts FROM users WHERE login=:login")
            query.bindValue(":login", login)

            if query.exec():
                if query.next():
                    current_attempts = query.value(0)
                    if current_attempts is not None:
                        current_attempts = int(current_attempts)
                        new_attempts = current_attempts + self.failed_attempts

                        query.prepare("UPDATE users SET failed_attempts=:failed_attempts WHERE login=:login")
                        query.bindValue(":failed_attempts", new_attempts)
                        query.bindValue(":login", login)

                        if query.exec():
                            db.commit()
                        else:
                            QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")

                else:
                    QMessageBox.about(self, "Ошибка", "Пользователь не найден.")
            else:
                QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")


class UUID(QMainWindow):
    def __init__(self):
        super(UUID, self).__init__()
        self.auth_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check_uuid)

    @staticmethod
    def get_uuid():
        output = subprocess.check_output(['wmic', 'csproduct', 'get', 'UUID']).decode().split('\n')[1].strip()
        return output

    def check_uuid(self):
        uuid = self.get_uuid()
        allowed_uuid = "1345D8C6-3FCA-B030-13D0-58112248AF9F"
        if uuid != allowed_uuid:
            QMessageBox.about(self, "Ошибка", "Отказ в доступе с этого устройства.")
        else:
            QMessageBox.about(self, "Успех!", "Доступ с этого устройства разрешен.")
            self.update_ui()

    def update_ui(self):
        self.close()
        self.auth_window = AuthWindow()
        self.auth_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uuid_window = UUID()
    uuid_window.show()
    app.exec()
