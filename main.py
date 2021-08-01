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

        # self.ui.pushButton_generate_random_signal.clicked.connect(self.update_graph)
        self.ui.pushButton.clicked.connect(self.buttonClick)
        self.setWindowTitle("PySide2 & Matplotlib Example GUI")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

    def drawGraph(self):
        values = self.buttonClick()
        self.ui.MatPlotWidget.canvas.axes.plot(values)
        print("drawing")
        self.ui.MatPlotWidget.canvas.draw()

    def buttonClick(self):
        max = self.maxInput()
        min = self.minInput()
        step=0.1
        x = np.arange(min, max+step, step)
        y = self.functionInput(x)
        self.functionInput(x)

        self.ui.MatPlotWidget.canvas.axes.cla()
        self.ui.MatPlotWidget.canvas.axes.plot(x, y)
        print("drawing")
        self.ui.MatPlotWidget.canvas.draw()

    def minInput(self):
        min = int(self.ui.MinButton.text())
        return min

    def maxInput(self):
        max = int(self.ui.MaxButton.text())
        return max

    def functionInput(self, x):
        function = self.ui.FunctionButton.text()
        y = x
        function = function.replace("^", "**")
        function+="+0"
        print(function)
        temp = ""
        for char in function:
            print(char)
            if char == '*' or char == '+' or char == '-' or char == '/' :
                if("x" in temp):
                    replaceStr=temp
                    if(temp.find("x")!=0):
                        replaceStr=replaceStr.replace("x","*x")
                        function=function.replace(temp,replaceStr)
                temp=""
            else:
                temp += char
        print(function)
        y = eval(function)
        print(y)
        return y

app = QApplication([])
window = MainWidget()
window.show()
app.exec_()

# function to show the plot
plt.show()
