import hashlib
import re
import subprocess
import sys
import os
import datetime

import PySide6
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QFileDialog, \
    QTextEdit, QTableWidgetItem
from PySide6.QtCore import QObject, Signal, QDateTime

from auth import Ui_AuthWindow
from reg import Ui_reg
from uuid import Ui_MainWindow
from redactor import Ui_RedWindow
from adminpanel2 import Ui_adminpanel1
from moderpanel import Ui_ModerPanel

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("DRIVER={SQL Server};SERVER=DESKTOP-A320SRA;DATABASE=UserAuth;UID=admin;PWD=1234")


class AuthWindow(QMainWindow):

    def __init__(self):
        super(AuthWindow, self).__init__()

        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)

        self.failed_attempts = 0  # Счетчик неудачных попыток входа
        self.ui.lcdNumber.display(self.failed_attempts)  # Отображение счетчика на QLCDNumber

        self.ui.pushButton.clicked.connect(self.check_credentials)
        self.ui.pushButton_2.clicked.connect(self.open_reg_window)

        self.login = ""
        self.password = ""

    def check_credentials(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT status FROM users1 WHERE login=:login")
            query.bindValue(":login", login)

            if query.exec():
                if query.next():
                    status = query.value(0)  # Получаем значение статуса пользователя
                    if status == "banned":
                        QMessageBox.about(self, "Ошибка", "Вам запрещен доступ.")
                        self.close()
                    elif status == "active":
                        query.prepare("SELECT * FROM users1 WHERE login=:login AND password=:password")
                        query.bindValue(":login", login)

                        query.bindValue(":password", self.calculate_md5_hash(password))

                        if query.exec() and query.next():
                            QMessageBox.about(self, "Успех!", "Авторизация успешна.")

                            print(login)
                            self.open_red_window(login, password)
                            print(password)
                        else:
                            QMessageBox.about(self, "Ошибка", "Неправильные учетные данные.")
                            self.failed_attempts += 1
                            if self.failed_attempts >= 3:
                                QMessageBox.about(self, "Ошибка", "Превышено количество попыток.")
                                self.close()
                            else:
                                self.update_failed_attempts(login)
                    else:
                        QMessageBox.about(self, "Ошибка", "Неизвестный статус пользователя.")
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

        self.login = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()

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

    def open_red_window(self, login, password):
        self.close()
        self.red_window = RedWindow(login, password)
        self.red_window.show()

    def update_failed_attempts(self, login):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT failed_attempts FROM users1 WHERE login=:login")
            query.bindValue(":login", login)

            if query.exec():
                if query.next():
                    current_attempts = query.value(0)
                    if current_attempts is not None:
                        current_attempts = int(current_attempts)
                        new_attempts = current_attempts + self.failed_attempts

                        query.prepare("UPDATE users1 SET failed_attempts=:failed_attempts WHERE login=:login")
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


class ModerPanelWindow(QMainWindow):
    def __init__(self):
        super(ModerPanelWindow, self).__init__()
        self.ui = Ui_ModerPanel()
        self.ui.setupUi(self)

        self.load_data_from_database()

        self.ui.pushButton_2.clicked.connect(self.save_status)
        # self.ui.pushButton_3.clicked.connect(self.)

    def load_data_from_database(self):
        query = QSqlQuery("SELECT login, role, status FROM users1")
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        row = 0
        while query.next():
            login = query.value(0)
            role = query.value(1)
            status = query.value(2)

            login_item = QTableWidgetItem(login)
            role_item = QTableWidgetItem(role)
            status_item = QTableWidgetItem(status)

            self.ui.tableWidget.insertRow(row)

            self.ui.tableWidget.setItem(row, 0, login_item)
            self.ui.tableWidget.setItem(row, 1, role_item)
            self.ui.tableWidget.setItem(row, 2, status_item)

            row += 1
        self.ui.tableWidget.repaint()

        self.ui.comboBox_3.clear()
        self.ui.comboBox_5.clear()

        query = QSqlQuery("SELECT login FROM users1")
        while query.next():
            login = query.value(0)

            self.ui.comboBox_3.addItem(login)
            self.ui.comboBox_5.addItem(login)

    def save_status(self):
        selected_user = self.ui.comboBox_3.currentText()
        selected_status = self.ui.comboBox_4.currentText()

        if selected_user and selected_status:
            query = QSqlQuery()
            query.prepare("UPDATE users1 SET status=:status WHERE login=:login")
            query.bindValue(":status", selected_status)
            query.bindValue(":login", selected_user)

            if query.exec():
                db.commit()
                QMessageBox.about(self, "Успех", "Статус успешно обновлен в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось обновить статус в базе данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Выберите пользователя и статус.")

        self.load_data_from_database()


class AdminPanelWindow(QMainWindow):
    def __init__(self):
        super(AdminPanelWindow, self).__init__()
        self.ui = Ui_adminpanel1()
        self.ui.setupUi(self)

        self.load_data_from_database()

        self.ui.pushButton.clicked.connect(self.handle_button_click)
        self.ui.pushButton_2.clicked.connect(self.save_status)
        self.ui.pushButton_3.clicked.connect(self.save_user_file)

    def load_data_from_database(self):
        # Получаем данные из базы данных
        query = QSqlQuery("SELECT login, role, status FROM users1")
        # Очищаем таблицу
        self.ui.tableWidget.clearContents()
        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)
        # Заполняем таблицу данными из базы данных
        row = 0
        while query.next():
            login = query.value(0)
            role = query.value(1)
            status = query.value(2)
            # Создаем элементы QTableWidgetItem и устанавливаем их значения
            login_item = QTableWidgetItem(login)
            role_item = QTableWidgetItem(role)
            status_item = QTableWidgetItem(status)

            self.ui.tableWidget.insertRow(row)
            # Устанавливаем элементы QTableWidgetItem в таблицу
            self.ui.tableWidget.setItem(row, 0, login_item)
            self.ui.tableWidget.setItem(row, 1, role_item)
            self.ui.tableWidget.setItem(row, 2, status_item)

            row += 1
        self.ui.tableWidget.repaint()
        self.ui.comboBox.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_5.clear()

        query = QSqlQuery("SELECT login FROM users1")  # Используем новый объект QSqlQuery
        while query.next():
            login = query.value(0)
            self.ui.comboBox.addItem(login)
            self.ui.comboBox_3.addItem(login)
            self.ui.comboBox_5.addItem(login)

        query = QSqlQuery("SELECT file_name FROM files")
        while query.next():
            file_name = query.value(0)
            self.ui.comboBox_6.addItem(file_name)

    def save_user_file(self):
        user_id = self.get_user_id(self.ui.comboBox_5.currentText())  # Получаем user_id выбранного имени пользователя
        file_name = self.ui.comboBox_6.currentText()  # Получаем выбранное имя файла

        if user_id and file_name:
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT id FROM files WHERE file_name = :file_name")
                query.bindValue(":file_name", file_name)

                if query.exec() and query.next():
                    file_id = query.value(0)  # Получаем file_id выбранного имени файла

                    query.prepare("INSERT INTO users_files (user_id, file_id) VALUES (:user_id, :file_id)")
                    query.bindValue(":user_id", user_id)
                    query.bindValue(":file_id", file_id)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Запись успешно сохранена в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось сохранить запись в базе данных.")
                else:
                    QMessageBox.about(self, "Ошибка", "Не удалось получить идентификатор файла.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Выберите имя пользователя и файл.")

    def handle_button_click(self):
        # Получаем выбранный пользователь из self.ui.comboBox
        selected_user = self.ui.comboBox.currentText()
        # Получаем выбранную роль из self.ui.comboBox_2
        selected_role = self.ui.comboBox_2.currentText()

        if selected_user and selected_role:
            # Обновляем роль пользователя в базе данных
            query = QSqlQuery()
            query.prepare("UPDATE users1 SET role=:role WHERE login=:login")
            query.bindValue(":role", selected_role)
            query.bindValue(":login", selected_user)

            if query.exec():
                db.commit()
                QMessageBox.about(self, "Успех", "Роль успешно обновлена в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось обновить роль в базе данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Выберите пользователя и роль.")

        self.load_data_from_database()

    def save_status(self):
        selected_user = self.ui.comboBox_3.currentText()
        selected_status = self.ui.comboBox_4.currentText()

        if selected_user and selected_status:
            query = QSqlQuery()
            query.prepare("UPDATE users1 SET status=:status WHERE login=:login")
            query.bindValue(":status", selected_status)
            query.bindValue(":login", selected_user)

            if query.exec():
                db.commit()
                QMessageBox.about(self, "Успех", "Статус успешно обновлен в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось обновить статус в базе данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Выберите пользователя и статус.")

        self.load_data_from_database()

    def get_user_id(self, login):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT id FROM users1 WHERE login = :login")
            query.bindValue(":login", login)

            if query.exec() and query.next():
                user_id = query.value(0)
                return user_id

        return None


