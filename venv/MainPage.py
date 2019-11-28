import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

CONST_SIZE_X = 540
CONST_SIZE_Y = 960

mainPage = uic.loadUiType("UI/main.ui")[0]
newsPage = uic.loadUiType("UI/news.ui")[0]
settingPage = uic.loadUiType("UI/setting.ui")[0]
newsSettingPage = uic.loadUiType("UI/newsSetting.ui")[0]


# 뉴스 페이지 위젯
class NewsSettingWindow(QWidget, newsSettingPage):
    def __init__(self, parent=None):
        super(NewsSettingWindow, self).__init__(parent)
        self.setupUi(self)


# 뉴스 페이지
class NewsWindow(QMainWindow, newsPage):
    def __init__(self, parent=None):
        super(NewsWindow, self).__init__(parent)
        self.setupUi(self)
        self.newsSetting.clicked.connect(self.openNewsSetting)

    # 뉴스 설정 창 띄움
    def openNewsSetting(self):
        tempX = self.x() + 70
        tempY = self.y() + 380
        self.newsSettingPage = NewsSettingWindow()
        self.newsSettingPage.setGeometry(tempX, tempY + 30, 400, 200)
        self.newsSettingPage.show()


# 설정 페이지
class SettingWindow(QMainWindow, settingPage):
    def __init__(self, parent=None):
        super(SettingWindow, self).__init__(parent)
        self.setupUi(self)

    # 메인 페이지로 이동
    def moveToMain(self):
        tempX = self.x()
        tempY = self.y()
        self.close()
        self.mainWindow = MainWindow()
        self.mainWindow.setGeometry(tempX, tempY + 30, CONST_SIZE_X, CONST_SIZE_Y)
        self.mainWindow.show()


# 메인 페이지
class MainWindow(QMainWindow, mainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.newsTitle.hide()
        self.setGeometry(10, 40, CONST_SIZE_X, CONST_SIZE_Y)
        self.mainGoToNewsList.clicked.connect(self.moveToNews)
        self.mainSetting.clicked.connect(self.moveToSetting)

    # 설정 페이지로 이동
    def moveToSetting(self):
        self.centralWidget().deleteLater()

    # 뉴스 페이지로 이동
    def moveToNews(self):
        tempX = self.x()
        tempY = self.y()
        self.close()
        self.newsWindow = NewsWindow()
        self.newsWindow.setGeometry(tempX, tempY+30, CONST_SIZE_X, CONST_SIZE_Y)
        self.newsWindow.show()


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
