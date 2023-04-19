from PyQt6.QtWidgets import QApplication, QBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from datetime import datetime
import sys

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()

        name_label = QLabel('Name')
        self.name_line_edit = QLineEdit()

        self.date_label = QLabel('Date of Birth (MM/DD/YY)')
        self.date_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate Age')
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel('')

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(self.date_label, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_line_edit.text()
        extract_year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
        age = current_year - extract_year_of_birth
        self.output_label.setText(f'{self.name_line_edit.text()} is {age} years old!')

setup_app = QApplication(sys.argv)
age_calc = AgeCalculator()
age_calc.show()
sys.exit(setup_app.exec())






# Always add the QWidget Class as the Parent Class while creating basic projects which only include one
# simple window.
# THERE ARE SPECIFIC METHODS FOR SPECIFIC TYPE OF WINDOWS.
# The 'class AgeCalculator(QWidget)' line of code which represents the class, we are recreating this line of code:
# AgeCalculator = Qwidget()
# This 'grid = QGridLayout()' the widget grid. THIS IS A MUST!
# This 'name_label = QLabel('Name')' generates an line of text according to what you give.
# The argument that the QLabel takes is the text you want to display.

# name_line_edit = QLineEdit()
# This produces an input box. YOU SHOULD ALWAYS USE THIS TO GET INPUT DATA FROM.

# THE GRID IS LIKE AN INVISIBLE LAYOUT WHICH WILL ADD ALL OF THE WIDGETS THAT WE CREATED LIKE THE QLabel,
# QLineEdit IN THE QWidget GUI.
# To add all of the Widgets into the grid:
# We should use the .addWidget() method to the instance which contains the grid method. In our case, it's the
# grid variable >> grid = QGridLayout()
# grid.addWidget(name_label, 0, 0)
# grid.addWidget(name_line_edit, 0, 1)
# grid.addWidget(date_label, 1, 0)
# grid.addWidget(date_line_edit, 1, 1)

# The first argument in the .addWidget() method are the widgets that we created:
# name_label = QLabel('Name')
# name_line_edit = QLineEdit()
# date_label = QLabel('Date of Birth (MM/DD/YY)')
# date_line_edit = QLineEdit()

# The Second Argument is the co-ordinates of the widget.
# The Co-ordinates work like this:
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9 10
# 2 3 4 5 6 7 8 9 10 11
# 3 4 5 6 7 8 9 10 11 12
# 4 5 6 7 8 9 10 11 12 13
# 5 6 7 8 9 10 11 12 13 14
# 6 7 8 9 10 11 12 13 14 15
# 7 8 9 10 11 12 13 14 15 16
# 8 9 10 11 12 13 14 15 16 17
# 9 10 11 12 13 14 15 16 17 18

# (DON'T MIND THE SLOPE ON THE RIGHT. IT LACKS THE JUSTIFICATION)

# To run the app:
# We have to import the sys library to add it to the QApplication method
# Syntax:
#setup_app = QApplication(sys.argv)
# age_calc = AgeCalculator()
# age_calc.show()
# sys.exit(setup_app.exec())

# So, according to the rules of OOP, there cannot be an __init__ method inside a child class.
# BUT, YOU CAN ADD AN __init__ METHOD WHEN YOU HAVE AN SUPER CLASS INSIDE IT.
# WHEN ADDING THIS SUPER CLASS, YOU CAN NOW BE ABLE TO OVERWRITE THE PARENT'S __init__ METHOD.
# THE PARENT CLASS IN OUR CASE IS THE QWidget Class
# To add the Super-Class:
# super().__init__()
# Just add this line of code in the child's __init__ method.

# Now if you run the code, you will get the window, but no widgets will be shown in the window.
# That is because the grid is created, but the grid is INVISIBLE. To be able to show the grid, you have to
# create an layout and add the grid to the layout.
# To do that:
# self.setLayout(grid)
# This should be added in the child class
# Now the reason why we are adding the self instance and instantiating the .setLayout() method even though
# the child class, does not get any arguments in it's __init__ method is because the PARENT CLASS' __init__
# METHOD HAS THIS INSTANCE VARIABLE. As this child class shares every variables and instance methods, we can
# be able to use it. :^

# >:>> IMPORTANT <:<< THE MAIN REASON WHY WE ARE ADDING THE CODE IN THE __init__ METHOD IS JUST TO
# DISPLAY THE WIDGET. BECUASE IN EVERY CLASS, WHENEVER THE CLASS IS CALLED AND EXECUTED, THE CODE IN THE
# __init__ METHOD WILL BE THE FIRST ONE TO BE EXECUTED.
# AS YOU KNOW, THE .lineEdit() method gets input from the user. BUT IF YOU DISPLAY IT OR PRINT IT OUT, YOU WILL
# GET SOMETHING LIKE THIS: <PyQt6.QtWidgets.QLineEdit object at 0x0000000049L435KB4334G>
# YOU SHOULD ALWAYS CONVERT THE .LineEdit() method to an text format when printing it or displaying it.
# To do that:
# variableName.LineEdit.text()
# USE THE .text() FUNCTION.
# DO NOT ADD THE PARANTHESIS WITH THE .LineEdit method when converting it to text.


# IF YOU DON'T UNDERSTAND:
# THIS: extract_year_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y').date().year
# WE ARE ACTUALLY CONVERTING THE 'date_of_birth' INSTANCE VARIABLE TO A DATE FORMAT USING THE .date()
# FUNCTION. AFTER THAT, WE USE THE .year PROPERTY METHOD TO EXTRACT THE YEAR.
# TIP >>> .month is a Property method to extract the month, and the .day is a Property Method to extract the day.
# THESE ARE VERY GOOD PROPERTY METHODS TO USE!