class RedWindow(QMainWindow):
    def __init__(self, login, password):
        super(RedWindow, self).__init__()
        self.moder_panel = None
        self.login = login
        self.password = password

        self.red_window = None
        self.ui = Ui_RedWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.update_file_list)
        self.ui.pushButton_3.clicked.connect(self.save_file)

        self.ui.comboBox.currentIndexChanged.connect(self.load_file_content)

        self.ui.pushButton_2.clicked.connect(self.create_file)
        self.ui.pushButton_6.clicked.connect(self.open_admin_panel)
        self.ui.pushButton_5.clicked.connect(self.open_moder_panel)
        self.ui.pushButton_8.clicked.connect(self.save_file_secretextension)

        self.admin_panel = None
        self.moder_panel = None

        self.ui.comboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

    def update_file_list(self):
        user_id = self.get_user_id(self.login)  # Получаем user_id

        if user_id:
            if db.open():
                query = QSqlQuery()
                query.prepare(
                    "SELECT file_name FROM files JOIN users_files ON files.id = users_files.file_id WHERE users_files.user_id = :user_id")
                query.bindValue(":user_id", user_id)

                if query.exec():
                    self.ui.comboBox.clear()  # Очищаем combobox

                    self.ui.comboBox.addItem("")
                    file_list = []
                    while query.next():
                        file_name = query.value(0)
                        file_list.append(file_name)

                    self.ui.comboBox.addItems(file_list)
                    self.ui.comboBox.setCurrentIndex(-1)

                else:
                    QMessageBox.about(self, "Ошибка", "Не удалось выполнить запрос к базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось получить идентификатор пользователя.")

    def load_file_content(self, new_file):
        selected_file = self.ui.comboBox.currentText()
        if selected_file:
            with open(selected_file, "r") as file:
                file_content = file.read()
            self.ui.lineEdit_2.setText(file_content)

            # Получаем данные файла из базы данных
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT last_saved, hash FROM files WHERE file_name=:file_name")
                query.bindValue(":file_name", selected_file)

                if query.exec() and query.next():
                    last_saved = query.value(0)

                    last_saved_datetime = last_saved.toPython()
                    print(type(last_saved_datetime), last_saved_datetime, "last_saved_datetime")

                    hash_value = query.value(1)

                    file_info = os.stat(selected_file)

                    last_modified = datetime.datetime.fromtimestamp(file_info.st_mtime)
                    last_modified = last_modified.replace(microsecond=0)
                    print(type(last_modified), last_modified, "last_modified")

                    if last_modified > last_saved_datetime:
                        QMessageBox.about(self, "Предупреждение", "Файл был изменен после последнего сохранения.")

                    # Проверяем хеш содержимого файла
                    if hash_value and self.calculate_md5_hash(file_content) != hash_value:
                        QMessageBox.about(self, "Предупреждение",
                                          "Хеш содержимого файла не совпадает с сохраненным значением.")

                    print(selected_file, "selected_file")
                    selected_file = self.change_to_secretextension(selected_file)  # Изменяем разрешение файла
                    new_file = os.path.splitext(selected_file)[0] + ".secretextension"
                    self.ui.comboBox.setItemText(self.ui.comboBox.currentIndex(), new_file)
                    print(selected_file, "selected_file_secretextension")

                    # Обновляем значение столбца last_opened в базе данных
                    query.prepare("UPDATE files SET last_opened=:last_opened WHERE file_name=:file_name")
                    query.bindValue(":last_opened", last_modified)
                    query.bindValue(":file_name", selected_file)

                    if not query.exec():
                        return
                    db.commit()
                else:
                    QMessageBox.about(self, "Ошибка", "Не удалось получить данные файла из базы данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

    def change_to_secretextension(self, selected_file):
        file_name, file_ext = os.path.splitext(selected_file)
        new_file = file_name + ".secretextension"
        os.rename(selected_file, new_file)
        print(new_file, "new_file")
        return new_file

    def save_file(self):
        text = self.ui.lineEdit_2.text()
        selected_file = self.ui.comboBox.currentText()
        if selected_file:
            new_file = self.change_to_txt(selected_file)  # Изменяем расширение файла на .txt
            with open(new_file, "w") as file:
                file.write(text)

            # Получаем остальные данные файла
            file_name = os.path.basename(new_file)
            creation_date = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
            hash_value = self.calculate_md5_hash(text)

            # Сохраняем данные файла в базу данных
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT * FROM files WHERE file_name=:file_name")
                query.bindValue(":file_name", file_name)

                if query.exec() and query.next():
                    # Запись уже существует, выполняем обновление значений
                    query.prepare("UPDATE files SET hash=:hash, last_saved=:last_saved WHERE file_name=:file_name")
                    query.bindValue(":hash", hash_value)
                    query.bindValue(":last_saved", datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
                    query.bindValue(":file_name", file_name)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Данные файла успешно обновлены в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось обновить данные файла в базе данных.")
                else:
                    # Запись не существует, выполняем вставку новой записи
                    query.prepare(
                        "INSERT INTO files (file_name, creation_date, last_saved, hash) VALUES (:file_name, :creation_date, :last_saved, :hash)")
                    last_saved = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
                    query.bindValue(":file_name", file_name)
                    query.bindValue(":creation_date", creation_date)
                    query.bindValue(":last_saved", last_saved)
                    query.bindValue(":hash", hash_value)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Данные файла успешно сохранены в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось сохранить данные файла в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

    def change_to_txt(self, selected_file):
        file_name, file_ext = os.path.splitext(selected_file)
        new_file = file_name + ".txt"
        os.rename(selected_file, new_file)
        return new_file

    def save_file_secretextension(self):
        text = self.ui.lineEdit_2.text()
        selected_file = self.ui.comboBox.currentText()
        if selected_file:
            new_file = self.change_to_secretextension(selected_file)  # Изменяем расширение файла на .secretextension
            with open(new_file, "w") as file:
                file.write(text)

            # Получаем остальные данные файла
            file_name = os.path.basename(new_file)
            creation_date = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
            hash_value = self.calculate_md5_hash(text)

            # Сохраняем данные файла в базу данных
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT * FROM files WHERE file_name=:file_name")
                query.bindValue(":file_name", file_name)

                if query.exec() and query.next():
                    # Запись уже существует, выполняем обновление значений
                    query.prepare("UPDATE files SET hash=:hash, last_saved=:last_saved WHERE file_name=:file_name")
                    query.bindValue(":hash", hash_value)
                    query.bindValue(":last_saved", datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
                    query.bindValue(":file_name", file_name)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Данные файла успешно обновлены в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось обновить данные файла в базе данных.")
                else:
                    # Запись не существует, выполняем вставку новой записи
                    query.prepare(
                        "INSERT INTO files (file_name, creation_date, last_saved, hash) VALUES (:file_name, :creation_date, :last_saved, :hash)")
                    last_saved = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
                    query.bindValue(":file_name", file_name)
                    query.bindValue(":creation_date", creation_date)
                    query.bindValue(":last_saved", last_saved)
                    query.bindValue(":hash", hash_value)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Данные файла успешно сохранены в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось сохранить данные файла в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

    def calculate_md5_hash(self, file_content):
        data = str(file_content)
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()

    def calculate_md5_hash(self, text):
        data = str(text)
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()

    def create_file(self):
        filename = self.ui.lineEdit.text()

        if filename:
            with open(filename + ".txt", "w") as file:
                pass
            # self.update_file_list()

            # Получаем данные файла
            file_name = filename + ".txt"
            creation_date = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")

            # Сохраняем данные файла в базу данных
            if db.open():
                query = QSqlQuery()
                query.prepare(
                    "INSERT INTO files (file_name, creation_date) VALUES (:file_name, :creation_date)")
                query.bindValue(":file_name", file_name)
                query.bindValue(":creation_date", creation_date)

                if query.exec():
                    file_id = query.lastInsertId()
                    user_id = self.get_user_id(self.login)
                    if file_id and user_id:
                        query.prepare(
                            "INSERT INTO users_files (file_id, user_id) VALUES (:file_id, :user_id)")
                        query.bindValue(":file_id", file_id)
                        query.bindValue(":user_id", user_id)

                        if query.exec():
                            db.commit()
                            QMessageBox.about(self, "Успех", "Файл успешно создан и данные сохранены в базе данных.")
                            index = self.ui.comboBox.findText(filename + ".txt")
                            if index != -1:
                                self.ui.comboBox.setCurrentIndex(index)
                        else:
                            QMessageBox.about(self, "Ошибка", "Не удалось сохранить данные файла в базе данных.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось получить идентификаторы файла и пользователя.")
                else:
                    QMessageBox.about(self, "Ошибка", "Не удалось сохранить данные файла в базе данных.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Введите название файла.")

    def get_user_id(self, login):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT id FROM users1 WHERE login = :login")
            query.bindValue(":login", login)

            if query.exec() and query.next():
                user_id = query.value(0)
                return user_id

        return None

    def open_admin_panel(self):
        if self.admin_panel is None:
            self.admin_panel = AdminPanelWindow()
            self.admin_panel.show()
        else:
            self.admin_panel.show()

    def open_moder_panel(self):
        if self.moder_panel is None:
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT role FROM users1 WHERE login=:login")
                query.bindValue(":login", self.login)

                if query.exec():
                    if query.next():
                        role = query.value(0)  # Получаем значение роли пользователя
                        if role == "Модератор":
                            QMessageBox.about(self, "Успех!", "Доступ разрешен. Открываю панель модератора.")
                            self.moder_panel = ModerPanelWindow()
                            self.moder_panel.show()
                        else:
                            QMessageBox.about(self, "Ошибка", "У вас нет прав доступа к панели модератора.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Пользователь не найден.")
                else:
                    QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")


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
                    'INSERT INTO users1 (login, password, email, phone, first_name, last_name, patronymic, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?)')
                values = [login, hashed_password, email, phone, first_name, last_name, patronymic, address]
                query.prepare(insert_query)
                for i, value in enumerate(values):
                    query.bindValue(i, value)
                if query.exec():
                    db.commit()
                    QMessageBox.about(self, "Успех", "Пользователь успешно зарегистрирован!")
                    # Записываем значение "active" в столбец status
                    update_query = QSqlQuery()
                    update_query.prepare("UPDATE users1 SET status=:status WHERE login=:login")
                    update_query.bindValue(":status", "active")
                    update_query.bindValue(":login", login)
                    if update_query.exec():
                        db.commit()
                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось обновить статус пользователя.")
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
    sys.exit(app.exec())
