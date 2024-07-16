import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QMessageBox
import mysql.connector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt MySQL Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Widgets
        self.label = QLabel("Enter MySQL Connection Details:")
        layout.addWidget(self.label)

        self.host_edit = QLineEdit(self)
        self.host_edit.setPlaceholderText("Enter host")
        layout.addWidget(self.host_edit)

        self.user_edit = QLineEdit(self)
        self.user_edit.setPlaceholderText("Enter username")
        layout.addWidget(self.user_edit)

        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText("Enter password")
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_edit)

        self.database_edit = QLineEdit(self)
        self.database_edit.setPlaceholderText("Enter database name")
        layout.addWidget(self.database_edit)

        self.connect_button = QPushButton("Connect to MySQL", self)
        self.connect_button.clicked.connect(self.connect_mysql)
        layout.addWidget(self.connect_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_mysql(self):
        try:
            # Get connection details from QLineEdit widgets
            host = self.host_edit.text()
            user = self.user_edit.text()
            password = self.password_edit.text()
            database = self.database_edit.text()

            # Connect to MySQL server
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if connection.is_connected():
                QMessageBox.information(self, "Connection Successful", "Connected to MySQL database successfully!")

                # Perform database operations here

                # Close connection
                connection.close()

        except mysql.connector.Error as error:
            QMessageBox.critical(self, "Error", f"Failed to connect to MySQL database: {error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
