from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from frame_main import Ui_mainmenu
from frame_logon import Ui_register_2
from frame_managemenu import Ui_manawindow
from frame_timeinsert import Ui_insert_time
#excel表格读取
import xlrd
import sys
from PyQt5.QtCore import *
import copy

# 主界面
class ManaMenu(QMainWindow,Ui_manawindow):
    def __init__(self):
        super(ManaMenu,self).__init__()
        self.setupUi(self)

        self.exit.clicked.connect(self.exit1)
        self.insert.clicked.connect(self.insert_parameter)
        self.reset.clicked.connect(self.resset)
        global N
        self.model = QStandardItemModel(N, N)
        self.tableView.setModel(self.model)

        # 计时器
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refreshtime)


    def refreshtime(self):
        global time, b_list,N,t,alist_len,alist
        if len(b_list)==0:
            b_list = copy.deepcopy(alist)
        x = b_list[0][0]
        y = b_list[0][1]
        """
        if x>N or y>N:
            z = x-N
            for j in (x-N):
        """
        self.model.setItem(x, y, QStandardItem('1'))
        self.textBrowser.append('Time:{0}(min)    Position: ({1},{2})'
                                .format(t, x, y))
        del b_list[0]
        if t == time:
            self.timer.stop()
            self.textBrowser.append('执行完毕，总时间：{0}（min）'.format(t))
            return
        t += 1
        if len(b_list)==0:
            self.timer.stop()
            self.textBrowser.append('执行完毕，总时间：{0}（min）'.format(alist_len))
            return


    def exit1(self):
        global ui
        reply = QMessageBox.information(self, "注意", "是否要退出？", QMessageBox.Yes|QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.close()
            ui.show()
        else:
            pass

    def insert_parameter(self):
        global para_insert
        para_insert.show()

    def resset(self):
        if self.insert.isEnabled()!=True:
            self.insert.setEnabled(1)
            self.model.clear()
            global N,t
            t = 1
            self.model = QStandardItemModel(N, N)
            self.tableView.setModel(self.model)
            self.textBrowser.clear()

    """
    def paintGL(self):
        # 20*20
        global N,time,xp,yp

        xgrid = gl.GLGridItem(size=QtGui.QVector3D(N, N, 1), color=(255, 255, 255))
        self.openGLWidget.addItem(xgrid)



        
        axis = gl.GLAxisItem()
        self.openGLWidget.addItem(axis)


        global drawpal

        # 创建一支画笔并设置属性
        pen = QPen(Qt.red, 2, Qt.SolidLine)  # pen = QPen(【1】颜色, 【2】线条粗细, 【3】线条形式)
        self.drawpal.setPen(pen)
        self.drawpal.setBrush(QColor(255, 0, 0))

        # 接着绘制各种图形
        self.drawEllipse(self.openGLWidget)  # 绘制圆 椭圆
        self.openGLWidget.drawRect(2,2,3,3)  ##绘制矩形
        self.openGLWidget.drawRoundedRect(5,5,4,4, 1, 1)  # 绘制圆角矩形

    
        # 20*20
        xgrid = gl.GLGridItem()
        ygrid = gl.GLGridItem()
        zgrid = gl.GLGridItem()
        self.openGLWidget.addItem(xgrid)
        self.openGLWidget.addItem(ygrid)
        self.openGLWidget.addItem(zgrid)

    

    def use_gl(self):

        # 自定义的方法

        self.openGLWidget.paintGL = self.paintGL()
"""


# 输入数据
class Insert_Time(QWidget,Ui_insert_time):
    def __init__(self):
        super(Insert_Time,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定

    # 子窗体自定义事件
    def btnClick(self):
        global time, manamenu, xp, yp
        if self.spinBox.value() != 0 and self.positionx.value() >= 0 and self.positiony.value() >= 0:
            time = self.spinBox.value()
            self.spinBox.setValue(0)
            manamenu.insert.setDisabled(1)
            manamenu.textBrowser.append('执行中，请勿退出！')
            manamenu.model.setItem(xp, yp, QStandardItem('1'))
            manamenu.textBrowser.append('Time:{0}(min)    Position: ({1},{2})'
                                    .format(0, xp, yp))
            manamenu.timer.start()
        else:
            reply = QMessageBox.information(self, "注意", "您未输入完整参数", QMessageBox.Yes)
        self.close()


# 登录
class ManaLogon(QWidget,Ui_register_2):
    def __init__(self):
        super(ManaLogon,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定

    # 子窗体自定义事件
    def btnClick(self):
        global manamenu, ui
        id = self.manaid.text()
        pa = self.manapassword.text()
        wb = xlrd.open_workbook(filename='用户登录信息.xlsx')  # 打开文件
        sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
        flag = 1
        for row in range(1, sheet1.nrows):
            name = str(sheet1.cell(row, 0).value)
            ctype = sheet1.cell(row, 1).ctype  # 表格的数据类型
            password = sheet1.cell_value(row, 1)
            if ctype == 2 and password % 1 == 0.0:  # ctype为2且为浮点
                password = int(password)  # 浮点转成整型
            passwords = repr(password)
            if name == id and passwords == pa:
                flag = 0
                break
        if flag==1:
            reply = QMessageBox.information(self, "注意", "该管理员账号不存在\n请检查账号和密码", QMessageBox.Yes)
        elif flag==0:
            manamenu.show()
            ui.close()
        self.manaid.clear()
        self.manapassword.clear()
        self.close()


# 初始界面
class MainWidget(QMainWindow,Ui_mainmenu):
    def __init__(self):
        super(MainWidget,self).__init__()
        self.setupUi(self)

if  __name__=="__main__":
    N = 30
    time = 0
    xp = 0
    yp = 0
    alist = [
        [0,1],
        [0,2]
    ]
    b_list = copy.deepcopy(alist)
    alist_len = len(alist)
    t = 1

    app=QtWidgets.QApplication(sys.argv)

    ui = MainWidget()

    manalg = ManaLogon()

    manamenu = ManaMenu()

    para_insert = Insert_Time()

    # 点击登录
    manalog = ui.logon
    manalog.clicked.connect(manalg.show)

    ui.show()
    sys.exit(app.exec_())
