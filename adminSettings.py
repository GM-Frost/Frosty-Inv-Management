import os
import sys
import connections
from Custom_Widgets.Widgets import *
from interface_ui import *
from PySide2.QtWidgets import QTableWidgetItem
from datetime import datetime

class AdminSettings():
    def __init__(self,arg):
        super(AdminSettings,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
    
    def adminEditProfile(self):
        msg = QMessageBox()
        adminID = self.ui.txtDashAdminID.text()
        firstName = self.ui.txtDashAdminFname.text().title()
        lastName = self.ui.txtDashAdminLname.text().title()
        username = self.ui.txtDashAdminUsername.text().lower()
        email = self.ui.txtDashAdminEmail.text().lower()
        status = self.ui.txtDashAdminStatusCombo.currentText()
        flag = self.ui.txtDashAdminFlagCombo.currentText()
        updatedBy = self.ui.sessionUser.text()
        currentAdminID = self.ui.adminSettingsID.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        if (adminID==""):
            QMessageBox.information(self, "Required", "Please select the Admin from table to make changes")
        elif (username=="" or firstName=="" or lastName=="" or email=="" or status =="" or flag==""):
            QMessageBox.information(self, "Required", "Please Fill out all Values")
        else:
            conn = connections.conndb()
            get_admin_status =  f"""SELECT adminStatus,adminFlag FROM adminusers where adminID='{currentAdminID}'"""
            c = conn.queryResult(get_admin_status)
            adminStatus = str(c[0][0])
            adminFlag = str(c[0][1])

                      
            msg = QMessageBox.question(self, "Make Changes?", "Are you sure you edit this Admin?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                if (adminFlag == "Super Admin" or adminFlag=="Main Admin"):
                    update_admin_data = f"""
                    UPDATE adminusers SET adminFname='{firstName}',adminLname='{lastName}',adminEmail='{email}',adminStatus='{status}', adminFlag='{flag}',updatedBy='{updatedBy}',changeDate='{changeDate}' WHERE adminID='{adminID}';
                    """
                    if not (conn.queryExecute(update_admin_data)):
                        conn.queryClose
                        QMessageBox.information(self, "Profile Updated", "Application closing to assign Changes")
                        QApplication.quit()
                    else:
                        msg.setWindowTitle("Error")
                        msg.setText("Something went wrong. Profile Couldnot be Updated!")
                        x = msg.exec_()
                elif (adminFlag=="Admin" and adminStatus=="Active"):
                    if(flag=="Super Admin"or flag=="Main Admin"):
                        QMessageBox.information(self, "Incomplete", "Sorry you donot have enough Privilege to Add Super Admin or Main Admins.\nPlease Change Admin Flag")
                    else:
                        update_normaladmin_data = f"""UPDATE adminusers SET adminFname='{firstName}',adminLname='{lastName}',adminUsername='{username}',adminEmail='{email}',updatedBy='{updatedBy}',changeDate='{changeDate}' WHERE adminID='{adminID}';
                        """
                        msg = QMessageBox.question(self, "Make Changes?", "Are you sure you edit this Admin?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if msg == QMessageBox.Yes:
                            if not (conn.queryExecute(update_normaladmin_data)):
                                conn.queryClose
                                QMessageBox.information(self, "Profile Updated", "Application closing to assign Changes")
                                QApplication.quit()
                else:
                    QMessageBox.information(self, "Incomplete", "Sorry you donot have enough Privilege to make Changes")
            else:
                pass        
        
    def adminDeleteProfile(self):
        msg = QMessageBox()
        adminID = self.ui.txtDashAdminID.text()
        currentAdminID = self.ui.adminSettingsID.text()

        if (adminID==""):
            QMessageBox.warning(self, "Selection Required", "Please select the Admin from table to make changes")
        else:
            conn = connections.conndb()
            get_admin_status =  f"""SELECT adminStatus,adminFlag FROM adminusers where adminID='{currentAdminID}'"""
            c = conn.queryResult(get_admin_status)
            adminStatus = str(c[0][0])
            adminFlag = str(c[0][1])
            msg = QMessageBox.question(self, "Delete?", "Are you sure you Delete this Admin?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                if (adminFlag == "Super Admin" or "Main Admin"):
                    delete_admin = f"""DELETE FROM adminusers WHERE adminID='{adminID}'"""
                    if not (conn.queryExecute(delete_admin)):
                        conn.queryClose
                        QMessageBox.information(self, "Admin Deleted", "Application closing for changes being applied")
                        QApplication.quit()
                else:
                    QMessageBox.warning(self, "Incomplete", "Sorry you donot have enough Privilege to Delete other Admins")
            else:
                pass

    def adminRegisterProfile(self):
        msg = QMessageBox()
        regfirstName = self.ui.txtDashRegAdminFname.text().title()
        reglastName = self.ui.txtDashRegAdminLname.text().title()
        regusername = self.ui.txtDashRegAdminUsername.text().title()
        regpassword = self.ui.txtDashRegAdminPassword.text().lower()
        regemail = self.ui.txtDashRegAdminEmail.text().lower()
        regstatus = self.ui.txtDashRegAdminStatusCombo.currentText()
        regflag = self.ui.txtDashRegAdminFlagCombo.currentText()

        currentAdminID = self.ui.adminSettingsID.text()
        updatedBy = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        conn = connections.conndb()

        get_admin_status =  f"""SELECT adminStatus,adminFlag FROM adminusers where adminID='{currentAdminID}'"""
        c = conn.queryResult(get_admin_status)
        adminStatus = str(c[0][0])
        adminFlag = str(c[0][1])

        dupEntryQuery =  f"""SELECT * FROM adminusers where adminUsername='{regusername}'"""
        conn = connections.conndb()
        dupEntry = conn.queryResult(dupEntryQuery)


        if (regfirstName=="" or reglastName=="" or regusername=="" or regpassword=="" or regemail=="" or regstatus=="" or regflag==""):
            QMessageBox.information(self, "Information Required", "Please fillout every Details for Admin Registration")
        else:  
            if dupEntry:
                QMessageBox.information(self, "Duplicate Entry", "This Admin Username is present on the Records.\nPlease assign new Username")
            else:
                if (adminFlag == "Admin"):
                    if (regflag =="Super Admin" or regflag =="Main Admin"):
                        QMessageBox.warning(self, "Incomplete", "Sorry you donot have enough Privilege to add Super/Main Admins")
                    else:
                        register_admin_data = f"""
                        Insert into adminusers (adminFname,adminLname,adminUsername,adminPassword,adminEmail,adminStatus,adminFlag,updatedBy,changeDate) VALUES ('{regfirstName}','{reglastName}','{regusername}',"{regpassword}",'{regemail}','{regstatus}','{regflag}','{updatedBy}','{changeDate}');
                        """
                        if not (conn.queryExecute(register_admin_data)):
                            conn.queryClose
                            msg = QMessageBox()
                            self.ui.txtDashRegAdminFname.setText("")
                            self.ui.txtDashRegAdminLname.setText("")
                            self.ui.txtDashRegAdminUsername.setText("")
                            self.ui.txtDashRegAdminPassword.setText("")
                            self.ui.txtDashRegAdminEmail.setText("")
                            self.ui.txtDashRegAdminStatusCombo.setCurrentText("Active")
                            self.ui.txtDashRegAdminFlagCombo.setCurrentText("0")
                            QMessageBox.information(self, "Admin Added", "New Admin Registered Sucessfully")
                            AdminSettings.displayAdminDashTable(self,AdminSettings.getAllAdmins(self))
                        else:
                            QMessageBox.critical(self, "Failed", "Couldnot be Added")

    def personalPasswordChange(self):
        newPassword = self.ui.adminSettingsNewPass.text().lower()
        reEnterPass = self.ui.adminSettingsReenterNewPass.text().lower()
        updatedBy = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        adminID = self.ui.adminSettingsID.text()
        conn = connections.conndb()


        if (newPassword=="" or reEnterPass==""):
            QMessageBox.warning(self, "Required", "Please fill out complete details")
        else:
            if(newPassword!=reEnterPass):
                QMessageBox.critical(self, "Incorrect", "Two Password must Match")
            else:
                update_password_data = f"""UPDATE adminusers SET adminPassword='{newPassword}',changeDate='{changeDate}' WHERE adminID='{adminID}';
                    """
                if not (conn.queryExecute(update_password_data)):
                    conn.queryClose
                    QMessageBox.information(self, "Change Success", "Password Has been Change. Please Restart Application for change to take effect")
                else:
                    QMessageBox.critical(self, "Error", "Something went wrong. Please try again")




    def adminPersonalInfoUpdate(self):
        firstname = self.ui.adminSettingsFname.text().title()
        lastname = self.ui.adminSettingsLname.text().title()
        email = self.ui.adminSettingsEmail.text().lower()
        username = self.ui.adminSettingsUsername.text().lower()
        currentAdminID = self.ui.adminSettingsID.text()
        updatedBy = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        conn = connections.conndb()

        if (firstname=="" or lastname =="" or email=="" or username==""):
            QMessageBox.information(self, "Information Required", "Please fill out complete details")
        else:
            strsql = f"UPDATE adminusers SET adminFname='{firstname}',adminLname='{lastname}',adminUsername='{username}',adminEmail='{email}',updatedBy='{updatedBy}',changeDate='{changeDate}' where adminID ='{currentAdminID}'"
            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Success", "Information Updated Successfully.")
                QMessageBox.information(self, "Closing Application", "Application closing for changes being applied")
                QApplication.quit()
            else:
                QMessageBox.critical(self, "Error", "Something went wrong. Please try again")

    def sessionLogout(self):
        msg = QMessageBox()
        msg = QMessageBox.question(self, "Logout", "Are you sure you want to logout?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            QMessageBox.information(self, "Good Bye!", "Logging Off")
            QApplication.quit()
        else:
            pass

    def getAdminData(self):
        row = self.ui.adminDashTable.currentRow()
        rowAdminID = self.ui.adminDashTable.item(row,0).text()
        rowAdminFname = self.ui.adminDashTable.item(row,1).text()
        rowAdminLname = self.ui.adminDashTable.item(row,2).text()
        rowAdminUsername = self.ui.adminDashTable.item(row,3).text()
        rowAdminEmail = self.ui.adminDashTable.item(row,4).text()
        rowAdminStatus = self.ui.adminDashTable.item(row,5).text()
        rowAdminFlag = self.ui.adminDashTable.item(row,6).text()

        self.ui.txtDashAdminID.setText(rowAdminID)
        self.ui.txtDashAdminFname.setText(rowAdminFname)
        self.ui.txtDashAdminLname.setText(rowAdminLname)
        self.ui.txtDashAdminUsername.setText(rowAdminUsername)
        self.ui.txtDashAdminEmail.setText(rowAdminEmail)
        self.ui.txtDashAdminStatusCombo.setCurrentText(rowAdminStatus)
        self.ui.txtDashAdminFlagCombo.setCurrentText(rowAdminFlag)

    def getAllAdmins(self):
        conn = connections.conndb()
        get_all_admin =  """SELECT * FROM adminusers"""
        try:
            c = conn.queryResult(get_all_admin)
            return c
        except Exception as e:
            print("Couldnt get all Admin List")

    def displayAdminDashTable(self,rows):
        if rows is not None: 
            conn = connections.conndb()
            strsql = "SELECT * FROM adminusers"
            result = conn.queryResult(strsql)
            row = 0
            self.ui.adminDashTable.setRowCount(len(result))
            self.ui.adminDashTable.setSortingEnabled(True)
            for adminsList in result:
                self.ui.adminDashTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(adminsList[0])))
                self.ui.adminDashTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(adminsList[1])))
                self.ui.adminDashTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(adminsList[2])))
                self.ui.adminDashTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(adminsList[3])))
                self.ui.adminDashTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(adminsList[5])))
                self.ui.adminDashTable.setItem(row,5,QtWidgets.QTableWidgetItem(str(adminsList[6])))
                self.ui.adminDashTable.setItem(row,6,QtWidgets.QTableWidgetItem(str(adminsList[7])))
                self.ui.adminDashTable.setItem(row,7,QtWidgets.QTableWidgetItem(str(adminsList[8])))
                self.ui.adminDashTable.setItem(row,8,QtWidgets.QTableWidgetItem(str(adminsList[9])))
                row = row + 1
        else:
            print("No Data Found")
