
import sys
import os

from interface_ui import *
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtCore import QEvent

#IMPORT CRUD FUNCTIONS

from serverInventory import LaptopInventoryFunctions as li
from repairsRecord import RepairsRecord as rr
from serverInventory import EquipInventoryFunctions as ei
from inuseInventory import InuseInvFunctions as iu
from adminSettings import AdminSettings as ams
from dashboard import HomeDashBoardFunctions as hd
import session
import connections
from datetime import datetime


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class LoginWindow(QtWidgets.QDialog):
    def __init__(self):

        super(LoginWindow, self).__init__()
        uic.loadUi(resource_path('login.ui'), self)
        self.oldPos = self.pos()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.loginBtn.clicked.connect(self.authenticate)

        self.closeWindowsBtn.clicked.connect(self.closeLogin)
        self.loginUsername.textChanged.connect(lambda: textChange(self))
        self.txtLoginError.hide()
        self.txtPasswordError.hide()
        self.txtUserError.hide()

        conn = connections.conndb()
        checkConn = conn.create_connection()
        if checkConn=="Connected":
            self.txtDatabaseconnection.setText("Database: Connected ✅")
        else:
            self.txtDatabaseconnection.setText("Database: Not Connected ❌")

        def textChange(self):
            self.txtPasswordError.hide()
            self.txtUserError.hide()
       
    def closeLogin(self):
        self.close()
        sys.exit()

    def loginUserDetails(self):
        sessionA = session.sessionAuth
        userDetails = sessionA.sessionUser(self)
        return (userDetails)

    def authenticate(self):
        conn = connections.conndb()
        checkConn = conn.create_connection()
        if checkConn=="Connected":
            self.txtDatabaseconnection.setText("Database: Connected ✅")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Failed Connection")
            msg.setText("No Database Connection!")
            x = msg.exec_()
            self.txtDatabaseconnection.setText("Database: Not Connected ❌")
            

            
        # self.msg = QtWidgets.QMessageBox()

        sessionA = session.sessionAuth
        checkAuth = sessionA.checkAuthentication(self)
        if checkAuth=="Approved":
            username = self.loginUsername.text()
            password = self.loginPassword.text()
            self.close()
            window.show()
            window.functionClass()
            userdetail = username
            window.userSession(str(userdetail))
            
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.log_App = LoginWindow()
        self.log_App.show()

    def functionClass(self):

         #EXPAND CENTER MENU WIDGET SIZE
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.informationBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #CLOSE CENTER MENU WIDGET SIZE
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

           #EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

             #CLOSE RIGHT MENU WIDGET SIZE
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

         #CLOSE NOTIFICATION MENU WIDGET SIZE
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        #--------------- LAPTOP INVENTORY FUNCTIONS ----------------------------------#
        li.displayLaptopTable(self,li.getAllLaptops(self))
        self.ui.laptopRecordsTable.clicked.connect(lambda: li.getData(self))
        self.ui.addLaptopBtn.clicked.connect(lambda: li.addLaptop(self))
        self.ui.updateLaptopBtn.clicked.connect(lambda: li.updateLaptop(self))
        self.ui.deleteLaptopBtn.clicked.connect(lambda: li.deleteLaptop(self))
        self.ui.txtLapInvSearch.textChanged.connect(lambda: li.search(self))

        self.ui.sendToRepairBtn.clicked.connect(lambda: li.sendforrepair(self))
        self.ui.laptopRecordGenerateExcelBtn.clicked.connect(lambda: li.laptopGenerateCSV(self))
        
        
        #--------------- REPAIRS INVENTORY FUNCTIONS ----------------------------------#

        rr.displayRepairsLaptopTable(self,rr.getAllLaptops(self))
        self.ui.RepairsRecordTable.clicked.connect(lambda: rr.getData(self))
        self.ui.addSentForRepairBtn.clicked.connect(lambda: rr.addLaptop(self))
        self.ui.clearSentForRepairBtn.clicked.connect(lambda: rr.clearOption(self))
        self.ui.updateSentForRepairBtn.clicked.connect(lambda: rr.updateLaptop(self))
        self.ui.txtSearchRepairs.textChanged.connect(lambda: rr.search(self))
        self.ui.repairsGenerateCSVBtn.clicked.connect(lambda: rr.returnGenerateCSV(self))
        self.ui.ssrBtn.clicked.connect(lambda: rr.sendBacktoServer(self))
        self.ui.ssuBtn.clicked.connect(lambda: rr.sendBacktoUser(self))

        #--------------- EQUIPMENTS INVENTORY FUNCTIONS ----------------------------------#
        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
        self.ui.updateEquipBtn.clicked.connect(lambda: ei.updateEquip(self))
        self.ui.addExtraEquipBtn.clicked.connect(lambda: ei.addEquip(self))
        self.ui.equipRecordTable.clicked.connect(lambda:ei.getEquipData(self))
        self.ui.updateExtraEquipBtn.clicked.connect(lambda: ei.updateExtraEquip(self))
        self.ui.deleteExtraEquipBtn.clicked.connect(lambda: ei.deleteExtraEquip(self))
        self.ui.equipRecordGenerateExcelBtn.clicked.connect(lambda: ei.equipmentsGenerateCSV(self))


        #--------------- INUSE INVENTORY FUNCTIONS ----------------------------------#
        iu.displayInuseTable(self,iu.getAllInuseItems(self))
        self.ui.addInuseInvBtn.clicked.connect(lambda: iu.addInuseInv(self))
        self.ui.InUseTableWidget.clicked.connect(lambda: iu.getInuseData(self))
        self.ui.clearInuseInvBtn.clicked.connect(lambda: iu.clearInuse(self))
        self.ui.InUseRecordSearchTxt.textChanged.connect(lambda: iu.inuseSearch(self))
        self.ui.inuseInvGenerateExcelBtn.clicked.connect(lambda: iu.inuseGenerateCSV(self))
        self.ui.updateInuseInvBtn.clicked.connect(lambda: iu.updateInuse(self))

        self.ui.sendForRepairBtn.clicked.connect(lambda: iu.sendForRepairs(self))
        self.ui.refreshSpareLaptop.clicked.connect(lambda: iu.load_spare_laptops(self))
        self.ui.offboardingBtn.clicked.connect(lambda: iu.offboardingRequest(self))

        #--------------- ADMIN FUNCTIONS ----------------------------------#
        #self.ui.registerAdminInfoBtn.clicked.connect(lambda: ams.adminRegister(self))
        self.ui.adminProfileSettingBtn.clicked.connect(lambda: ams.adminPersonalInfoUpdate(self))
        self.ui.adminChangePasswordBtn.clicked.connect(lambda: ams.personalPasswordChange(self))
        self.ui.logoutBtn.clicked.connect(lambda: ams.sessionLogout(self))

        #--------------- ADMIN DASHBOARD ----------------------------------#
        ams.displayAdminDashTable(self,ams.getAllAdmins(self))
        self.ui.adminDashTable.clicked.connect(lambda: ams.getAdminData(self))
        self.ui.editAdminInfoBtn.clicked.connect(lambda: ams.adminEditProfile(self))
        self.ui.deleteAdminInfoBtn.clicked.connect(lambda: ams.adminDeleteProfile(self))
        self.ui.registerAdminInfoBtn.clicked.connect(lambda: ams.adminRegisterProfile(self))
        #--------------- COPYRIGHT AREA ----------------------------------#
        now = datetime.now()
        currentYear = now.strftime("%Y")
        self.ui.copyrightArea.setText(f"Copyright ©️ Nayan Bastola {currentYear}")

        #--------------- HOME DASHBOARD ----------------------------------#
        self.ui.serverRoomDashCount.setText(str(hd.getServerCount(self)))
        self.ui.equipRoomCount.setText(str(hd.getEquipmentCount(self)))
        self.ui.repairsRoomDashCount.setText(str(hd.getRepairsCount(self)))
        self.ui.inuseRoomDashCount.setText(str(hd.getInuseCount(self)))

        #--------------- LOGIN USERS FUNCTIONS ----------------------------------#
    def userSession(self,userdetail):
        user = str(userdetail)
        cnx = connections.conndb()
        strsql = f"SELECT * FROM adminusers WHERE adminUsername ='{user}'"
        result = cnx.queryResult(strsql)
        for user in result:
            adminid = (str(user[0]))
            adminfname = (str(user[1]))
            adminlname = (str(user[2]))
            adminUsername = (str(user[3]))
            adminEmail = (str(user[5]))
            adminStatus = (str(user[6]))
        
        self.ui.sessionID.setText(adminid)
        self.ui.sessionEmail.setText(adminEmail)
        self.ui.sessionStatus.setText(adminStatus+" ✅")
        self.ui.sessionUser.setText(adminfname+" "+adminlname)
        self.ui.sessionUsername.setText(adminUsername)
        self.ui.adminSettingsID.setText(adminid)
        self.ui.adminSettingsUsername.setText(adminUsername)
        self.ui.adminSettingsFname.setText(adminfname)
        self.ui.adminSettingsLname.setText(adminlname)
        self.ui.adminSettingsEmail.setText(adminEmail)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()    
    sys.exit(app.exec_())