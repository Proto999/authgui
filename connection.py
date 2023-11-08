import sys


from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    db = QSqlDatabase("QPSQL")
    db.setHostName("localhost")
    db.setDatabaseName('UserAuth')
    db.setUserName('postgres')
    db.setPassword('1')

    if not db.open():
        print("\n=> Unable to connect to the database")
        print('\nConnection   : ', db.isOpen())
        print('Drivers      : ', db.drivers())
        print('Last error   : ', db.lastError().text())
        print('\nIs QPSQL driver available : ', db.isDriverAvailable('QPSQL'))
        sys.exit(1)
    else:
        print("\n=> Connect to the database successful")

    app.exec()