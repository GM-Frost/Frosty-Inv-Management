import os
import sys
import connections
from Custom_Widgets.Widgets import *
from serverInventory import EquipInventoryFunctions as ei
from serverInventory import LaptopInventoryFunctions as li

from interface_ui import *
from datetime import datetime
import pandas as pd

class InuseInvFunctions():
    def __init__(self,arg):
        super(InuseInvFunctions,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
   
    def getInuseData(self):
        row = self.ui.InUseTableWidget.currentRow()
        rowItemLaptopID = self.ui.InUseTableWidget.item(row,0).text()
        rowItemUser = self.ui.InUseTableWidget.item(row,1).text()
        rowItemSerial = self.ui.InUseTableWidget.item(row,2).text()
        rowItemModel = self.ui.InUseTableWidget.item(row,3).text()
        rowItemStatus = self.ui.InUseTableWidget.item(row,5).text()

        rowItemOfficeKeyboard = self.ui.InUseTableWidget.item(row,7)
        rowItemHomeKeyboard = self.ui.InUseTableWidget.item(row,8)
        rowItemOfficeMouse = self.ui.InUseTableWidget.item(row,9)
        rowItemHomeMouse = self.ui.InUseTableWidget.item(row,10)
        rowItemOfficeHeadphone = self.ui.InUseTableWidget.item(row,11)
        rowItemHomeHeadphone = self.ui.InUseTableWidget.item(row,12)
        rowItemOfficeMonitor = self.ui.InUseTableWidget.item(row,13)
        rowItemHomeMonitor = self.ui.InUseTableWidget.item(row,14)
        rowItemOfficeDock = self.ui.InUseTableWidget.item(row,15)
        rowItemHomeDock = self.ui.InUseTableWidget.item(row,16)
        rowItemOfficeExtra = self.ui.InUseTableWidget.item(row,17).text()
        rowItemHomeExtra = self.ui.InUseTableWidget.item(row,18).text()

        #---------------------------------- KEYBOARD RADIO DEFAULT -------------------------------------------#
        if rowItemOfficeKeyboard is not None:
            rowOfficeKeyboard = rowItemOfficeKeyboard.text()
            if rowOfficeKeyboard == "✅":
                self.ui.officeKeyboardRadioStocked.setChecked(True)
            else:
                self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
                self.ui.officeKeyboardRadioStocked.setChecked(False)
                self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
        else:
            self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
            self.ui.officeKeyboardRadioStocked.setChecked(False)
            self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
        
        if rowItemHomeKeyboard is not None:
            rowHomeKeyboard = rowItemHomeKeyboard.text()
            if rowHomeKeyboard == "✅":
                self.ui.homeKeyboardRadioStocked.setChecked(True)
            else:
                self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
                self.ui.homeKeyboardRadioStocked.setChecked(False)
                self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)
        else:
            self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
            self.ui.homeKeyboardRadioStocked.setChecked(False)
            self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)
        #---------------------------------- MOUSE RADIO DEFAULT -------------------------------------------#
        if rowItemOfficeMouse is not None:
            rowOfficeMouse = rowItemOfficeMouse.text()
            if rowOfficeMouse == "✅":
                self.ui.officeMouseRadioStocked.setChecked(True)
            else:
                self.ui.officeMouseRadioStocked.setAutoExclusive(False)
                self.ui.officeMouseRadioStocked.setChecked(False)
                self.ui.officeMouseRadioStocked.setAutoExclusive(True)
        else:
            self.ui.officeMouseRadioStocked.setAutoExclusive(False)
            self.ui.officeMouseRadioStocked.setChecked(False)
            self.ui.officeMouseRadioStocked.setAutoExclusive(True)
            
        if rowItemHomeMouse is not None:
            rowHomeMouse = rowItemHomeMouse.text()
            if rowHomeMouse == "✅":
                self.ui.homeMouseRadioStocked.setChecked(True)
            else:
                self.ui.homeMouseRadioStocked.setAutoExclusive(False)
                self.ui.homeMouseRadioStocked.setChecked(False)
                self.ui.homeMouseRadioStocked.setAutoExclusive(True)
        else:
            self.ui.homeMouseRadioStocked.setAutoExclusive(False)
            self.ui.homeMouseRadioStocked.setChecked(False)
            self.ui.homeMouseRadioStocked.setAutoExclusive(True)

        #---------------------------------- HEADPHONE RADIO DEFAULT -------------------------------------------#
        if rowItemOfficeHeadphone is not None:
            rowOfficeHeadphone = rowItemOfficeHeadphone.text()
            if rowOfficeHeadphone == "✅":
                self.ui.officeHeadphoneRadioStocked.setChecked(True)
            else:
                self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
                self.ui.officeHeadphoneRadioStocked.setChecked(False)
                self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
        else:
            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
            self.ui.officeHeadphoneRadioStocked.setChecked(False)
            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
            
        if rowItemHomeHeadphone is not None:
            rowHomeHeadphone = rowItemHomeHeadphone.text()
            if rowHomeHeadphone == "✅":
                self.ui.homeHeadphoneRadioStocked.setChecked(True)
            else:
                self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
                self.ui.homeHeadphoneRadioStocked.setChecked(False)
                self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)
        else:
            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
            self.ui.homeHeadphoneRadioStocked.setChecked(False)
            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)
        
        #---------------------------------- MONITOR RADIO DEFAULT -------------------------------------------#

        if rowItemOfficeMonitor is not None:
            rowOfficeMonitor = int(rowItemOfficeMonitor.text())
            if rowOfficeMonitor > 0:
                self.ui.officeMonitorRadioStocked.setChecked(True)
                self.ui.officeEquipMonitorSpin.setValue(rowOfficeMonitor)
            else:
                self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
                self.ui.officeMonitorRadioStocked.setChecked(False)
                self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
        else:
            self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
            self.ui.officeMonitorRadioStocked.setChecked(False)
            self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
            
        if rowItemHomeMonitor is not None:
            rowHomeMonitor = int(rowItemHomeMonitor.text())
            if rowHomeMonitor > 0 :
                self.ui.homeMonitorRadioStocked.setChecked(True)
                self.ui.homeEquipMonitorSpin.setValue(rowHomeMonitor)
            else:
                self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
                self.ui.homeMonitorRadioStocked.setChecked(False)
                self.ui.homeMonitorRadioStocked.setAutoExclusive(True)
        else:
            self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
            self.ui.homeMonitorRadioStocked.setChecked(False)
            self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

        #---------------------------------- DOCK RADIO DEFAULT -------------------------------------------#

        if rowItemOfficeDock is not None:
            rowOfficeDock = rowItemOfficeDock.text()
            if rowOfficeDock == "✅":
                self.ui.officeDockRadioStocked.setChecked(True)
            else:
                self.ui.officeDockRadioStocked.setAutoExclusive(False)
                self.ui.officeDockRadioStocked.setChecked(False)
                self.ui.officeDockRadioStocked.setAutoExclusive(True)
        else:
            self.ui.officeDockRadioStocked.setAutoExclusive(False)
            self.ui.officeDockRadioStocked.setChecked(False)
            self.ui.officeDockRadioStocked.setAutoExclusive(True)
            
        if rowItemHomeDock is not None:
            rowHomeDock = rowItemHomeDock.text()
            if rowHomeDock == "✅":
                self.ui.homeDockRadioStocked.setChecked(True)
            else:
                self.ui.homeDockRadioStocked.setAutoExclusive(False)
                self.ui.homeDockRadioStocked.setChecked(False)
                self.ui.homeDockRadioStocked.setAutoExclusive(True)
        else:
            self.ui.homeDockRadioStocked.setAutoExclusive(False)
            self.ui.homeDockRadioStocked.setChecked(False)
            self.ui.homeDockRadioStocked.setAutoExclusive(True)


        self.ui.txtInuseLaptopSerial.setText(rowItemSerial)
        self.ui.txtInuseLaptopModel.setText(rowItemModel)
        self.ui.txtInuseUser.setText(rowItemUser)
        self.ui.txtInuseLaptopStatus.setText(rowItemStatus)
        self.ui.txtInuseSLNO.setText(rowItemLaptopID)
        self.ui.extraEquipOffice.setText(rowItemOfficeExtra)
        self.ui.extraEquipHome.setText(rowItemHomeExtra)
        
        if (rowItemStatus=="Sent For Repairs"):
            self.ui.sendForRepairLaptopSerial.setText("")
        else:
            self.ui.sendForRepairLaptopSerial.setText(rowItemSerial)

        self.ui.offboardingLaptopSerial.setText(rowItemSerial)
 
    
    def getAllInuseItems(self):
        conn = connections.conndb()
        get_all_data =  """SELECT * FROM inuseinventory"""
        try:
            c = conn.queryResult(get_all_data)
            return c
        except Exception as e:
            print("Couldnt get all Data")   

    def addInuseInv(self):
        conn = connections.conndb()
        msg = QMessageBox()

        laptopSerial = self.ui.txtInuseLaptopSerial.text().upper()
        laptopModel = self.ui.txtInuseLaptopModel.text().upper()
        laptopUser = self.ui.txtInuseUser.text().title()
        inUsecurrentStatus = self.ui.txtInuseLaptopStatus.text().title()
      
        officeExtraEquip = self.ui.extraEquipOffice.text().title()
        homeExtraEquip = self.ui.extraEquipHome.text().title()

        dupEntryQuery1 =  f"""SELECT * FROM inuseinventory where LaptopSerial='{laptopSerial}'"""
        dupEntry1 = conn.queryResult(dupEntryQuery1)

        dupEntryQuery2 =  f"""SELECT * FROM laptopinventory where LaptopSerial='{laptopSerial}'"""
        dupEntry2 = conn.queryResult(dupEntryQuery2)

        if dupEntry1:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop is Already Present on Records")
            return
        else:    
            if dupEntry2:
                QMessageBox.warning(self, "On Records", "Laptop Preset at Server Room and will be inserted here")

                laptopModel = dupEntry2[0][2]
            else:
                laptopModel = self.ui.txtInuseLaptopModel.text().upper()
                
            
            ##-----------------------------------KEYBOARD OFFICE VALUE----------------------------------------------##
            officeKeyboardNewDefVal=0
            officeKeyboardStockDefVal=0
            officeKeyboardValue = 0
            if (self.ui.officeKeyboardRadioNew.isChecked()):
                officeKeyboardNewDefVal=1
            elif (self.ui.officeKeyboardRadioStocked.isChecked()):
                officeKeyboardStockDefVal=1
            if (officeKeyboardNewDefVal!=0):
                officeKeyboardValue = 1
            if (officeKeyboardStockDefVal != 0):
                conn = connections.conndb()
                get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                c = conn.queryResult(get_keyboard_count)
                keyboard_count = c[0][0]
                if (keyboard_count > 0):
                    newKeyboardValue = keyboard_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                    conn.queryExecute(strsql)
                    officeKeyboardValue = 1
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Keyboard Stock Too Low")
                    return
            
            ##-----------------------------------KEYBOARD HOME VALUE----------------------------------------------##
            homeKeyboardNewDefVal=0
            homeKeyboardStockDefVal=0
            homeKeyboardValue = 0

            if (self.ui.homeKeyboardRadioNew.isChecked()):
                homeKeyboardNewDefVal=1
            elif (self.ui.homeKeyboardRadioStocked.isChecked()):
                homeKeyboardStockDefVal=1
            if (homeKeyboardNewDefVal!=0):
                homeKeyboardValue = 1
            if (homeKeyboardStockDefVal != 0):
                conn = connections.conndb()
                get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                keyboardSearch = conn.queryResult(get_keyboard_count)
                keyboard_count = keyboardSearch[0][0]
                if (keyboard_count > 0):
                    newKeyboardValue = keyboard_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                    conn.queryExecute(strsql)
                    homeKeyboardValue = 1
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Keyboard Stock Too Low")
                    return 
            
            ##-----------------------------------MOUSE OFFICE VALUE----------------------------------------------##
            officeMouseNewDefVal=0
            officeMouseStockDefVal=0
            officeMouseValue = 0
            if (self.ui.officeMouseRadioNew.isChecked()):
                officeMouseNewDefVal=1
            elif (self.ui.officeMouseRadioStocked.isChecked()):
                officeMouseStockDefVal=1
            if (officeMouseNewDefVal!=0):
                officeMouseValue = 1
            if (officeMouseStockDefVal != 0):
                conn = connections.conndb()
                get_mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                mouseSearch = conn.queryResult(get_mouse_count)
                mouse_count = mouseSearch[0][0]
                if (mouse_count > 0):
                    newMouseValue = mouse_count - 1
                    mouseOfficeSql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                    conn.queryExecute(mouseOfficeSql)
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    officeMouseValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Mouse Stock Too Low")
                    return
            
            ##-----------------------------------MOUSE HOME VALUE----------------------------------------------##
            homeMouseNewDefVal=0
            homeMouseStockDefVal=0
            homeMouseValue = 0

            if (self.ui.homeMouseRadioNew.isChecked()):
                homeMouseNewDefVal=1
            elif (self.ui.homeMouseRadioStocked.isChecked()):
                homeMouseStockDefVal=1
            if (homeMouseNewDefVal!=0):
                homeMouseValue = 1
            if (homeMouseStockDefVal != 0):
                conn = connections.conndb()
                get_Mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                c = conn.queryResult(get_Mouse_count)
                Mouse_count = c[0][0]
                
                if (Mouse_count > 0):
                    newMouseValue = Mouse_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                    conn.queryExecute(strsql)
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    homeMouseValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Mouse Stock Too Low")

                    return

            ##-----------------------------------HEADPHONE OFFICE VALUE----------------------------------------------##
            officeHeadphoneNewDefVal=0
            officeHeadphoneStockDefVal=0
            officeHeadphoneValue = 0
            if (self.ui.officeHeadphoneRadioNew.isChecked()):
                officeHeadphoneNewDefVal=1
            elif (self.ui.officeHeadphoneRadioStocked.isChecked()):
                officeHeadphoneStockDefVal=1
            if (officeHeadphoneNewDefVal!=0):
                officeHeadphoneValue = 1
            if (officeHeadphoneStockDefVal != 0):
                conn = connections.conndb()
                get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Headphones'"""
                headphoneSearch = conn.queryResult(get_Headphone_count)
                headphoneCount = headphoneSearch[0][0]
                if (headphoneCount > 0):
                    newHeadphoneValue = headphoneCount - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                    conn.queryExecute(strsql)
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    officeHeadphoneValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Headphone Stock Too Low")
                    return
            
            ##-----------------------------------HEADPHONE HOME VALUE----------------------------------------------##
            homeHeadphoneNewDefVal=0
            homeHeadphoneStockDefVal=0
            homeHeadphoneValue = 0

            if (self.ui.homeHeadphoneRadioNew.isChecked()):
                homeHeadphoneNewDefVal=1
            elif (self.ui.homeHeadphoneRadioStocked.isChecked()):
                homeHeadphoneStockDefVal=1
            if (homeHeadphoneNewDefVal!=0):
                homeHeadphoneValue = 1
            if (homeHeadphoneStockDefVal != 0):
                conn = connections.conndb()
                get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Headphones'"""
                c = conn.queryResult(get_Headphone_count)
                Headphone_count = c[0][0]
                if (Headphone_count > 0):
                    newHeadphoneValue = Headphone_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                    conn.queryExecute(strsql)
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    homeHeadphoneValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Headphone Stock Too Low")
                    return 

                ##-----------------------------------MONITOR OFFICE VALUE----------------------------------------------##
            officeMonitorNewDefVal=0
            officeMonitorStockDefVal=0
            officeMonitorValue = 0

            if (self.ui.officeEquipMonitorSpin.value() > 0):
                if not ((self.ui.officeMonitorRadioNew.isChecked()) or (self.ui.officeMonitorRadioStocked.isChecked())):
                    QMessageBox.information(self, "Required", "Please Specify Monitor Provided New/Stocked")
                    return 
                else:
                    if (self.ui.officeMonitorRadioNew.isChecked()):
                        officeMonitorNewDefVal=self.ui.officeEquipMonitorSpin.text()
                    elif (self.ui.officeMonitorRadioStocked.isChecked()):
                        officeMonitorStockDefVal=self.ui.officeEquipMonitorSpin.text()
                    if (officeMonitorNewDefVal!=0):
                        officeMonitorValue = self.ui.officeEquipMonitorSpin.text()
                    if (officeMonitorStockDefVal != 0):
                        conn = connections.conndb()
                        get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                        monitorSearch = conn.queryResult(get_Monitor_count)
                        monitor_count = monitorSearch[0][0]
                        newMonitorValue = monitor_count - (self.ui.officeEquipMonitorSpin.value())
                        if (newMonitorValue >= 0):
                            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                            conn.queryExecute(strsql)
                            ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                            officeMonitorValue = self.ui.officeEquipMonitorSpin.text()
                        else:
                            QMessageBox.warning(self, "Status", "Sorry! Monitor Stock Too Low")
                            return
            
            ##-----------------------------------MONITOR HOME VALUE----------------------------------------------##
            homeMonitorNewDefVal=0
            homeMonitorStockDefVal=0
            homeMonitorValue = 0

            if (self.ui.homeEquipMonitorSpin.value() > 0):
                if not ((self.ui.homeMonitorRadioNew.isChecked()) or (self.ui.homeMonitorRadioStocked.isChecked())):
                    QMessageBox.information(self, "Selection Required", "Please Specify Monitor Provided New/Stocked")
                    return 
                else:
                    if self.ui.homeMonitorRadioNew.isChecked():
                        homeMonitorNewDefVal=self.ui.homeEquipMonitorSpin.text()
                    elif self.ui.homeMonitorRadioStocked.isChecked():
                        homeMonitorStockDefVal=self.ui.homeEquipMonitorSpin.text()
                    if homeMonitorNewDefVal!=0:
                        homeMonitorValue = self.ui.homeEquipMonitorSpin.text()
                    if homeMonitorStockDefVal != 0:
                        conn = connections.conndb()
                        get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                        c = conn.queryResult(get_Monitor_count)
                        Monitor_count = c[0][0]
                        newMonitorValue = Monitor_count - (self.ui.homeEquipMonitorSpin.value())
                        if (newMonitorValue >= 0):
                            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                            conn.queryExecute(strsql)
                            
                            ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                            homeMonitorValue = self.ui.homeEquipMonitorSpin.text()
                        else:
                            QMessageBox.warning(self, "Status", "Sorry! Monitor Stock Too Low")
                            return 

                ##-----------------------------------DOCK OFFICE VALUE----------------------------------------------##
            officeDockNewDefVal=0
            officeDockStockDefVal=0
            officeDockValue = 0
            if self.ui.officeDockRadioNew.isChecked():
                officeDockNewDefVal=1
            elif self.ui.officeDockRadioStocked.isChecked():
                officeDockStockDefVal=1
            if officeDockNewDefVal!=0:
                officeDockValue = 1
            if officeDockStockDefVal != 0:
                conn = connections.conndb()
                get_Dock_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                dockSearch = conn.queryResult(get_Dock_count)
                dock_count = dockSearch[0][0]
                
                if (dock_count > 0):
                    newDockValue = dock_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                    conn.queryExecute(strsql)
                    
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    officeDockValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Dock Stock Too Low")
                    return
            
            ##-----------------------------------DOCK HOME VALUE----------------------------------------------##
            homeDockNewDefVal= 0
            homeDockStockDefVal=0
            homeDockValue = 0

            if self.ui.homeDockRadioNew.isChecked():
                homeDockNewDefVal=1
            elif self.ui.homeDockRadioStocked.isChecked():
                homeDockStockDefVal=1
            if homeDockNewDefVal!=0:
                homeDockValue = 1
            if homeDockStockDefVal != 0:
                conn = connections.conndb()
                get_Dock_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                c = conn.queryResult(get_Dock_count)
                Dock_count = c[0][0]
                
                if (Dock_count > 0):
                    newDockValue = Dock_count - 1
                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                    conn.queryExecute(strsql)
                    
                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    homeDockValue = 1
                else:
                    QMessageBox.warning(self, "Status", "Sorry! Dock Stock Too Low")
                    return 

            updatedBy = self.ui.sessionUser.text()
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            changeDate = dt_string
            currentDate = changeDate

            insert_inuseInv_data = f"""
            INSERT INTO inuseinventory (users,LaptopSerial,ModelNumber,CurrentStatus,officeKeyboard,homeKeyboard,officeMouse,homeMouse,officeHeadphone,homeHeadphone,officeMonitor,homeMonitor,officeDock,homeDock,officeExtra,homeExtra,UpdatedBy,ChangeDate) VALUES 
            ('{laptopUser}','{laptopSerial}','{laptopModel}','{inUsecurrentStatus}','{officeKeyboardValue}','{homeKeyboardValue}','{officeMouseValue}','{homeMouseValue}','{officeHeadphoneValue}','{homeHeadphoneValue}','{officeMonitorValue}','{homeMonitorValue}','{officeDockValue}','{homeDockValue}','{officeExtraEquip}','{homeExtraEquip}','{updatedBy}','{currentDate}');
            """
            conn = connections.conndb()
            if (laptopSerial=="")or(laptopModel=="")or(laptopUser==""):
                QMessageBox.information(self, "Failed", "Please Fill the Required Fields")
            else:
                if not (conn.queryExecute(insert_inuseInv_data)):
                    delete_laptop_from_server = f"DELETE FROM laptopinventory WHERE LaptopSerial='{laptopSerial}'"
                    if not (conn.queryExecute(delete_laptop_from_server)):
                        
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        self.ui.txtInuseLaptopSerial.setText("")
                        self.ui.txtInuseSLNO.setText("")
                        self.ui.txtInuseLaptopModel.setText("")
                        self.ui.txtInuseUser.setText("")
                        self.ui.txtInuseLaptopStatus.setText("")
                        self.ui.officeEquipMonitorSpin.setValue(0)
                        self.ui.homeEquipMonitorSpin.setValue(0)
                        self.ui.extraEquipOffice.setText("")
                        self.ui.extraEquipHome.setText("")

                        self.ui.offboardingLaptopSerial.setText("")
                        self.ui.sendForRepairLaptopSerial.setText("")
                        self.ui.spareCombo.setCurrentText("")

                        self.ui.officeKeyboardRadioNew.setAutoExclusive(False)
                        self.ui.officeKeyboardRadioNew.setChecked(False)
                        self.ui.officeKeyboardRadioNew.setAutoExclusive(True)
                        self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
                        self.ui.officeKeyboardRadioStocked.setChecked(False)
                        self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
                        self.ui.homeKeyboardRadioNew.setAutoExclusive(False)
                        self.ui.homeKeyboardRadioNew.setChecked(False)
                        self.ui.homeKeyboardRadioNew.setAutoExclusive(True)
                        self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
                        self.ui.homeKeyboardRadioStocked.setChecked(False)
                        self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)

                        self.ui.officeMouseRadioNew.setAutoExclusive(False)
                        self.ui.officeMouseRadioNew.setChecked(False)
                        self.ui.officeMouseRadioNew.setAutoExclusive(True)
                        self.ui.officeMouseRadioStocked.setAutoExclusive(False)
                        self.ui.officeMouseRadioStocked.setChecked(False)
                        self.ui.officeMouseRadioStocked.setAutoExclusive(True)
                        self.ui.homeMouseRadioNew.setAutoExclusive(False)
                        self.ui.homeMouseRadioNew.setChecked(False)
                        self.ui.homeMouseRadioNew.setAutoExclusive(True)
                        self.ui.homeMouseRadioStocked.setAutoExclusive(False)
                        self.ui.homeMouseRadioStocked.setChecked(False)
                        self.ui.homeMouseRadioStocked.setAutoExclusive(True)

                        self.ui.officeHeadphoneRadioNew.setAutoExclusive(False)
                        self.ui.officeHeadphoneRadioNew.setChecked(False)
                        self.ui.officeHeadphoneRadioNew.setAutoExclusive(True)
                        self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
                        self.ui.officeHeadphoneRadioStocked.setChecked(False)
                        self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
                        self.ui.homeHeadphoneRadioNew.setAutoExclusive(False)
                        self.ui.homeHeadphoneRadioNew.setChecked(False)
                        self.ui.homeHeadphoneRadioNew.setAutoExclusive(True)
                        self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
                        self.ui.homeHeadphoneRadioStocked.setChecked(False)
                        self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)

                        self.ui.officeMonitorRadioNew.setAutoExclusive(False)
                        self.ui.officeMonitorRadioNew.setChecked(False)
                        self.ui.officeMonitorRadioNew.setAutoExclusive(True)
                        self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
                        self.ui.officeMonitorRadioStocked.setChecked(False)
                        self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
                        self.ui.homeMonitorRadioNew.setAutoExclusive(False)
                        self.ui.homeMonitorRadioNew.setChecked(False)
                        self.ui.homeMonitorRadioNew.setAutoExclusive(True)
                        self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
                        self.ui.homeMonitorRadioStocked.setChecked(False)
                        self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

                        self.ui.officeDockRadioNew.setAutoExclusive(False)
                        self.ui.officeDockRadioNew.setChecked(False)
                        self.ui.officeDockRadioNew.setAutoExclusive(True)
                        self.ui.officeDockRadioStocked.setAutoExclusive(False)
                        self.ui.officeDockRadioStocked.setChecked(False)
                        self.ui.officeDockRadioStocked.setAutoExclusive(True)
                        self.ui.homeDockRadioNew.setAutoExclusive(False)
                        self.ui.homeDockRadioNew.setChecked(False)
                        self.ui.homeDockRadioNew.setAutoExclusive(True)
                        self.ui.homeDockRadioStocked.setAutoExclusive(False)
                        self.ui.homeDockRadioStocked.setChecked(False)
                        self.ui.homeDockRadioStocked.setAutoExclusive(True)


                        li.displayLaptopTable(self,li.getAllLaptops(self))
                        InuseInvFunctions.displayInuseTable(self,InuseInvFunctions.getAllInuseItems(self))
                        # self.ui.notificationBtn.click()
                        # self.ui.notificationMsg.setText("Record Added !!!")
                        QMessageBox.information(self, "Success", "Record Added")
                        conn.queryClose
                    else:
                        QMessageBox.warning(self, "Failed", "Sorry! Couldnt Add to Records. Please Try again")
                      

    def updateInuse(self):
        conn = connections.conndb()
        msg = QMessageBox()
        laptopID = self.ui.txtInuseSLNO.text()
        laptopSerial = self.ui.txtInuseLaptopSerial.text().upper()
        laptopModel = self.ui.txtInuseLaptopModel.text().upper()
        laptopUser = self.ui.txtInuseUser.text().title()
        inUsecurrentStatus = self.ui.txtInuseLaptopStatus.text().title()
        officeExtraEquip = self.ui.extraEquipOffice.text().title()
        homeExtraEquip = self.ui.extraEquipHome.text().title()
        updatedBy = self.ui.sessionUser.text()
        currentRow = self.ui.InUseTableWidget.currentRow()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        
        dupEntryQuery1=  f"""SELECT * FROM laptopinventory where LaptopSerial='{laptopSerial}'"""
        dupEntry1 = conn.queryResult(dupEntryQuery1)
        
        if (laptopID==""):
            QMessageBox.warning(self, "Required", "Please select the item to be updated")
        elif (laptopSerial=="" or laptopModel=="" or laptopUser=="" or inUsecurrentStatus==""):
            QMessageBox.information(self, "Required", "Please Enter all Required Fields")
        elif dupEntry1:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop is Currently Present at Server Room.\nCannot be Updated")
        elif currentRow=="":
            QMessageBox.warning(self, "Required", "Please Select the Item to be Updated")
        else:

            get_Count = f"""SELECT * FROM inuseinventory WHERE SerialNumber ='{laptopID}'"""
            c = conn.queryResult(get_Count)
            normalcheck = c[0][5]
            keyboard_Office_Count = c[0][6]
            keyboard_Home_count=c[0][7]
            mouse_Office_Count = c[0][8]
            mouse_Home_Count = c[0][9]
            headphone_Office_Count = c[0][10]
            headphone_Home_Count = c[0][11]
            monitor_Office_Count = c[0][12]
            monitor_Home_Count = c[0][13]
            dock_Office_Count = c[0][14]
            dock_Home_Count = c[0][15]
         

            ##-----------------------------------KEYBOARD OFFICE VALUE----------------------------------------------##
            
            if keyboard_Office_Count=="0":
                if (self.ui.officeKeyboardRadioStocked.isChecked()):
                    officeKeyboardValue=1
                    conn = connections.conndb()
                    get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                    c = conn.queryResult(get_keyboard_count)
                    keyboard_count = c[0][0]
                    if (keyboard_count > 0):
                        newKeyboardValue = keyboard_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                        conn.queryExecute(strsql)
                        officeKeyboardValue = 1
                        strsql2 = f"UPDATE inuseinventory SET officeKeyboard='{officeKeyboardValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Keyboard Stock Too Low")
                     
                        return "lowStock"
            ##-----------------------------------KEYBOARD HOME VALUE----------------------------------------------##
            
            if keyboard_Home_count =="0":
                if self.ui.homeKeyboardRadioStocked.isChecked():
                    homeKeyboardValue = 1
                    conn = connections.conndb()
                    get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                    keyboardSearch = conn.queryResult(get_keyboard_count)
                    keyboard_count = keyboardSearch[0][0]
                    if (keyboard_count > 0):
                        newKeyboardValue = keyboard_count - 1
                        
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                        conn.queryExecute(strsql)
                        homeKeyboardValue = 1
                        strsql2 = f"UPDATE inuseinventory SET homeKeyboard='{homeKeyboardValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Keyboard Stock Too Low")
                        return 
            ##-----------------------------------MOUSE OFFICE VALUE----------------------------------------------##
            
            if mouse_Office_Count == "0":
                if self.ui.officeMouseRadioStocked.isChecked():
                    officeMouseValue = 1
                    conn = connections.conndb()
                    get_mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                    mouseSearch = conn.queryResult(get_mouse_count)
                    mouse_count = mouseSearch[0][0]
                    if (mouse_count > 0):
                        newMouseValue = mouse_count - 1
                        mouseOfficeSql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                        conn.queryExecute(mouseOfficeSql)
                        officeMouseValue = 1
                        strsql2 = f"UPDATE inuseinventory SET officeMouse='{officeMouseValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Mouse Stock Too Low")
                        return    
             ##-----------------------------------MOUSE HOME VALUE----------------------------------------------##
          
            
            if mouse_Home_Count == "0":
                if self.ui.homeMouseRadioStocked.isChecked():
                    homeMouseValue = 1
                    conn = connections.conndb()
                    get_Mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                    c = conn.queryResult(get_Mouse_count)
                    Mouse_count = c[0][0]
                    
                    if (Mouse_count > 0):
                        newMouseValue = Mouse_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                        conn.queryExecute(strsql)
                        homeMouseValue = 1
                        strsql2 = f"UPDATE inuseinventory SET homeMouse='{homeMouseValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Mouse Stock Too Low")
                        return
            ##-----------------------------------HEADPHONE OFFICE VALUE----------------------------------------------##
            
            if headphone_Office_Count =="0":
                if self.ui.officeHeadphoneRadioStocked.isChecked():
                    conn = connections.conndb()
                    get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Headphones'"""
                    headphoneSearch = conn.queryResult(get_Headphone_count)
                    headphone_count = headphoneSearch[0][0]
                    if (headphone_count > 0):
                        newHeadphoneValue = headphone_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                        conn.queryExecute(strsql)
                        officeHeadphoneValue = 1
                        strsql2 = f"UPDATE inuseinventory SET officeHeadphone='{officeHeadphoneValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Headphone Stock Too Low")
                        return
            
            ##-----------------------------------HEADPHONE HOME VALUE----------------------------------------------##
            if headphone_Home_Count == "0":
                if self.ui.homeHeadphoneRadioStocked.isChecked():
                    conn = connections.conndb()
                    get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Headphones'"""
                    c = conn.queryResult(get_Headphone_count)
                    Headphone_count = c[0][0]
                    if (Headphone_count > 0):
                        newHeadphoneValue = Headphone_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                        conn.queryExecute(strsql)
                        homeHeadphoneValue = 1
                        strsql2 = f"UPDATE inuseinventory SET homeHeadphone='{homeHeadphoneValue}' WHERE SerialNumber ='{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Headphone Stock Too Low")
                        return         

            ##-----------------------------------MONITOR OFFICE VALUE----------------------------------------------##
            if int(monitor_Office_Count)<self.ui.officeEquipMonitorSpin.value():
                if (self.ui.officeEquipMonitorSpin.value() > 0):
                    if (self.ui.officeMonitorRadioStocked.isChecked()):
                        officeMonitorValue = self.ui.officeEquipMonitorSpin.text()
                        conn = connections.conndb()
                        get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                        monitorSearch = conn.queryResult(get_Monitor_count)
                        monitor_count = monitorSearch[0][0]
                        newMonitorValue = monitor_count - (self.ui.officeEquipMonitorSpin.value())
                        if (newMonitorValue >= 0):
                            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                            conn.queryExecute(strsql)
                            officeMonitorValue = self.ui.officeEquipMonitorSpin.text()
                            strsql2 = f"UPDATE inuseinventory SET officeMonitor='{officeMonitorValue}' WHERE SerialNumber = '{laptopID}'"
                            conn.queryExecute(strsql2)
                            ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                            
                        else:
                            QMessageBox.warning(self, "Status", "Sorry! Monitor Stock Too Low")
                            return
            
            ##-----------------------------------MONITOR HOME VALUE----------------------------------------------##
            if int(monitor_Home_Count)<self.ui.homeEquipMonitorSpin.value():
                if (self.ui.homeEquipMonitorSpin.value() > 0):
                    if self.ui.homeMonitorRadioStocked.isChecked():
                        conn = connections.conndb()
                        get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                        c = conn.queryResult(get_Monitor_count)
                        Monitor_count = c[0][0]
                        newMonitorValue = Monitor_count - (self.ui.homeEquipMonitorSpin.value())
                        if (newMonitorValue >= 0):
                            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                            conn.queryExecute(strsql)
                            homeMonitorValue = self.ui.homeEquipMonitorSpin.text()
                            strsql2 = f"UPDATE inuseinventory SET homeMonitor='{homeMonitorValue}' WHERE SerialNumber = '{laptopID}'"
                            conn.queryExecute(strsql2)
                            ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                        else:
                            QMessageBox.warning(self, "Status", "Sorry! Monitor Stock Too Low")
                            return 

            ##-----------------------------------DOCK OFFICE VALUE----------------------------------------------##
            if dock_Office_Count== "0":
                if self.ui.officeDockRadioStocked.isChecked():
                    conn = connections.conndb()
                    get_Dock_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                    dockSearch = conn.queryResult(get_Dock_count)
                    dock_count = dockSearch[0][0]
                    if (dock_count > 0):
                        newDockValue = dock_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                        conn.queryExecute(strsql)
                        officeDockValue = 1
                        strsql2 = f"UPDATE inuseinventory SET officeDock='{officeDockValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Dock Stock Too Low")
                        return
            
            ##-----------------------------------DOCK HOME VALUE----------------------------------------------##
            if dock_Home_Count== "0":
                if self.ui.homeDockRadioStocked.isChecked():
                    conn = connections.conndb()
                    get_Dock_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                    c = conn.queryResult(get_Dock_count)
                    Dock_count = c[0][0]
                    
                    if (Dock_count > 0):
                        newDockValue = Dock_count - 1
                        strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                        conn.queryExecute(strsql)
                        homeDockValue = 1
                        strsql2 = f"UPDATE inuseinventory SET homeDock='{homeDockValue}' WHERE SerialNumber = '{laptopID}'"
                        conn.queryExecute(strsql2)
                        ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                    else:
                        QMessageBox.warning(self, "Status", "Sorry! Dock Stock Too Low")
                        return 

            strsql = f"UPDATE inuseinventory SET users='{laptopUser}', LaptopSerial='{laptopSerial}', ModelNumber='{laptopModel}',CurrentStatus='{inUsecurrentStatus}',officeExtra='{officeExtraEquip}',homeExtra='{homeExtraEquip}',UpdatedBy='{updatedBy}',ChangeDate='{changeDate}' WHERE SerialNumber='{laptopID}'"
            if not (conn.queryExecute(strsql)):

                self.ui.txtInuseLaptopSerial.setText("")
                self.ui.txtInuseSLNO.setText("")
                self.ui.txtInuseLaptopModel.setText("")
                self.ui.txtInuseUser.setText("")
                self.ui.txtInuseLaptopStatus.setText("")
                self.ui.officeEquipMonitorSpin.setValue(0)
                self.ui.homeEquipMonitorSpin.setValue(0)
                self.ui.extraEquipOffice.setText("")
                self.ui.extraEquipHome.setText("")

                self.ui.offboardingLaptopSerial.setText("")
                self.ui.sendForRepairLaptopSerial.setText("")
                self.ui.spareCombo.setCurrentText("")

                self.ui.officeKeyboardRadioNew.setAutoExclusive(False)
                self.ui.officeKeyboardRadioNew.setChecked(False)
                self.ui.officeKeyboardRadioNew.setAutoExclusive(True)
                self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
                self.ui.officeKeyboardRadioStocked.setChecked(False)
                self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
                self.ui.homeKeyboardRadioNew.setAutoExclusive(False)
                self.ui.homeKeyboardRadioNew.setChecked(False)
                self.ui.homeKeyboardRadioNew.setAutoExclusive(True)
                self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
                self.ui.homeKeyboardRadioStocked.setChecked(False)
                self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)

                self.ui.officeMouseRadioNew.setAutoExclusive(False)
                self.ui.officeMouseRadioNew.setChecked(False)
                self.ui.officeMouseRadioNew.setAutoExclusive(True)
                self.ui.officeMouseRadioStocked.setAutoExclusive(False)
                self.ui.officeMouseRadioStocked.setChecked(False)
                self.ui.officeMouseRadioStocked.setAutoExclusive(True)
                self.ui.homeMouseRadioNew.setAutoExclusive(False)
                self.ui.homeMouseRadioNew.setChecked(False)
                self.ui.homeMouseRadioNew.setAutoExclusive(True)
                self.ui.homeMouseRadioStocked.setAutoExclusive(False)
                self.ui.homeMouseRadioStocked.setChecked(False)
                self.ui.homeMouseRadioStocked.setAutoExclusive(True)

                self.ui.officeHeadphoneRadioNew.setAutoExclusive(False)
                self.ui.officeHeadphoneRadioNew.setChecked(False)
                self.ui.officeHeadphoneRadioNew.setAutoExclusive(True)
                self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
                self.ui.officeHeadphoneRadioStocked.setChecked(False)
                self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
                self.ui.homeHeadphoneRadioNew.setAutoExclusive(False)
                self.ui.homeHeadphoneRadioNew.setChecked(False)
                self.ui.homeHeadphoneRadioNew.setAutoExclusive(True)
                self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
                self.ui.homeHeadphoneRadioStocked.setChecked(False)
                self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)

                self.ui.officeMonitorRadioNew.setAutoExclusive(False)
                self.ui.officeMonitorRadioNew.setChecked(False)
                self.ui.officeMonitorRadioNew.setAutoExclusive(True)
                self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
                self.ui.officeMonitorRadioStocked.setChecked(False)
                self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
                self.ui.homeMonitorRadioNew.setAutoExclusive(False)
                self.ui.homeMonitorRadioNew.setChecked(False)
                self.ui.homeMonitorRadioNew.setAutoExclusive(True)
                self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
                self.ui.homeMonitorRadioStocked.setChecked(False)
                self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

                self.ui.officeDockRadioNew.setAutoExclusive(False)
                self.ui.officeDockRadioNew.setChecked(False)
                self.ui.officeDockRadioNew.setAutoExclusive(True)
                self.ui.officeDockRadioStocked.setAutoExclusive(False)
                self.ui.officeDockRadioStocked.setChecked(False)
                self.ui.officeDockRadioStocked.setAutoExclusive(True)
                self.ui.homeDockRadioNew.setAutoExclusive(False)
                self.ui.homeDockRadioNew.setChecked(False)
                self.ui.homeDockRadioNew.setAutoExclusive(True)
                self.ui.homeDockRadioStocked.setAutoExclusive(False)
                self.ui.homeDockRadioStocked.setChecked(False)
                self.ui.homeDockRadioStocked.setAutoExclusive(True)

                li.displayLaptopTable(self,li.getAllLaptops(self))
                InuseInvFunctions.displayInuseTable(self,InuseInvFunctions.getAllInuseItems(self))
                
                # self.ui.notificationBtn.click()
                # self.ui.notificationMsg.setText("Record Added !!!")
                QMessageBox.warning(self, "Success", "Record has been Updated")
                conn.queryClose

    def load_spare_laptops(self):
        conn = connections.conndb()
        # Select LaptopSerial and LaptopModel from Laptopinventory where LaptopStatus='Spare'
        query = """SELECT LaptopSerial, LaptopModel FROM laptopinventory WHERE LaptopStatus = 'Spare'"""
        result = conn.queryResult(query)
        # Add the spare laptops to the QComboBox
        self.ui.spareCombo.clear()
        for row in result:
            serial, model = row
            item_text = f"{serial}"
            self.ui.spareCombo.addItem(item_text)

    def offboardingRequest(self):
        msg = QMessageBox()
        conn = connections.conndb()
        laptopSerial = self.ui.offboardingLaptopSerial.text().upper()

        if laptopSerial == "":
            QMessageBox.warning(self, "Required", "Please Select Laptop Serial")
        else:
            msg = QMessageBox.question(self, "Offboarding", "Are you sure you want to Offboard this user?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                    row = self.ui.InUseTableWidget.currentRow()
                    laptopID = self.ui.InUseTableWidget.item(row,0).text()
                    laptopSerial = self.ui.InUseTableWidget.item(row,2).text().upper()
                    laptopModel = self.ui.InUseTableWidget.item(row,3).text().upper()
                    lastUser = self.ui.InUseTableWidget.item(row,1).text().title()
                    status = "Returned"
                    updatedBy = self.ui.sessionUser.text()
                    now = datetime.now()
                    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                    changeDate = dt_string


                    insert_serverroom_data = f"""
                    INSERT INTO laptopinventory (LaptopSerial,LaptopModel,LastUser,LaptopStatus,UpdatedBy,ChangeDate) VALUES 
                    ('{laptopSerial}','{laptopModel}','{lastUser}','{status}','{updatedBy}','{changeDate}');
                    """
                    delete_inv_record = f"""
                        DELETE FROM inuseinventory WHERE LaptopSerial='{laptopSerial}'
                    """
                    if not (conn.queryExecute(insert_serverroom_data)):
                        if not (conn.queryExecute(delete_inv_record)):
                            ##-----------------------------------KEYBOARD OFFICE VALUE----------------------------------------------##

                            if (self.ui.officeKeyboardRadioStocked.isChecked()):
                                conn = connections.conndb()
                                get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                                c = conn.queryResult(get_keyboard_count)
                                keyboard_count = c[0][0]
                                newKeyboardValue = keyboard_count + 1
                                strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                                conn.queryExecute(strsql)
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                                
                            ##-----------------------------------KEYBOARD HOME VALUE----------------------------------------------##
                            
                        
                            if self.ui.homeKeyboardRadioStocked.isChecked():
                                conn = connections.conndb()
                                get_keyboard_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Keyboard'"""
                                keyboardSearch = conn.queryResult(get_keyboard_count)
                                keyboard_count = keyboardSearch[0][0]
                                newKeyboardValue = keyboard_count + 1
                                
                                strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newKeyboardValue}' where equipItems ='Keyboard'"
                                conn.queryExecute(strsql)
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                            
                        ##-----------------------------------MOUSE OFFICE VALUE----------------------------------------------##
                    
                        
                            if self.ui.officeMouseRadioStocked.isChecked():
                                conn = connections.conndb()
                                get_mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                                mouseSearch = conn.queryResult(get_mouse_count)
                                mouse_count = mouseSearch[0][0]
                                newMouseValue = mouse_count + 1
                                mouseOfficeSql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                                conn.queryExecute(mouseOfficeSql)
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                                
                            ##-----------------------------------MOUSE HOME VALUE----------------------------------------------##
                            
                        
                            if self.ui.homeMouseRadioStocked.isChecked():
                                conn = connections.conndb()
                                get_Mouse_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Mouse'"""
                                c = conn.queryResult(get_Mouse_count)
                                Mouse_count = c[0][0]
                                newMouseValue = Mouse_count + 1
                                strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMouseValue}' where equipItems ='Mouse'"
                                conn.queryExecute(strsql)
                                
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                            
                            ##-----------------------------------HEADPHONE OFFICE VALUE----------------------------------------------##
                                    
                            if self.ui.officeHeadphoneRadioStocked.isChecked():
                                conn = connections.conndb()
                                get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems = 'Headphones'"""
                                headphoneSearch = conn.queryResult(get_Headphone_count)
                                headphone_count = headphoneSearch[0][0]
                                newHeadphoneValue = headphone_count + 1
                                strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                                conn.queryExecute(strsql)
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))

                            ##-----------------------------------HEADPHONE HOME VALUE----------------------------------------------##
                    
                            if self.ui.homeHeadphoneRadioStocked.isChecked():
                                conn = connections.conndb()
                                get_Headphone_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Headphones'"""
                                c = conn.queryResult(get_Headphone_count)
                                Headphone_count = c[0][0]
                                newHeadphoneValue = Headphone_count + 1
                                strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newHeadphoneValue}' where equipItems ='Headphones'"
                                conn.queryExecute(strsql)
                                
                                ei.displayEquipmentsTable(self,ei.getAllEquipments(self))

                            ##-----------------------------------MONITOR OFFICE VALUE----------------------------------------------##
                            if (self.ui.officeEquipMonitorSpin.value() > 0):
                                if (self.ui.officeMonitorRadioStocked.isChecked()):
                                    conn = connections.conndb()
                                    get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                                    monitorSearch = conn.queryResult(get_Monitor_count)
                                    monitor_count = monitorSearch[0][0]
                                    newMonitorValue = monitor_count + (self.ui.officeEquipMonitorSpin.value())
                                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                                    conn.queryExecute(strsql)
                                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                                    
                        
                    ##-----------------------------------MONITOR HOME VALUE----------------------------------------------##
                            if (self.ui.homeEquipMonitorSpin.value() > 0):
                                if self.ui.homeMonitorRadioStocked.isChecked():
                                    conn = connections.conndb()
                                    get_Monitor_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Monitors'"""
                                    c = conn.queryResult(get_Monitor_count)
                                    Monitor_count = c[0][0]
                                    newMonitorValue = Monitor_count + (self.ui.homeEquipMonitorSpin.value())
                                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newMonitorValue}' where equipItems ='Monitors'"
                                    conn.queryExecute(strsql)
                                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                                
                            ##-----------------------------------DOCK OFFICE VALUE----------------------------------------------##
                                    
                                if self.ui.officeDockRadioStocked.isChecked():
                                    conn = connections.conndb()
                                    get_Dock_count = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                                    dockSearch = conn.queryResult(get_Dock_count)
                                    dock_count = dockSearch[0][0]
                                    newDockValue = dock_count + 1
                                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                                    conn.queryExecute(strsql)
                                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))
                                
                            
                            ##-----------------------------------DOCK HOME VALUE----------------------------------------------##
                            
                                if self.ui.homeDockRadioStocked.isChecked():
                                    conn = connections.conndb()
                                    get_Dock_count2 = """SELECT equipItemCount FROM equipmentsrecord WHERE equipItems ='Docks'"""
                                    dockSearch2 = conn.queryResult(get_Dock_count2)
                                    Dock_count = dockSearch2[0][0]
                                    newDockValue = Dock_count + 1
                                    strsql = f"UPDATE equipmentsrecord SET equipItemCount='{newDockValue}' where equipItems ='Docks'"
                                    conn.queryExecute(strsql)
                                    ei.displayEquipmentsTable(self,ei.getAllEquipments(self))


                            InuseInvFunctions.displayInuseTable(self,InuseInvFunctions.getAllInuseItems(self))
                            li.displayLaptopTable(self,li.getAllLaptops(self))
                            QMessageBox.information(self, "Offboarding Complete", "User has been Offboarded.")

                            self.ui.txtInuseLaptopSerial.setText("")
                            self.ui.txtInuseSLNO.setText("")
                            self.ui.txtInuseLaptopModel.setText("")
                            self.ui.txtInuseUser.setText("")
                            self.ui.txtInuseLaptopStatus.setText("")
                            self.ui.officeEquipMonitorSpin.setValue(0)
                            self.ui.homeEquipMonitorSpin.setValue(0)
                            self.ui.extraEquipOffice.setText("")
                            self.ui.extraEquipHome.setText("")

                            self.ui.offboardingLaptopSerial.setText("")
                            self.ui.sendForRepairLaptopSerial.setText("")
                            self.ui.spareCombo.setCurrentText("")

                            self.ui.officeKeyboardRadioNew.setAutoExclusive(False)
                            self.ui.officeKeyboardRadioNew.setChecked(False)
                            self.ui.officeKeyboardRadioNew.setAutoExclusive(True)
                            self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
                            self.ui.officeKeyboardRadioStocked.setChecked(False)
                            self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
                            self.ui.homeKeyboardRadioNew.setAutoExclusive(False)
                            self.ui.homeKeyboardRadioNew.setChecked(False)
                            self.ui.homeKeyboardRadioNew.setAutoExclusive(True)
                            self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
                            self.ui.homeKeyboardRadioStocked.setChecked(False)
                            self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)

                            self.ui.officeMouseRadioNew.setAutoExclusive(False)
                            self.ui.officeMouseRadioNew.setChecked(False)
                            self.ui.officeMouseRadioNew.setAutoExclusive(True)
                            self.ui.officeMouseRadioStocked.setAutoExclusive(False)
                            self.ui.officeMouseRadioStocked.setChecked(False)
                            self.ui.officeMouseRadioStocked.setAutoExclusive(True)
                            self.ui.homeMouseRadioNew.setAutoExclusive(False)
                            self.ui.homeMouseRadioNew.setChecked(False)
                            self.ui.homeMouseRadioNew.setAutoExclusive(True)
                            self.ui.homeMouseRadioStocked.setAutoExclusive(False)
                            self.ui.homeMouseRadioStocked.setChecked(False)
                            self.ui.homeMouseRadioStocked.setAutoExclusive(True)

                            self.ui.officeHeadphoneRadioNew.setAutoExclusive(False)
                            self.ui.officeHeadphoneRadioNew.setChecked(False)
                            self.ui.officeHeadphoneRadioNew.setAutoExclusive(True)
                            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
                            self.ui.officeHeadphoneRadioStocked.setChecked(False)
                            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
                            self.ui.homeHeadphoneRadioNew.setAutoExclusive(False)
                            self.ui.homeHeadphoneRadioNew.setChecked(False)
                            self.ui.homeHeadphoneRadioNew.setAutoExclusive(True)
                            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
                            self.ui.homeHeadphoneRadioStocked.setChecked(False)
                            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)

                            self.ui.officeMonitorRadioNew.setAutoExclusive(False)
                            self.ui.officeMonitorRadioNew.setChecked(False)
                            self.ui.officeMonitorRadioNew.setAutoExclusive(True)
                            self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
                            self.ui.officeMonitorRadioStocked.setChecked(False)
                            self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
                            self.ui.homeMonitorRadioNew.setAutoExclusive(False)
                            self.ui.homeMonitorRadioNew.setChecked(False)
                            self.ui.homeMonitorRadioNew.setAutoExclusive(True)
                            self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
                            self.ui.homeMonitorRadioStocked.setChecked(False)
                            self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

                            self.ui.officeDockRadioNew.setAutoExclusive(False)
                            self.ui.officeDockRadioNew.setChecked(False)
                            self.ui.officeDockRadioNew.setAutoExclusive(True)
                            self.ui.officeDockRadioStocked.setAutoExclusive(False)
                            self.ui.officeDockRadioStocked.setChecked(False)
                            self.ui.officeDockRadioStocked.setAutoExclusive(True)
                            self.ui.homeDockRadioNew.setAutoExclusive(False)
                            self.ui.homeDockRadioNew.setChecked(False)
                            self.ui.homeDockRadioNew.setAutoExclusive(True)
                            self.ui.homeDockRadioStocked.setAutoExclusive(False)
                            self.ui.homeDockRadioStocked.setChecked(False)
                            self.ui.homeDockRadioStocked.setAutoExclusive(True)
                        else:
                            QMessageBox.warning(self, "Failed", "Couldnt Delete from the list")
                    else:
                        QMessageBox.warning(self, "Failed", "Laptop couldnt be send to server room")
            else:
                pass

    def sendForRepairs(self):
        conn = connections.conndb()
        msg = QMessageBox()
        row = self.ui.InUseTableWidget.currentRow()
        laptopSerial = self.ui.sendForRepairLaptopSerial.text().upper()
        spareLaptop = self.ui.spareCombo.currentText()
        rowItemLaptopID = self.ui.InUseTableWidget.item(row,0).text().upper()
        rowItemUser = self.ui.InUseTableWidget.item(row,1).text().title()
        rowItemModel = self.ui.InUseTableWidget.item(row,3).text().upper()
        updatedBy = self.ui.sessionUser.text()
        currentRow = self.ui.InUseTableWidget.currentRow()
        rowSelection = self.ui.txtInuseSLNO.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        if (laptopSerial=="" ):
            QMessageBox.warning(self, "Required", "Please select an item from the Record")
        elif (spareLaptop==""):
            QMessageBox.warning(self, "Required", "Please Specify Spare Laptop to be replaced")
        else:
            get_spare_laptop = f"""SELECT * from laptopinventory WHERE LaptopSerial='{spareLaptop}'"""
            result = conn.queryResult(get_spare_laptop)

            if result:
                # Access the first tuple in the result list
                row = result[0]
                serverLaptopSerial = row[1]
                serverLaptopModel = row[2]
                
                
                send_for_repairs = f"""INSERT INTO repairsrecord (RepairLaptopSerial,RepairLaptopModel,RepairLaptopUser,RepairSource,RepairSpareProvided,RepairSpareModel,RepairLaptopStatus,UpdatedBy,ChangeDate) VALUES
                    ('{laptopSerial}','{rowItemModel}','{rowItemUser}','From InUse','{spareLaptop}','{serverLaptopModel}','For Repairs','{updatedBy}','{changeDate}');
                    """
                delete_laptop_from_server = f"DELETE FROM laptopinventory WHERE LaptopSerial='{serverLaptopSerial}'"

                update_inuse_inventory = f"""UPDATE inuseinventory SET LaptopSerial='{spareLaptop} (Spare)',ModelNumber='{serverLaptopModel}',PreviousLaptopSerial='{laptopSerial}',CurrentStatus='Sent For Repairs',UpdatedBy='{updatedBy}',ChangeDate='{changeDate}'
                WHERE SerialNumber='{rowItemLaptopID}'
                """
                if not (conn.queryExecute(send_for_repairs)):
                    if not (conn.queryExecute(delete_laptop_from_server)):
                        if not (conn.queryExecute(update_inuse_inventory)):
                            QMessageBox.information(self, "Success", "Laptop has been Sent for Repairs")

                            self.ui.txtInuseLaptopSerial.setText("")
                            self.ui.txtInuseSLNO.setText("")
                            self.ui.txtInuseLaptopModel.setText("")
                            self.ui.txtInuseUser.setText("")
                            self.ui.txtInuseLaptopStatus.setText("")
                            self.ui.officeEquipMonitorSpin.setValue(0)
                            self.ui.homeEquipMonitorSpin.setValue(0)
                            self.ui.extraEquipOffice.setText("")
                            self.ui.extraEquipHome.setText("")

                            self.ui.offboardingLaptopSerial.setText("")
                            self.ui.sendForRepairLaptopSerial.setText("")
                            self.ui.spareCombo.setCurrentText("")

                            self.ui.officeKeyboardRadioNew.setAutoExclusive(False)
                            self.ui.officeKeyboardRadioNew.setChecked(False)
                            self.ui.officeKeyboardRadioNew.setAutoExclusive(True)
                            self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
                            self.ui.officeKeyboardRadioStocked.setChecked(False)
                            self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
                            self.ui.homeKeyboardRadioNew.setAutoExclusive(False)
                            self.ui.homeKeyboardRadioNew.setChecked(False)
                            self.ui.homeKeyboardRadioNew.setAutoExclusive(True)
                            self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
                            self.ui.homeKeyboardRadioStocked.setChecked(False)
                            self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)

                            self.ui.officeMouseRadioNew.setAutoExclusive(False)
                            self.ui.officeMouseRadioNew.setChecked(False)
                            self.ui.officeMouseRadioNew.setAutoExclusive(True)
                            self.ui.officeMouseRadioStocked.setAutoExclusive(False)
                            self.ui.officeMouseRadioStocked.setChecked(False)
                            self.ui.officeMouseRadioStocked.setAutoExclusive(True)
                            self.ui.homeMouseRadioNew.setAutoExclusive(False)
                            self.ui.homeMouseRadioNew.setChecked(False)
                            self.ui.homeMouseRadioNew.setAutoExclusive(True)
                            self.ui.homeMouseRadioStocked.setAutoExclusive(False)
                            self.ui.homeMouseRadioStocked.setChecked(False)
                            self.ui.homeMouseRadioStocked.setAutoExclusive(True)

                            self.ui.officeHeadphoneRadioNew.setAutoExclusive(False)
                            self.ui.officeHeadphoneRadioNew.setChecked(False)
                            self.ui.officeHeadphoneRadioNew.setAutoExclusive(True)
                            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
                            self.ui.officeHeadphoneRadioStocked.setChecked(False)
                            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
                            self.ui.homeHeadphoneRadioNew.setAutoExclusive(False)
                            self.ui.homeHeadphoneRadioNew.setChecked(False)
                            self.ui.homeHeadphoneRadioNew.setAutoExclusive(True)
                            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
                            self.ui.homeHeadphoneRadioStocked.setChecked(False)
                            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)

                            self.ui.officeMonitorRadioNew.setAutoExclusive(False)
                            self.ui.officeMonitorRadioNew.setChecked(False)
                            self.ui.officeMonitorRadioNew.setAutoExclusive(True)
                            self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
                            self.ui.officeMonitorRadioStocked.setChecked(False)
                            self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
                            self.ui.homeMonitorRadioNew.setAutoExclusive(False)
                            self.ui.homeMonitorRadioNew.setChecked(False)
                            self.ui.homeMonitorRadioNew.setAutoExclusive(True)
                            self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
                            self.ui.homeMonitorRadioStocked.setChecked(False)
                            self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

                            self.ui.officeDockRadioNew.setAutoExclusive(False)
                            self.ui.officeDockRadioNew.setChecked(False)
                            self.ui.officeDockRadioNew.setAutoExclusive(True)
                            self.ui.officeDockRadioStocked.setAutoExclusive(False)
                            self.ui.officeDockRadioStocked.setChecked(False)
                            self.ui.officeDockRadioStocked.setAutoExclusive(True)
                            self.ui.homeDockRadioNew.setAutoExclusive(False)
                            self.ui.homeDockRadioNew.setChecked(False)
                            self.ui.homeDockRadioNew.setAutoExclusive(True)
                            self.ui.homeDockRadioStocked.setAutoExclusive(False)
                            self.ui.homeDockRadioStocked.setChecked(False)
                            self.ui.homeDockRadioStocked.setAutoExclusive(True)

                            li.displayLaptopTable(self,li.getAllLaptops(self))

                            from repairsRecord import RepairsRecord as rr
                            rr.displayRepairsLaptopTable(self,rr.getAllLaptops(self))

                            InuseInvFunctions.displayInuseTable(self,InuseInvFunctions.getAllInuseItems(self))
                            
                        else:
                            QMessageBox.warning(self, "Failed", "Could not update In-Use Inventory")
                    else:
                        QMessageBox.warning(self, "Failed", "Could not delete Spare Laptop from Server")
                else:
                    QMessageBox.warning(self, "Failed", "Could not Send for Repairs")
            else:
                QMessageBox.critical(self, "Failed", "Critical Error")

    def clearInuse(self):
            self.ui.txtInuseLaptopSerial.setText("")
            self.ui.txtInuseSLNO.setText("")
            self.ui.txtInuseLaptopModel.setText("")
            self.ui.txtInuseUser.setText("")
            self.ui.txtInuseLaptopStatus.setText("")
            self.ui.officeEquipMonitorSpin.setValue(0)
            self.ui.homeEquipMonitorSpin.setValue(0)
            self.ui.extraEquipOffice.setText("")
            self.ui.extraEquipHome.setText("")

            self.ui.offboardingLaptopSerial.setText("")
            self.ui.sendForRepairLaptopSerial.setText("")
            self.ui.spareCombo.setCurrentText("")

            self.ui.officeKeyboardRadioNew.setAutoExclusive(False)
            self.ui.officeKeyboardRadioNew.setChecked(False)
            self.ui.officeKeyboardRadioNew.setAutoExclusive(True)
            self.ui.officeKeyboardRadioStocked.setAutoExclusive(False)
            self.ui.officeKeyboardRadioStocked.setChecked(False)
            self.ui.officeKeyboardRadioStocked.setAutoExclusive(True)
            self.ui.homeKeyboardRadioNew.setAutoExclusive(False)
            self.ui.homeKeyboardRadioNew.setChecked(False)
            self.ui.homeKeyboardRadioNew.setAutoExclusive(True)
            self.ui.homeKeyboardRadioStocked.setAutoExclusive(False)
            self.ui.homeKeyboardRadioStocked.setChecked(False)
            self.ui.homeKeyboardRadioStocked.setAutoExclusive(True)

            self.ui.officeMouseRadioNew.setAutoExclusive(False)
            self.ui.officeMouseRadioNew.setChecked(False)
            self.ui.officeMouseRadioNew.setAutoExclusive(True)
            self.ui.officeMouseRadioStocked.setAutoExclusive(False)
            self.ui.officeMouseRadioStocked.setChecked(False)
            self.ui.officeMouseRadioStocked.setAutoExclusive(True)
            self.ui.homeMouseRadioNew.setAutoExclusive(False)
            self.ui.homeMouseRadioNew.setChecked(False)
            self.ui.homeMouseRadioNew.setAutoExclusive(True)
            self.ui.homeMouseRadioStocked.setAutoExclusive(False)
            self.ui.homeMouseRadioStocked.setChecked(False)
            self.ui.homeMouseRadioStocked.setAutoExclusive(True)

            self.ui.officeHeadphoneRadioNew.setAutoExclusive(False)
            self.ui.officeHeadphoneRadioNew.setChecked(False)
            self.ui.officeHeadphoneRadioNew.setAutoExclusive(True)
            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(False)
            self.ui.officeHeadphoneRadioStocked.setChecked(False)
            self.ui.officeHeadphoneRadioStocked.setAutoExclusive(True)
            self.ui.homeHeadphoneRadioNew.setAutoExclusive(False)
            self.ui.homeHeadphoneRadioNew.setChecked(False)
            self.ui.homeHeadphoneRadioNew.setAutoExclusive(True)
            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(False)
            self.ui.homeHeadphoneRadioStocked.setChecked(False)
            self.ui.homeHeadphoneRadioStocked.setAutoExclusive(True)

            self.ui.officeMonitorRadioNew.setAutoExclusive(False)
            self.ui.officeMonitorRadioNew.setChecked(False)
            self.ui.officeMonitorRadioNew.setAutoExclusive(True)
            self.ui.officeMonitorRadioStocked.setAutoExclusive(False)
            self.ui.officeMonitorRadioStocked.setChecked(False)
            self.ui.officeMonitorRadioStocked.setAutoExclusive(True)
            self.ui.homeMonitorRadioNew.setAutoExclusive(False)
            self.ui.homeMonitorRadioNew.setChecked(False)
            self.ui.homeMonitorRadioNew.setAutoExclusive(True)
            self.ui.homeMonitorRadioStocked.setAutoExclusive(False)
            self.ui.homeMonitorRadioStocked.setChecked(False)
            self.ui.homeMonitorRadioStocked.setAutoExclusive(True)

            self.ui.officeDockRadioNew.setAutoExclusive(False)
            self.ui.officeDockRadioNew.setChecked(False)
            self.ui.officeDockRadioNew.setAutoExclusive(True)
            self.ui.officeDockRadioStocked.setAutoExclusive(False)
            self.ui.officeDockRadioStocked.setChecked(False)
            self.ui.officeDockRadioStocked.setAutoExclusive(True)
            self.ui.homeDockRadioNew.setAutoExclusive(False)
            self.ui.homeDockRadioNew.setChecked(False)
            self.ui.homeDockRadioNew.setAutoExclusive(True)
            self.ui.homeDockRadioStocked.setAutoExclusive(False)
            self.ui.homeDockRadioStocked.setChecked(False)
            self.ui.homeDockRadioStocked.setAutoExclusive(True)

    def inuseSearch(self):
        searchText = self.ui.InUseRecordSearchTxt.text().lower()
        input = self.ui.InUseRecordSearchCombo.currentText()
        selection = ""
        if input == "Serial (A-Z)":
            selection = "LaptopSerial"
        elif input == "Model (A-Z)":
            selection = "ModelNumber"
        else:
            selection = "user"
            
        if searchText!= "":

            conn = connections.conndb()
            strsql = f"SELECT * FROM inuseinventory WHERE '{selection}' LIKE '%{searchText}%'"
            result = conn.queryResult(strsql)
            row = 0
            records = self.ui.InUseTableWidget.setRowCount(len(result))
            for inuseRecords in result:

                self.ui.InUseTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(inuseRecords[0])))
                self.ui.InUseTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(inuseRecords[1])))
                self.ui.InUseTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(inuseRecords[2])))
                self.ui.InUseTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(inuseRecords[3])))
                self.ui.InUseTableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(inuseRecords[4])))
                self.ui.InUseTableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(inuseRecords[5])))
                # self.ui.InUseTableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(inuseRecords[6])))
                if (inuseRecords[6])=="1":
                    self.ui.InUseTableWidget.setItem(row,7,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[7])=="1":
                    self.ui.InUseTableWidget.setItem(row,8,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[8])=="1":
                    self.ui.InUseTableWidget.setItem(row,9,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[9])=="1":
                    self.ui.InUseTableWidget.setItem(row,10,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[10])=="1":
                    self.ui.InUseTableWidget.setItem(row,11,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[11])=="1":
                    self.ui.InUseTableWidget.setItem(row,12,QtWidgets.QTableWidgetItem("✅"))
                
                self.ui.InUseTableWidget.setItem(row,13,QtWidgets.QTableWidgetItem(str(inuseRecords[12])))
                self.ui.InUseTableWidget.setItem(row,14,QtWidgets.QTableWidgetItem(str(inuseRecords[13])))

                if (inuseRecords[14])=="1":
                    self.ui.InUseTableWidget.setItem(row,15,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[15])=="1":
                    self.ui.InUseTableWidget.setItem(row,16,QtWidgets.QTableWidgetItem("✅"))
                
                self.ui.InUseTableWidget.setItem(row,17,QtWidgets.QTableWidgetItem(str(inuseRecords[16])))
                self.ui.InUseTableWidget.setItem(row,18,QtWidgets.QTableWidgetItem(str(inuseRecords[17])))
                self.ui.InUseTableWidget.setItem(row,20,QtWidgets.QTableWidgetItem(str(inuseRecords[18])))
                self.ui.InUseTableWidget.setItem(row,21,QtWidgets.QTableWidgetItem(str(inuseRecords[19])))
            row = row + 1
        else:
            InuseInvFunctions.displayInuseTable(self,InuseInvFunctions.getAllInuseItems(self))

    def displayInuseTable(self,rows):
        conn = connections.conndb()
               
        if rows is not None: 
            
            strsql = "SELECT * FROM inuseinventory"
            result = conn.queryResult(strsql)
            row = 0
            self.ui.InUseTableWidget.setRowCount(len(result))
            self.ui.InUseTableWidget.setSortingEnabled(True)
            for inuseRecords in result:

                self.ui.InUseTableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(inuseRecords[0])))
                self.ui.InUseTableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(inuseRecords[1])))
                self.ui.InUseTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(inuseRecords[2])))
                self.ui.InUseTableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(inuseRecords[3])))
                self.ui.InUseTableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(inuseRecords[4])))
                self.ui.InUseTableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(inuseRecords[5])))
                # self.ui.InUseTableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(inuseRecords[6])))
                if (inuseRecords[6])=="1":
                    self.ui.InUseTableWidget.setItem(row,7,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[7])=="1":
                    self.ui.InUseTableWidget.setItem(row,8,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[8])=="1":
                    self.ui.InUseTableWidget.setItem(row,9,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[9])=="1":
                    self.ui.InUseTableWidget.setItem(row,10,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[10])=="1":
                    self.ui.InUseTableWidget.setItem(row,11,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[11])=="1":
                    self.ui.InUseTableWidget.setItem(row,12,QtWidgets.QTableWidgetItem("✅"))
                
                self.ui.InUseTableWidget.setItem(row,13,QtWidgets.QTableWidgetItem(str(inuseRecords[12])))
                self.ui.InUseTableWidget.setItem(row,14,QtWidgets.QTableWidgetItem(str(inuseRecords[13])))

                if (inuseRecords[14])=="1":
                    self.ui.InUseTableWidget.setItem(row,15,QtWidgets.QTableWidgetItem("✅"))
                if (inuseRecords[15])=="1":
                    self.ui.InUseTableWidget.setItem(row,16,QtWidgets.QTableWidgetItem("✅"))
                
                self.ui.InUseTableWidget.setItem(row,17,QtWidgets.QTableWidgetItem(str(inuseRecords[16])))
                self.ui.InUseTableWidget.setItem(row,18,QtWidgets.QTableWidgetItem(str(inuseRecords[17])))
                self.ui.InUseTableWidget.setItem(row,20,QtWidgets.QTableWidgetItem(str(inuseRecords[18])))
                self.ui.InUseTableWidget.setItem(row,21,QtWidgets.QTableWidgetItem(str(inuseRecords[19])))
                row = row + 1
        else:
            print("No Data Found") 
    
    def inuseGenerateCSV(self):
        # Retrieve data from the database
        conn = connections.conndb()
        strsql = "SELECT * FROM inuseinventory"
        result = conn.queryResult(strsql)
        try:
            # Convert the result to a pandas DataFrame
            df = pd.DataFrame(result, columns=[i[0] for i in conn.cursor.description])
             # Get the path and file name for the Excel file to save
            path, _filter = QFileDialog.getSaveFileName(None, 'Save File', QDir.homePath() + "/ymca_InuseInventory.xlsx", "Excel Files (*.xlsx)")
            if path:
                # Save the DataFrame to the Excel file
                df.to_excel(path, index=False)
                QMessageBox.information(self, "File Saved", f"Excel File Exported to: '{path}'")

        except Exception:
            QMessageBox.warning(self, "Cancel Event", "Cancelled by User")
                
