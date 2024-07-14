import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #set window Name
        self.setWindowTitle("Hello World")

        #set vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #create a Label
        my_label = qtw.QLabel("Hello World")
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        # create a entrybox
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name_field')
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #Create a Button
        my_button= qtw.QPushButton("Press Me", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            #add the Text
            my_label.setText(f'Hello {my_entry.text()}')
            #clear
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()

#to run the app
app.exec()