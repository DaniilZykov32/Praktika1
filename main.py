from ui import Ui_Form
from PySide2.QtWidgets import  QApplication, QWidget
import sys
from datetime import datetime



class MainW():
    def __init__(self,ui):
        super(MainW, self).__init__()
        self.ui = ui
        self.date = ui.calendarWidget.selectedDate()
        self.date_2 = ui.calendarWidget_2.selectedDate()
        self.initUi()
        self.show_date(self.date)
        # self.show_date_2(self.date)
        
        
        
    a = ''
    

    def initUi(self):
        
        date = self.ui.calendarWidget.selectedDate()
        date_2 = self.ui.calendarWidget_2.selectedDate()
        print(self.ui.calendarWidget.clicked['QDate'])

        self.ui.calendarWidget.clicked['QDate'].connect(self.show_date)
        self.ui.calendarWidget_2.clicked['QDate'].connect(self.show_date)
    
    # def show_date_2(self, date):
    #     return date

    def show_date(self, date):
        b = self.ui.calendarWidget.selectedDate()
        a = self.ui.calendarWidget_2.selectedDate()
        
        year , month , day = b.getDate()
        first_date = datetime(year, month, day)
        
        
        y, m, d = a.getDate()
        
        sec_date = datetime(y,m ,d)
        delta = first_date - sec_date
        print(delta, a)
        self.ui.lineEdit.setText(str(delta))
    
    
    

def main():
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ex=MainW(ui)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()