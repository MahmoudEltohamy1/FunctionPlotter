# importing the required module
import matplotlib.pyplot as plt
import numpy as np
# x axis values
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure


class MatPlotWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvasQTAgg(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    # ------------------ MainWidget ------------------


class MainWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        designer_file = QFile("PlotterDesign.ui")
        designer_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        loader.registerCustomWidget(MatPlotWidget)
        self.ui = loader.load(designer_file, self)

        designer_file.close()

        self.ui.pushButton.clicked.connect(self.buttonClick)
        self.setWindowTitle("Function Plotter")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

    def buttonClick(self):
        self.ui.label_4.setText("")
        max = self.maxInput()
        min = self.minInput()
        step=0.1
        x = np.arange(min, max+step, step)
        function=self.ui.FunctionButton.text()
        y = self.functionInput(x,function)
        self.ui.MatPlotWidget.canvas.axes.cla()
        self.ui.MatPlotWidget.canvas.axes.plot(x, y)
        self.ui.MatPlotWidget.canvas.draw()

    def minInput(self):
        try:
            min = int(self.ui.MinButton.text())
            return min
        except:
            self.ui.label_4.setText("please enter numbers only")


    def maxInput(self):
        try:
            max = int(self.ui.MaxButton.text())
            return max
        except:
            self.ui.label_4.setText("please enter numbers only")

    def functionInput(self, x,function):
        function = function.replace("^", "**")
        function+="+0"
        temp = ""
        for char in function:
            if char == '*' or char == '+' or char == '-' or char == '/' :
                if("x" in temp):
                    replaceStr=temp
                    if(temp.find("x")!=0):
                        replaceStr=replaceStr.replace("x","*x")
                        function=function.replace(temp,replaceStr)
                temp=""
            else:
                temp += char
        try:
            y = eval(function)
            return y
        except:
            self.ui.label_4.setText("Invalid input eg: x^2 or 3x^3+2x^2")

app = QApplication([])
window = MainWidget()
window.show()
app.exec_()

# function to show the plot
plt.show()
