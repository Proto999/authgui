import hashlib
import re
import shutil
import subprocess
import sys
import datetime
import win32con
import win32file
import zipfile
import time
import os
import stat
import pyzipper
import msvcrt
import PySide6
import win32con
import win32file
from PySide6 import QtCore
from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import Qt, QCloseEvent
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import *

from auth import Ui_AuthWindow
from redactor2 import Ui_RedWindow2
from reg import Ui_reg
from uuid import Ui_MainWindow
from adminpanel2 import Ui_adminpanel1
from moderpanel import Ui_ModerPanel
from userpanel import Ui_UserPanel

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
        self.red_window = RedWindow2(login, password)
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


class UserPanelWindow(QMainWindow):
    def __init__(self, login):
        super(UserPanelWindow, self).__init__()
        self.ui = Ui_UserPanel()
        self.ui.setupUi(self)
        self.login = login
        print(login, "login_user_panel")

        self.load_data_for_user(login)
        self.ui.pushButton_3.clicked.connect(self.share_file_with_user)

    def load_data_for_user(self, login):
        # Очищаем таблицу
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(0)

        # Устанавливаем количество столбцов
        self.ui.tableWidget_2.setColumnCount(2)

        # Получаем логины пользователей с ролью "Пользователь" и "Гость"
        query_users = QSqlQuery()
        query_users.prepare("SELECT login FROM users1 WHERE role IN ('Пользователь', 'Гость')")
        query_users.exec()

        # Заполняем столбец 0
        row = 0
        while query_users.next():
            user_login = query_users.value(0)
            self.ui.tableWidget_2.insertRow(row)
            self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(user_login))
            row += 1

        # Получаем файлы, с которыми пользователь поделился
        query_files = QSqlQuery()
        query_files.prepare("SELECT f.file_name "
                            "FROM users1 u1 "
                            "JOIN users_files uf ON u1.id = uf.user_id "
                            "JOIN files f ON uf.file_id = f.id "
                            "WHERE uf.user_id = (SELECT id FROM users1 WHERE login = :login) "
                            "ORDER BY f.file_name")
        query_files.bindValue(":login", login)
        query_files.exec()

        row = 0
        while query_files.next():
            file_name = query_files.value(0)

            # Заполняем столбец 1
            self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(file_name))

            row += 1

        # Получаем логины пользователей с ролью "Пользователь" и "Гость" и заполняем comboBox_5
        query_users = QSqlQuery()
        query_users.prepare("SELECT login FROM users1 WHERE role IN ('Пользователь', 'Гость')")
        query_users.exec()

        # Очищаем и заполняем comboBox_5
        self.ui.comboBox_5.clear()
        while query_users.next():
            user_login = query_users.value(0)
            self.ui.comboBox_5.addItem(user_login)
        # Удаляем первый элемент из comboBox_5, если он не пуст
        if self.ui.comboBox_5.count() > 0:
            self.ui.comboBox_5.removeItem(0)

        # Получаем файлы, которыми владеет пользователь и заполняем comboBox_6
        query_owner_files = QSqlQuery()
        query_owner_files.prepare("SELECT DISTINCT f.file_name "
                                  "FROM users1 u1 "
                                  "JOIN users_files uf ON u1.id = uf.user_id "
                                  "JOIN files f ON uf.file_id = f.id "
                                  "WHERE uf.user_id = (SELECT id FROM users1 WHERE login = :login) "
                                  "ORDER BY f.file_name")
        query_owner_files.bindValue(":login", login)
        query_owner_files.exec()

        # Очищаем и заполняем comboBox_6
        self.ui.comboBox_6.clear()
        while query_owner_files.next():
            owner_file_name = query_owner_files.value(0)
            self.ui.comboBox_6.addItem(owner_file_name)

        self.ui.tableWidget_2.repaint()

    def share_file_with_user(self):
        # Получаем выбранных пользователя и файл
        selected_user = self.ui.comboBox_5.currentText()
        selected_file = self.ui.comboBox_6.currentText()

        # Проверяем, что пользователь и файл выбраны
        if not selected_user or not selected_file:
            QMessageBox.warning(self, "Предупреждение", "Выберите пользователя и файл для передачи прав доступа.")
            return

        # Получаем user_id выбранного пользователя
        query_user_id = QSqlQuery()
        query_user_id.prepare("SELECT id FROM users1 WHERE login = :login")
        query_user_id.bindValue(":login", selected_user)
        if not query_user_id.exec_() or not query_user_id.next():
            QMessageBox.warning(self, "Ошибка", "Не удалось получить информацию о пользователе.")
            return
        user_id = query_user_id.value(0)

        # Получаем file_id выбранного файла
        query_file_id = QSqlQuery()
        query_file_id.prepare("SELECT id FROM files WHERE file_name = :file_name")
        query_file_id.bindValue(":file_name", selected_file)
        if not query_file_id.exec_() or not query_file_id.next():
            QMessageBox.warning(self, "Ошибка", "Не удалось получить информацию о файле.")
            return
        file_id = query_file_id.value(0)

        # Проверяем, что пользователь еще не имеет доступа к файлу
        query_check_access = QSqlQuery()
        query_check_access.prepare("SELECT COUNT(*) FROM users_files WHERE user_id = :user_id AND file_id = :file_id")
        query_check_access.bindValue(":user_id", user_id)
        query_check_access.bindValue(":file_id", file_id)
        if not query_check_access.exec_() or not query_check_access.next():
            QMessageBox.warning(self, "Ошибка", "Не удалось проверить доступ пользователя к файлу.")
            return
        if query_check_access.value(0) > 0:
            QMessageBox.warning(self, "Предупреждение", "Пользователь уже имеет доступ к выбранному файлу.")
            return

        # Добавляем запись в таблицу users_files
        query_insert_access = QSqlQuery()
        query_insert_access.prepare("INSERT INTO users_files (user_id, file_id) VALUES (:user_id, :file_id)")
        query_insert_access.bindValue(":user_id", user_id)
        query_insert_access.bindValue(":file_id", file_id)
        if not query_insert_access.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось предоставить доступ к файлу.")
            return

        QMessageBox.information(self, "Успех",
                                f"Пользователю {selected_user} предоставлен доступ к файлу {selected_file}.")

        # Обновляем данные в таблицах
        self.load_data_for_user(self.login)


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


