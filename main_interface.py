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


import fire_state

# 主界面
class ManaMenu(QMainWindow,Ui_manawindow):
    def __init__(self):
        super(ManaMenu, self).__init__()
        self.setupUi(self)

        self.exit.clicked.connect(self.exit1)
        self.insert.clicked.connect(self.insert_parameter)
        self.reset.clicked.connect(self.resset)
        global N
        self.model = QStandardItemModel(N, N)
        self.tableView.setModel(self.model)


        # self.textBrowser.append('Time:{0}(min)    Position: ({1},{2})'
        #                         .format(t, x, y))
        # del b_list[0]



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
        global para_insert
        if self.insert.isEnabled()!=True:
            self.insert.setEnabled(1)
            self.model.clear()
            global N, initial_list
            t = 1
            for z in range(N):
                ii_list = []
                for rep in range(N):
                    ii_list.append(0)
                initial_list.append(ii_list)
            self.model = QStandardItemModel(N, N)
            para_insert.tablemodel = MyTableModel(initial_list)
            self.tableView.setModel(self.model)
            self.textBrowser.clear()



# 输入数据
class Insert_Time(QWidget,Ui_insert_time):
    def __init__(self):
        super(Insert_Time,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClick)  # 按钮事件绑定
        self.tablemodel = 0

    def refreshtime(self):
        global time, N, alist
        b_list = copy.deepcopy(alist)
        # x = b_list[0][0]
        # y = b_list[0][1]
        """
        if x>N or y>N:
            z = x-N
            for j in (x-N):
        """
        global initial_list, manamenu, xp, yp
        if xp>0 and yp>0 and xp<N and yp<N:
            initial_list[xp-1][yp-1] = 2
        for key, value in b_list.items():
            if key[0]<0 or key[1]<0 or key[0]>=N or key[1]>=N:
                continue
            if value == 1:
                initial_list[key[0]][key[1]] = 1

        self.tablemodel = MyTableModel(initial_list)
        manamenu.tableView.setModel(self.tablemodel)

    # 子窗体自定义事件
    def btnClick(self):
        global time, manamenu, xp, yp, alist,initial_list
        if self.spinBox.value() != 0 and self.positionx.value() >= 0 \
                and self.positiony.value() >= 0 and self.spin_wind.value() >= 0 and self.spin_angle.value() >= 0:
            time = self.spinBox.value()
            wind = self.spin_wind.value()
            angle = self.spin_angle.value()
            xp = self.positionx.value()
            yp = self.positiony.value()
            x = self.positionx.value()
            x = x-1
            y = self.positiony.value()
            y = y-1
            if wind == 0:
                wind = 1
            if angle == 0:
                angle = 1
            fire_state.clear_map()
            alist = fire_state.cacl_map(wind, angle, (x, y), 1, 1, time, 0)

            # self.spinBox.setValue(0)
            manamenu.insert.setDisabled(1)
            manamenu.textBrowser.append('执行中，请勿退出！')
            self.refreshtime()
        else:
            reply = QMessageBox.information(self, "注意", "您未输入完整参数", QMessageBox.Yes)
        self.close()



#模型
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
            # vvvv this is the magic part
        elif role == Qt.BackgroundRole:
            #if self.arraydata[index.row()][index.column()] == 1:
            if self.arraydata[index.row()][index.column()] == 1:
                return QBrush(Qt.red)
            if self.arraydata[index.row()][index.column()] == 2:
                return QBrush(Qt.yellow)
            else:
                return QVariant()
            # ^^^^ this is the magic part
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant()



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
    alist = dict()

    # pos = fire_state.cacl_map(2, 15, (5, 6), 1, 1, 5, 0)
    # alist = pos
    # # [
    # #     [0,1],
    # #     [0,2]
    # # ]
    b_list = copy.deepcopy(alist)
    alist_len = len(alist)
    t = 1
    initial_list = []

    app=QtWidgets.QApplication(sys.argv)

    ui = MainWidget()

    manalg = ManaLogon()

    manamenu = ManaMenu()

    para_insert = Insert_Time()

    for z in range(N):
        ii_list = []
        for rep in range(N):
            ii_list.append(0)
        initial_list.append(ii_list)

    # 点击登录
    manalog = ui.logon
    manalog.clicked.connect(manalg.show)

    ui.show()
    sys.exit(app.exec_())
