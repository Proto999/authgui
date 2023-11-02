from PySide6.QtSql import QSqlDatabase

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("DRIVER={SQL Server};SERVER=DESKTOP-A320SRA;DATABASE=users;UID=admin;PWD=1234")

if db.open():
    print("Соединение установлено")
else:
    print("Ошибка при установке соединения:", db.lastError().text())
