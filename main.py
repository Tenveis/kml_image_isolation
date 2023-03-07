
import gui_class_1
import sys


if __name__ == "__main__":
    app = gui_class_1.QtWidgets.QApplication(sys.argv)
    MainWindow = gui_class_1.QtWidgets.QMainWindow()
    ui = gui_class_1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""
/home/vibi/Downloads/personal/DREAM/test/input_data/csv1.csv
/home/vibi/Downloads/personal/DREAM/test/input_data/images

25.234581
92.490524
25.235609
92.487755

"""
