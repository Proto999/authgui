import sys

from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication


def test_db_connection():
    # Создаем объект базы данных
    db = QSqlDatabase.addDatabase("QODBC")

    # Устанавливаем параметры подключения
    db.setDatabaseName("DRIVER={SQL Server};SERVER=DESKTOP-A320SRA;DATABASE=UserAuth;UID=admin;PWD=1234")

    # Пытаемся открыть соединение
    if db.open():
        print("Подключение к базе данных успешно.")
        db.close()  # Закрываем соединение после проверки
    else:
        print("Ошибка подключения к базе данных:", db.lastError().text())


if __name__ == "__main__":
    test_db_connection()