class RedWindow2(QMainWindow):
    def __init__(self, login, password):
        super(RedWindow2, self).__init__()

        self.closing = False
        self.ui = Ui_RedWindow2()
        self.ui.setupUi(self)
        self.red_window = None

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Устанавливаем обработчик событий мыши для окна
        self.installEventFilter(self)
        self.resizing = False

        self.moder_panel = None
        self.login = login
        self.password = password

        self.ui.pushButton.clicked.connect(self.update_file_list)
        self.ui.pushButton_3.clicked.connect(self.save_file)

        self.ui.pushButton_9.clicked.connect(self.load_file_content)
        self.ui.pushButton_2.clicked.connect(self.create_file)
        self.ui.pushButton_4.clicked.connect(self.open_user_panel)
        self.ui.pushButton_6.clicked.connect(self.open_admin_panel)
        self.ui.pushButton_5.clicked.connect(self.open_moder_panel)
        self.ui.pushButton_7.clicked.connect(self.save_file_to_archive)
        self.ui.pushButton_8.clicked.connect(self.save_file_secretextension)
        self.ui.pushButton_10.clicked.connect(self.load_file_content_rar)
        self.ui.pushButton_11.clicked.connect(self.delete_file)
        self.ui.pushButton_12.clicked.connect(self.on_pushButton_12_clicked)
        self.ui.pushButton_13.clicked.connect(self.on_pushButton_13_clicked)
        self.ui.pushButton_14.clicked.connect(self.confirm_exit)

        self.resize_timer = QTimer(self)
        self.resize_timer.timeout.connect(self.step_resize)
        self.resize_step = 10  # Шаг изменения размера

        self.fullscreen_timer = QTimer(self)
        self.fullscreen_timer.timeout.connect(self.step_fullscreen)

        self.previous_size = None

        # Добавим обработчик событий мыши для изменения размера
        self.setMouseTracking(True)
        self.installEventFilter(self)  # Добавим обработчик событий мыши для перемещения окна

        self.admin_panel = None
        self.moder_panel = None
        self.user_panel = None

        self.ui.comboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
        elif event.type() == QEvent.MouseMove and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.old_pos)
            self.old_pos = event.globalPosition().toPoint()
        elif event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
            self.resize_timer.start(20)
        elif event.type() == QEvent.MouseButtonRelease and event.button() == Qt.RightButton:
            self.resize_timer.stop()
        return super().eventFilter(obj, event)

    def step_resize(self):
        current_width = self.width()
        current_height = self.height()

        target_width = 1920
        target_height = 1080
        min_width = 900
        min_height = 435

        if not hasattr(self, 'resizing_direction'):
            self.resizing_direction = 1  # Направление изменения размера: 1 - увеличение, -1 - уменьшение

        new_width = current_width + self.resizing_direction * self.resize_step
        new_height = current_height + self.resizing_direction * self.resize_step

        # Если достигнут максимальный или минимальный размер, меняем направление
        if new_width >= target_width or new_width <= min_width or new_height >= target_height or new_height <= min_height:
            self.resizing_direction *= -1

        # Ограничиваем размеры окна
        new_width = max(min_width, min(target_width, new_width))
        new_height = max(min_height, min(target_height, new_height))

        self.resize(new_width, new_height)

        if new_width <= min_width or new_width >= target_width or new_height <= min_height or new_height >= target_height:
            self.resize_timer.stop()

    def confirm_exit(self):
        # Проверка, не было ли окно уже закрыто
        if not self.closing:
            self.closing = True
            reply = QMessageBox.question(
                self, 'Exit Confirmation',
                'Are you sure you want to exit?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                current_file = self.ui.comboBox.currentText()

                if current_file.endswith(".txt"):
                    self.save_file()
                elif current_file.endswith(".secretextension"):
                    self.save_file_secretextension()
                elif current_file.endswith(".zip"):
                    self.save_file_to_archive()

                self.close()

            # Сброс флага после закрытия окна
            self.closing = False

    def closeEvent(self, event: QCloseEvent):
        # Переопределение closeEvent для обработки Alt+F4
        event.ignore()  # Игнорируем стандартное закрытие
        # Вызываем confirm_exit вместо закрытия окна
        self.confirm_exit()

    def on_pushButton_13_clicked(self):
        # Кнопка для постепенного перехода в полноэкранный режим или возврата к предыдущему размеру
        if self.isFullScreen():
            self.showNormal()  # Возвращаемся к предыдущему размеру
            if self.previous_size is not None:
                self.resize(*self.previous_size)
        else:
            self.previous_size = (self.width(), self.height())  # Сохраняем текущий размер
            self.showFullScreen()

    def step_fullscreen(self):
        if not self.isFullScreen():
            self.showFullScreen()
            self.fullscreen_timer.stop()

    def on_pushButton_12_clicked(self):
        # Кнопка для сворачивания окна
        self.showMinimized()

    def update_file_list(self):
        user_id = self.get_user_id(self.login)  # Получаем user_id

        if user_id:
            if db.open():
                # Получаем роль пользователя
                role_query = QSqlQuery()
                role_query.prepare("SELECT role FROM users1 WHERE id = :user_id")
                role_query.bindValue(":user_id", user_id)

                if role_query.exec():
                    if role_query.next():
                        role = role_query.value(0)

                        # Выполняем запрос в зависимости от роли пользователя
                        query = QSqlQuery()
                        if role in ["Администратор", "Модератор"]:
                            query.prepare("SELECT file_name FROM files")
                        elif role in ["Пользователь", "Гость"]:
                            query.prepare(
                                "SELECT file_name FROM files JOIN users_files ON files.id = users_files.file_id WHERE users_files.user_id = :user_id"
                            )
                            query.bindValue(":user_id", user_id)

                        if query.exec():
                            self.ui.comboBox.clear()  # Очищаем combobox

                            file_list = []
                            while query.next():
                                file_name = query.value(0)
                                file_list.append(file_name)

                            self.ui.comboBox.addItems(file_list)
                        else:
                            QMessageBox.about(
                                self, "Ошибка", "Не удалось выполнить запрос к базе данных."
                            )
                    else:
                        QMessageBox.about(
                            self, "Ошибка", "Не удалось получить роль пользователя."
                        )
                else:
                    QMessageBox.about(
                        self, "Ошибка", "Не удалось выполнить запрос к базе данных."
                    )
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")
        else:
            QMessageBox.about(self, "Ошибка", "Не удалось получить идентификатор пользователя.")

    def load_file_content(self):
        selected_file = self.ui.comboBox.currentText()

        if selected_file:
            # Чтение содержимого файла
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

                    hash_value = query.value(1)

                    file_info = os.stat(selected_file)
                    last_modified = datetime.datetime.fromtimestamp(file_info.st_mtime)
                    last_modified = last_modified.replace(microsecond=0)

                    # Проверяем, был ли файл изменен после последнего сохранения
                    if last_modified > last_saved_datetime:
                        QMessageBox.about(self, "Предупреждение", "Файл был изменен после последнего сохранения.")

                    # Проверяем хеш содержимого файла
                    if hash_value and self.calculate_md5_hash(selected_file) != hash_value:
                        QMessageBox.about(self, "Предупреждение",
                                          "Хеш содержимого файла не совпадает с сохраненным значением.")

                    # Изменяем разрешение файла на .secretextension
                    new_file = self.change_to_secretextension(selected_file)

                    # Обновляем значение столбца file_name в базе данных
                    update_query = QSqlQuery()
                    update_query.prepare(
                        "UPDATE files SET file_name=:new_file, last_opened=:last_opened WHERE file_name=:old_file")
                    update_query.bindValue(":new_file", new_file)
                    update_query.bindValue(":last_opened", last_modified)
                    update_query.bindValue(":old_file", selected_file)

                    if update_query.exec():
                        db.commit()

                        os.chmod(new_file, stat.S_IRUSR)  # Только чтение для владельца
                        print("Файл защищен от записи")

                        self.ui.comboBox.setItemText(self.ui.comboBox.currentIndex(), new_file)

                    else:
                        QMessageBox.about(self, "Ошибка", "Не удалось обновить данные файла в базе данных.")
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
        os.chmod(selected_file, stat.S_IRUSR | stat.S_IWUSR)
        print("Файл разблокирован")

        if selected_file:
            # Получаем старое название файла
            old_file_name = os.path.basename(selected_file)

            # Изменяем расширение файла на .txt
            new_file = self.change_to_txt(selected_file)

            with open(new_file, "w") as file:
                file.write(text)

            # Получаем остальные данные файла
            file_name = os.path.basename(new_file)
            creation_date = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
            hash_value = self.calculate_md5_hash(selected_file)

            # Сохраняем данные файла в базу данных
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT * FROM files WHERE file_name=:file_name")
                query.bindValue(":file_name", old_file_name)

                if query.exec() and query.next():
                    # Запись уже существует, выполняем обновление значений
                    query.prepare(
                        "UPDATE files SET file_name=:new_file_name, hash=:hash, last_saved=:last_saved WHERE file_name=:old_file_name")
                    query.bindValue(":new_file_name", file_name)
                    query.bindValue(":hash", hash_value)
                    query.bindValue(":last_saved", datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
                    query.bindValue(":old_file_name", old_file_name)

                    if query.exec():
                        db.commit()
                        QMessageBox.about(self, "Успех", "Данные файла успешно обновлены в базе данных.")

                        # Обновляем название файла в QComboBox
                        index = self.ui.comboBox.findText(old_file_name)
                        if index != -1:
                            self.ui.comboBox.setItemText(index, file_name)
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
        os.chmod(selected_file, stat.S_IRUSR | stat.S_IWUSR)
        print("Файл разблокирован")
        if selected_file:
            if selected_file.endswith(".zip"):
                with zipfile.ZipFile(selected_file, 'r') as zip_ref:
                    file_list = zip_ref.namelist()
                    if len(file_list) == 1:  # Предполагаем, что в архиве только один файл
                        extracted_file = file_list[0]
                        zip_ref.extract(extracted_file)  # Разархивируем файл
                        new_file = extracted_file.replace(".txt", ".secretextension")
                        os.rename(extracted_file, new_file)  # Меняем расширение файла на .secretextension
                        with open(new_file, "w") as file:
                            file.write(text)
            else:
                new_file = self.change_to_secretextension(
                    selected_file)  # Изменяем расширение файла на .secretextension
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
                        "INSERT INTO files (file_name, creation_date, last_saved, hash) VALUES (:file_name, "
                        ":creation_date, :last_saved, :hash)")
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

        time.sleep(1)  # Добавляем задержку в 1 секунду
        os.remove(selected_file)  # Удаляем архив

    def save_file_to_archive(self):
        selected_file = self.ui.comboBox.currentText()

        os.chmod(selected_file, stat.S_IRUSR | stat.S_IWUSR)
        print("Файл разблокирован")

        if selected_file:
            # Получаем ID пользователя
            user_id = self.get_user_id(self.login)
            if user_id is None:
                print("Ошибка: Не удалось получить ID пользователя.")
                return
            # Проверяем расширение файла
            if selected_file.endswith(".txt") or selected_file.endswith(".secretextension"):
                self.archive_txt_file(selected_file, user_id)
            else:
                QMessageBox.about(self, "Ошибка", "Неподдерживаемый формат файла для сохранения в защищенный архив.")

    def delete_file(self):
        selected_file = self.ui.comboBox.currentText()

        if selected_file:
            user_id = self.get_user_id(self.login)

            # Проверяем подключение к базе данных
            if not db.isOpen():
                db.open()

            # Удаляем запись из таблицы users_files
            if user_id and db.isOpen():
                delete_users_files_query = QSqlQuery()
                delete_users_files_query.prepare(
                    "DELETE FROM users_files WHERE user_id=:user_id AND file_id=(SELECT id FROM files WHERE file_name=:file_name)")
                delete_users_files_query.bindValue(":user_id", user_id)
                delete_users_files_query.bindValue(":file_name", selected_file)

                if not delete_users_files_query.exec():
                    error_message = delete_users_files_query.lastError().text()
                    QMessageBox.about(self, "Ошибка",
                                      f"Не удалось удалить запись из таблицы users_files: {error_message}")
                    return
            else:
                QMessageBox.about(self, "Ошибка",
                                  "Не удалось получить идентификатор пользователя или открыть базу данных.")
                return

            # Удаляем файл из директории
            try:
                os.remove(selected_file)
            except OSError as e:
                QMessageBox.about(self, "Ошибка", f"Не удалось удалить файл: {e}")
                return

            # Удаляем данные файла из базы данных
            if db.isOpen():
                delete_query = QSqlQuery()
                delete_query.prepare("DELETE FROM files WHERE file_name=:file_name")
                delete_query.bindValue(":file_name", selected_file)

                if delete_query.exec():
                    db.commit()
                else:
                    error_message = delete_query.lastError().text()
                    QMessageBox.about(self, "Ошибка",
                                      f"Не удалось удалить данные файла из базы данных: {error_message}")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

            # Удаляем название файла из ComboBox
            index = self.ui.comboBox.findText(selected_file)
            if index != -1:
                self.ui.comboBox.removeItem(index)
                self.ui.comboBox.setCurrentIndex(-1)
        else:
            QMessageBox.about(self, "Предупреждение", "Выберите файл для удаления.")

    def load_file_content_rar(self):
        selected_file = self.ui.comboBox.currentText()
        if not selected_file or not os.path.exists(selected_file):
            QMessageBox.about(self, "Ошибка", "Файл не найден.")
            return

        # Получаем ID пользователя
        user_id = self.get_user_id(self.login)
        if user_id is None:
            print("Ошибка: Не удалось получить ID пользователя.")
            return

        # Проверяем расширение файла
        if selected_file.endswith(f".zip"):
            self.extract_and_check_archive(selected_file, user_id)
        elif selected_file.endswith(".txt") or selected_file.endswith(".secretextension"):
            QMessageBox.about(self, "Ошибка", "Выбранный вами файл не является защищенным архивом. "
                                              "Используйте другой способ открытия файла.")
        else:
            QMessageBox.about(self, "Ошибка", "Неподдерживаемый формат файла.")

    def extract_and_check_archive(self, archive_path, user_id):
        try:
            password = str(user_id).encode('utf-8')
            with pyzipper.AESZipFile(archive_path, "r") as zipf:
                # Вводим в качестве пароля хешированный id пользователя
                zipf.setpassword(password)
                zipf.extractall()

            # Удаляем архив
            os.remove(archive_path)

            # Получаем имя файла без расширения
            base_name = os.path.splitext(os.path.basename(archive_path))[0]

            # Меняем расширение полученного файла на .secretextension
            txt_file_path = os.path.join(os.path.dirname(archive_path), f"{base_name}.secretextension")

            # Блокировать файл после извлечения
            os.chmod(txt_file_path, stat.S_IRUSR)  # Только чтение для владельца
            print("Файл защищен от записи после извлечения")

            # Сверяем хеш содержимого из бд
            if self.check_file_hash(txt_file_path):
                # Загружаем содержимое файла
                with open(txt_file_path, "r") as file:
                    file_content = file.read()
                    self.ui.lineEdit_2.setText(file_content)

                # Меняем имя файла в comboBox
                self.ui.comboBox.setItemText(self.ui.comboBox.currentIndex(), txt_file_path)

            else:
                QMessageBox.about(self, "Ошибка", "Хеш содержимого файла не совпадает с сохраненным значением.")
        except Exception as e:
            print(f"Ошибка при разархивации файла: {str(e)}")
            QMessageBox.about(self, "Ошибка", "Невозможно открыть архив. Неверный пароль.")

    def check_file_hash(self, file_path, user_id):
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT hash FROM files WHERE file_name=:file_name")
            query.bindValue(":file_name", file_path)

            if query.exec() and query.next():
                saved_hash = query.value(0)

                # Рассчитываем хеш содержимого файла
                calculated_hash = self.calculate_md5_hash(file_path)

                # Сверяем хеш с сохраненным значением
                return saved_hash == calculated_hash

        return False

    def archive_txt_file(self, selected_file, user_id):
        os.chmod(selected_file, stat.S_IRUSR | stat.S_IWUSR)
        print("Файл разблокирован")

        file_name, file_ext = os.path.splitext(selected_file)
        archive_name = file_name + f".zip"

        content_hash = self.calculate_md5_hash_from_lineedit()
        content = self.ui.lineEdit_2.text()

        # Записываем содержимое в файл .secretextension
        secretextension_file = file_name + ".secretextension"
        with open(secretextension_file, "w") as txt_file:
            txt_file.write(content)

        # Создаем защищенный архив с паролем на основе ID пользователя
        try:
            password = str(user_id).encode('utf-8')
            with pyzipper.AESZipFile(archive_name, 'w', compression=pyzipper.ZIP_LZMA,
                                     encryption=pyzipper.WZ_AES) as zipf:
                zipf.setpassword(password)
                zipf.write(os.path.basename(selected_file), os.path.basename(selected_file))

        except Exception as e:
            print(f"Ошибка при создании архива: {str(e)}")
            QMessageBox.about(self, "Ошибка", "Невозможно создать защищенный архив.")
            return
        finally:
            # Возвращаемся в исходную директорию
            os.chdir(os.path.dirname(__file__))

        # Удаляем исходный файл
        os.remove(selected_file)

        # Обновляем информацию в базе данных
        self.update_database_after_archiving(selected_file, archive_name, content_hash)
        self.update_file_list()

    def update_database_after_archiving(self, original_file_path, archive_name, content_hash):
        if db.open():
            query = QSqlQuery()

            # Получаем хеш и время сохранения файла перед архивацией
            original_hash, original_last_saved = self.get_file_info(original_file_path)

            # Обновляем информацию в базе данных
            query.prepare(
                "UPDATE files SET file_name=:file_name, hash=:hash, last_saved=:last_saved WHERE file_name=:original_file_name")
            query.bindValue(":file_name", archive_name)
            query.bindValue(":hash", content_hash)
            query.bindValue(":last_saved", original_last_saved)
            query.bindValue(":original_file_name", original_file_path)

            if not query.exec():
                print("Ошибка: Не удалось обновить информацию в базе данных.")
                return
            db.commit()

        else:
            print("Ошибка: Не удалось открыть базу данных.")

    def get_file_info(self, file_path):
        # Получаем хеш и время сохранения файла из базы данных
        if db.open():
            query = QSqlQuery()
            query.prepare("SELECT hash, last_saved FROM files WHERE file_name=:file_name")
            query.bindValue(":file_name", file_path)

            if query.exec() and query.next():
                hash_value = query.value(0)
                last_saved = query.value(1).toPython()
                return hash_value, last_saved

        return None, None

    def check_file_hash(self, file_path):
        file_content = self.calculate_md5_hash(file_path)
        return self.calculate_md5_hash(file_content)

    def calculate_md5_hash(self, data):
        if isinstance(data, str):
            # Если передана строка, хешируем ее содержимое
            md5_hash = hashlib.md5()
            md5_hash.update(data.encode('utf-8'))
            return md5_hash.hexdigest()
        elif isinstance(data, bytes):
            # Если переданы байты (например, содержимое файла), хешируем их
            md5_hash = hashlib.md5()
            md5_hash.update(data)
            return md5_hash.hexdigest()
        else:
            raise ValueError("Неподдерживаемый тип данных для расчета хеша.")

    def calculate_md5_hash_from_lineedit(self):
        text = self.ui.lineEdit_2.text()
        print(text, "text")
        return self.calculate_md5_hash(text)

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
                return query.value(0)

        return None

    def get_user_id(self, login):
        print(f"Попытка получения ID пользователя для {login}")

        if not isinstance(login, str):
            print("Неверный формат логина.")
            return None

        if not db.open():
            print("Не удалось открыть базу данных.")
            return None

        query = QSqlQuery()
        query.prepare("SELECT id FROM users1 WHERE login = :login")
        query.bindValue(":login", login)

        if query.exec():
            if query.next():
                user_id = query.value(0)
                print(f"ID пользователя для {login}: {user_id}")
                return user_id
            else:
                print(f"Для {login} не найдено ни одного пользователя.")
        else:
            print(f"Не удалось выполнить запрос для {login}: {query.lastError().text()}")

        return None

    def open_admin_panel(self):
        if self.admin_panel is None:
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT role FROM users1 WHERE login=:login")
                query.bindValue(":login", self.login)

                if query.exec():
                    if query.next():
                        role = query.value(0)  # Получаем значение роли пользователя
                        if role == "Администратор":
                            QMessageBox.about(self, "Успех!", "Доступ разрешен. Открываю панель Администратора.")
                            self.admin_panel = AdminPanelWindow()
                            self.admin_panel.show()
                        else:
                            QMessageBox.about(self, "Ошибка", "У вас нет прав доступа к панели Администратора.")
                    else:
                        QMessageBox.about(self, "Ошибка", "Пользователь не найден.")
                else:
                    QMessageBox.about(self, "Ошибка", "Ошибка выполнения запроса.")
            else:
                QMessageBox.about(self, "Ошибка", "Не удалось открыть базу данных.")

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

    def open_user_panel(self):
        if self.moder_panel is None:
            if db.open():
                query = QSqlQuery()
                query.prepare("SELECT role FROM users1 WHERE login=:login")
                query.bindValue(":login", self.login)

                if query.exec():
                    if query.next():
                        role = query.value(0)  # Получаем значение роли пользователя
                        if role in ["Администратор", "Модератор", "Пользователь"]:
                            QMessageBox.about(self, "Успех!", "Доступ разрешен. Открываю панель пользователя.")
                            self.user_panel = UserPanelWindow(self.login)
                            self.user_panel.show()
                        else:
                            QMessageBox.about(self, "Ошибка", "У вас нет прав доступа к панели пользователя.")
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
