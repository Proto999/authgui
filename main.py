import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import subprocess

from uuid import Ui_MainWindow
from auth import Ui_AuthWindow
from reg import Ui_reg

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("DRIVER={SQL Server};SERVER=DESKTOP-A320SRA;DATABASE=users;UID=admin;PWD=1234")


class RegWindow(QMainWindow):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.ui = Ui_reg()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.register_user)
        self.ui.pushButton_2.clicked.connect(AuthWindow.update_ui)

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

        if db.open():
            query = QSqlQuery()
            query.prepare(
                "INSERT INTO users (login, password, email, phone, address, first_name, last_name, patronymic) "
                "VALUES (:login, :password, :email, :phone, :address, :first_name, :last_name, :patronymic)")
            query.bindValue(":login", login)
            query.bindValue(":password", password)
            query.bindValue(":email", email)
            query.bindValue(":phone", phone)
            query.bindValue(":address", address)
            query.bindValue(":first_name", first_name)
            query.bindValue(":last_name", last_name)
            query.bindValue(":patronymic", patronymic)

            if query.exec_():
                db.close()
                QMessageBox.about(self, "Успех!", "Пользователь успешно зарегистрирован.")
            else:
                db.close()
                QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

    def updateLineEdit(self, value):
        self.ui.lineEdit_4.setText(str(value))



class AuthWindow(QMainWindow):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)

        self.failed_attempts = 0  # Счетчик неудачных попыток входа
        self.ui.lcdNumber.display(self.failed_attempts)  # Отображение счетчика на QLCDNumber

        self.ui.pushButton.clicked.connect(self.check_credentials)

    def check_credentials(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT * FROM users WHERE login=:login AND password=:password")
            query.bindValue(":login", login)
            query.bindValue(":password", password)

            if query.exec():
                if query.next():
                    db.close()
                    QMessageBox.about(self, "Успех!", "Доступ с этого устройства разрешен.")
                    self.open_reg_window()
                else:
                    db.close()
                    QMessageBox.about(self, "Ошибка", "Неправильные учетные данные.")
                    self.failed_attempts += 1
                    if self.failed_attempts >= 3:
                        QMessageBox.about(self, "Ошибка", "Превышено количество попыток.")
                        self.close()
                    else:
                        self.update_failed_attempts(login)
            else:
                db.close()
                QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

        self.ui.lcdNumber.display(self.failed_attempts)

    def open_reg_window(self):
        self.close()
        self.reg_window = RegWindow()
        self.reg_window.show()

    def update_failed_attempts(self, login):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT failed_attempts FROM users WHERE login=:login")
            query.bindValue(":login", login)

            if query.exec():
                if query.next():
                    current_attempts = int(query.value(0))
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
            db.close()
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

    def update_ui(self):
        self.close()
        self.auth_window = AuthWindow()
        self.auth_window.show()


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
