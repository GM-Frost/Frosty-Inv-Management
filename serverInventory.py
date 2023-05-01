import os
import sys
import connections
from Custom_Widgets.Widgets import *
from interface_ui import *
from PySide2.QtWidgets import QTableWidgetItem

# Import the necessary classes
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import Qt

from datetime import datetime
import pandas as pd

from repairsRecord import RepairsRecord as rr

class LaptopInventoryFunctions():
    def __init__(self,arg):
        super(LaptopInventoryFunctions,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

    def getData(self):
        row = self.ui.laptopRecordsTable.currentRow()
        rowItemSerial = self.ui.laptopRecordsTable.item(row,1).text()
        rowItemModel = self.ui.laptopRecordsTable.item(row,2).text()
        rowItemLastUse = self.ui.laptopRecordsTable.item(row,3).text()
        rowItemStatus = self.ui.laptopRecordsTable.item(row,4).text()
        rowItemLaptopID = self.ui.laptopRecordsTable.item(row,0).text()
        rowSentForRepair = self.ui.laptopRecordsTable.item(row,1).text()
        
        self.ui.txtLaptopSerial.setText(rowItemSerial)
        self.ui.txtModelNumber.setText(rowItemModel)
        self.ui.txtLastUser.setText(rowItemLastUse)
        self.ui.txtComboStatus.setCurrentText(rowItemStatus)
        self.ui.txtLaptopID.setText(rowItemLaptopID)
        self.ui.sendforrepairSerial.setText(rowSentForRepair)

    def getAllLaptops(self):
        conn = connections.conndb()
        get_all_laptops =  """SELECT * FROM laptopinventory"""
        try:
            c = conn.queryResult(get_all_laptops)
            return c
        except Exception as e:
            print("Couldnt get all Laptops")

    def addLaptop(self):
        msg = QMessageBox()
               
        newLapSerial = self.ui.txtLaptopSerial.text().upper()
        newLapModel = self.ui.txtModelNumber.text().upper()
        newLapUser = self.ui.txtLastUser.text().title()
        newLapStatus = self.ui.txtComboStatus.currentText()
        fullname = self.ui.sessionUser.text()

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        currentDate = changeDate
        insert_laptop_data = f"""
        INSERT INTO laptopinventory (LaptopSerial,LaptopModel,LastUser,LaptopStatus,UpdatedBy,ChangeDate) VALUES 
        ('{newLapSerial}','{newLapModel}','{newLapUser}','{newLapStatus}','{fullname}','{currentDate}');
        """
        dupEntryQuery =  f"""SELECT * FROM laptopinventory where LaptopSerial='{newLapSerial}'"""
        conn = connections.conndb()
        dupEntry = conn.queryResult(dupEntryQuery)

        dupEntryQuery2 =  f"""SELECT * FROM inuseinventory where LaptopSerial='{newLapSerial}'"""
        conn = connections.conndb()
        dupEntry2 = conn.queryResult(dupEntryQuery2)

        dupEntryQuery3 =  f"""SELECT * FROM repairsrecord where RepairLaptopSerial='{newLapSerial}'"""
        conn = connections.conndb()
        dupEntry3 = conn.queryResult(dupEntryQuery3)

        if (newLapSerial=="")or(newLapModel=="")or(newLapStatus==""):
            QMessageBox.information(self, "Incomplete", "Please Enter the Required Values")
        elif dupEntry:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial Exists on Records")
        elif dupEntry2:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial is present in In-Use Inventory")
        elif dupEntry3:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial is present in Repairs Record")

        else:
            if not (conn.queryExecute(insert_laptop_data)):
                conn.queryClose
                self.ui.txtLaptopSerial.setText("")
                self.ui.txtModelNumber.setText("")
                self.ui.txtLastUser.setText("")
                self.ui.txtComboStatus.setCurrentText("")
                self.ui.txtLaptopID.setText("")
                self.ui.sendforrepairSerial.setText("")
                self.ui.sendforrepairStatus.setCurrentText("")
                self.ui.txtLapInvSearch.setText("")
                LaptopInventoryFunctions.displayLaptopTable(self,LaptopInventoryFunctions.getAllLaptops(self))
                # self.ui.notificationBtn.click()
                # self.ui.notificationMsg.setText("Record Added !!!")
                QMessageBox.information(self, "Success", "Record Added")
               
            else:
                QMessageBox.information(self, "Sorry", "Couldnt Add to the Records. Please Try again.")

           
    def updateLaptop(self):
        msg = QMessageBox()
               
        laptopID = self.ui.txtLaptopID.text()
        serialNumber = self.ui.txtLaptopSerial.text()
        modelNumber = self.ui.txtModelNumber.text()
        lastUser = self.ui.txtLastUser.text()
        laptopStatus = self.ui.txtComboStatus.currentText()
        fullname = self.ui.sessionUser.text()
    
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        try:
            if (laptopID!=""):
                row = int(self.ui.laptopRecordsTable.currentRow())
                rowSerial = self.ui.laptopRecordsTable.item(row,1).text()
                if (serialNumber!=rowSerial):
                    QMessageBox.information(self, "Error - Input Mismatch", "Possible Duplicate or Out-of-Bound Entry\n\nRecord Could not be Updated.")
                else:
                    strsql = "UPDATE laptopinventory SET LaptopSerial='"+serialNumber+"',LaptopModel='"+modelNumber+"', LastUser='"+lastUser+"',LaptopStatus ='"+laptopStatus+"',UpdatedBy='"+fullname+"',ChangeDate='"+changeDate+"' where ID='"+laptopID+"'"
                    conn = connections.conndb()
                    
                    if not (conn.queryExecute(strsql)):
                        
                        self.ui.txtLaptopSerial.setText("")
                        self.ui.txtModelNumber.setText("")
                        self.ui.txtLastUser.setText("")
                        self.ui.txtComboStatus.setCurrentText("")
                        self.ui.txtLaptopID.setText("")
                        self.ui.sendforrepairSerial.setText("")
                        self.ui.sendforrepairStatus.setCurrentText("")
                        self.ui.txtLapInvSearch.setText("")
                        # self.ui.notificationBtn.click()
                        # self.ui.notificationMsg.setText("Record Updated !!!")
                        QMessageBox.information(self, "Success", "Record Updated")
                        LaptopInventoryFunctions.displayLaptopTable(self,LaptopInventoryFunctions.getAllLaptops(self))
            else:
                QMessageBox.warning(self, "Failed", "Update Failed")

        except:
            QMessageBox.warning(self, "Update Fail", "Please select the record to Update")


    def deleteLaptop(self):
        msg = QMessageBox()
        laptopID = self.ui.txtLaptopID.text()
        serialNumber = self.ui.txtLaptopSerial.text()
      

        strsql = "DELETE FROM laptopinventory WHERE LaptopSerial='"+serialNumber+"' AND ID='"+laptopID+"'"
        conn = connections.conndb()
        
        try:
            if (laptopID==""):
                QMessageBox.warning(self, "Failure", "Please select the record to Delete")
            else:
                if not (conn.queryExecute(strsql)):
                    conn.queryClose
                    self.ui.txtLaptopSerial.setText("")
                    self.ui.txtModelNumber.setText("")
                    self.ui.txtLastUser.setText("")
                    self.ui.txtComboStatus.setCurrentText("")
                    self.ui.txtLaptopID.setText("")
                    self.ui.sendforrepairSerial.setText("")
                    self.ui.sendforrepairStatus.setCurrentText("")
                    self.ui.txtLapInvSearch.setText("")
                    # self.ui.notificationBtn.click()
                    # self.ui.notificationMsg.setText("Record Deleted !!!")
                    QMessageBox.information(self, "Deleted", "Record Deleted")
                    LaptopInventoryFunctions.displayLaptopTable(self,LaptopInventoryFunctions.getAllLaptops(self))
        except:
            QMessageBox.warning(self, "Exceptional", "Something went wrong")
    
    def search(self):
        searchText = self.ui.txtLapInvSearch.text().lower()
        input = self.ui.txtLapInvSearchCombo.currentText()
        selection = ""
        if input == "Serial (A-Z)":
            selection = "LaptopSerial"
        elif input == "Model (A-Z)":
            selection = "LaptopModel"
        else:
            selection = "LastUser"
            
        if searchText!= "":

            conn = connections.conndb()
            strsql = f"SELECT * FROM laptopinventory WHERE '{selection}' LIKE '%{searchText}%'"
            result = conn.queryResult(strsql)
            row = 0
            records = self.ui.laptopRecordsTable.setRowCount(len(result))
            for laptops in result:
                self.ui.laptopRecordsTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(laptops[0])))
                self.ui.laptopRecordsTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(laptops[1])))
                self.ui.laptopRecordsTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(laptops[2])))
                self.ui.laptopRecordsTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(laptops[3])))
                self.ui.laptopRecordsTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(laptops[4])))
                self.ui.laptopRecordsTable.setItem(row,5,QtWidgets.QTableWidgetItem(str(laptops[5])))
                self.ui.laptopRecordsTable.setItem(row,6,QtWidgets.QTableWidgetItem(str(laptops[6])))
            row = row + 1
        else:
            LaptopInventoryFunctions.displayLaptopTable(self,LaptopInventoryFunctions.getAllLaptops(self))

    
    def displayLaptopTable(self,rows):
        if rows is not None: 
          
            conn = connections.conndb()
            strsql = "SELECT * FROM laptopinventory"
            result = conn.queryResult(strsql)
            row = 0
            self.ui.laptopRecordsTable.setRowCount(len(result))
            self.ui.laptopRecordsTable.setSortingEnabled(True)
            for laptops in result:
                self.ui.laptopRecordsTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(laptops[0])))
                self.ui.laptopRecordsTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(laptops[1])))
                self.ui.laptopRecordsTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(laptops[2])))
                self.ui.laptopRecordsTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(laptops[3])))
                self.ui.laptopRecordsTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(laptops[4])))
                self.ui.laptopRecordsTable.setItem(row,5,QtWidgets.QTableWidgetItem(str(laptops[5])))
                self.ui.laptopRecordsTable.setItem(row,6,QtWidgets.QTableWidgetItem(str(laptops[6])))

                row = row + 1
        else:
            print("No Data Found")  

    def laptopGenerateCSV(self):
        msg = QMessageBox()
        try:
            path, _filter = QFileDialog.getSaveFileName(self, 'Save File',QDir.homePath()+"/ymca_ServerLaptopInventory.xlsx","CSV_FILES(*.xlsx *.csv)")
            columnHeaders = []
            for j in range(self.ui.laptopRecordsTable.model().columnCount()):
                columnHeaders.append(self.ui.laptopRecordsTable.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.laptopRecordsTable.rowCount()):
                for col in range(self.ui.laptopRecordsTable.columnCount()):
                    df.at[row,columnHeaders[col]]=self.ui.laptopRecordsTable.item(row, col).text()
                
            df.to_excel(path,index = False)
            QMessageBox.information(self, "File Saved", f"Excel File Exported to: '{path}'")
        except Exception:
            QMessageBox.warning(self, "Cancel Event", "Cancelled by User")
#------------------------------------------- SEND FOR REPAIR FUNCTIONS --------------------------------------------------#

    def sendforrepair(self):
        msg = QMessageBox()
        conn = connections.conndb()
        serialNumber = self.ui.sendforrepairSerial.text().upper()
        status = self.ui.sendforrepairStatus.currentText()
        modelNumber = self.ui.txtModelNumber.text().upper()
        lastUser = self.ui.txtLastUser.text().title()
        updatedBy = self.ui.sessionUser.text()
        laptopID = self.ui.txtRepairLaptopID.text()
        spareProvided=""
        spareModel = ""
        source="Server Room"
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string


        checkLaptop =  f"""SELECT * FROM laptopinventory where LaptopSerial='{serialNumber}'"""
        
        result = conn.queryResult(checkLaptop)

        if not result:
            # msg.setWindowTitle("Laptop Not Present")
            # msg.setText("Serial Not Valid/Not Present in the Records")
            # x = msg.exec_()
            QMessageBox.warning(self, "Laptop Not Present", "Serial Not Valid/Not Present in the Records")
        elif status=="":
            QMessageBox.information(self, "Status", "Please Specify Status of Laptop.")

        else:
            insert_laptop_to_repairs = f"""
                INSERT INTO repairsrecord (RepairLaptopSerial,RepairLaptopModel,RepairLaptopUser,RepairSource,RepairSpareProvided,RepairSpareModel,RepairLaptopStatus,UpdatedBy,ChangeDate) VALUES
                ('{serialNumber}','{modelNumber}','{lastUser}','{source}','{spareProvided}','{spareModel}','{status}','{updatedBy}','{changeDate}');
                """
            delete_laptop_from_server = f"DELETE FROM laptopinventory WHERE LaptopSerial='{serialNumber}'"
            if not (conn.queryExecute(insert_laptop_to_repairs)):
                if not (conn.queryExecute(delete_laptop_from_server)):
                    QMessageBox.information(self, "Status", "Laptop Sent for Repairs")
                    self.ui.txtLaptopSerial.setText("")
                    self.ui.txtModelNumber.setText("")
                    self.ui.txtLastUser.setText("")
                    self.ui.txtComboStatus.setCurrentText("")
                    self.ui.txtLaptopID.setText("")
                    self.ui.sendforrepairSerial.setText("")
                    self.ui.sendforrepairStatus.setCurrentText("")
                    self.ui.txtLapInvSearch.setText("")

                    LaptopInventoryFunctions.displayLaptopTable(self,LaptopInventoryFunctions.getAllLaptops(self))
                    rr.displayRepairsLaptopTable(self,rr.getAllLaptops(self))

                


            
#-------------------------------------------------------------------## EXTRA EQUIPMENT FUNCTIONS ##-------------------------------------------------#

class EquipInventoryFunctions():
    def __init__(self,arg):
        super(LaptopInventoryFunctions,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
    
    def getAllEquipments(self):
        conn = connections.conndb()
        get_all_equipments =  """SELECT * FROM equipmentsrecord"""
        try:
            c = conn.queryResult(get_all_equipments)
            return c
        except Exception as e:
            print("Couldnt get all Equipments")
    
    def getEquipData(self):
        row = self.ui.equipRecordTable.currentRow()
        if (row>=5):
            rowEquipItem = self.ui.equipRecordTable.item(row,1).text()
            rowEquipItemCount = int(self.ui.equipRecordTable.item(row,2).text())

            self.ui.equipOtherItemCombo.setCurrentText(rowEquipItem)
            self.ui.equipOtherItemSpinbox.setValue(rowEquipItemCount)
        else:
            self.ui.equipOtherItemCombo.setCurrentText("")
            self.ui.equipOtherItemSpinbox.setValue(0)

    def updateEquip(self):
        equipKeyboard = int(self.ui.txtEquipKeyboardSpin.value())
        equipMouse = self.ui.txtEquipMouseSpin.value()
        equipHeadphones = self.ui.txtEquipHeadphoneSpin.value()
        equipMonitor = self.ui.txtEquipMonitorSpin.value()
        equipDocks = self.ui.txtEquipDockSpin.value()

        updatedby = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        if (int(self.ui.txtEquipKeyboardSpin.value()) != int(self.ui.equipRecordTable.item(0,2).text())):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{equipKeyboard}',equipUpdatedby='{updatedby}',equipChangeDate='{changeDate}' where equipItems ='Keyboard'"
            conn = connections.conndb()

            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Status", "Keyboard Updated")
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))

        if (int(self.ui.txtEquipMouseSpin.value()) != int(self.ui.equipRecordTable.item(1,2).text())):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{equipMouse}',equipUpdatedby='{updatedby}',equipChangeDate='{changeDate}' where equipItems ='Mouse'"
            conn = connections.conndb()

            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Status", "Mouse Updated")
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))

        if (int(self.ui.txtEquipHeadphoneSpin.value()) != int(self.ui.equipRecordTable.item(2,2).text())):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{equipHeadphones}',equipUpdatedby='{updatedby}',equipChangeDate='{changeDate}' where equipItems ='Headphones'"
            conn = connections.conndb()

            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Status", "Headphones Updated")
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
        
        if (int(self.ui.txtEquipMonitorSpin.value()) != int(self.ui.equipRecordTable.item(3,2).text())):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{equipMonitor}',equipUpdatedby='{updatedby}',equipChangeDate='{changeDate}' where equipItems ='Monitors'"
            conn = connections.conndb()

            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Status", "Monitor Updated")
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
        
        if (int(self.ui.txtEquipDockSpin.value()) != int(self.ui.equipRecordTable.item(4,2).text())):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{equipDocks}',equipUpdatedby='{updatedby}',equipChangeDate='{changeDate}' where equipItems ='Docks'"
            conn = connections.conndb()

            if not (conn.queryExecute(strsql)):
                QMessageBox.information(self, "Status", "Docks Updated")
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
    
    def addEquip(self):
        
        otherEquipItem = self.ui.equipOtherItemCombo.currentText()
        otherEquipCount = self.ui.equipOtherItemSpinbox.value()
        
        updatedby = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        currentDate = changeDate

        insert_other_equip_item = f"""
        INSERT INTO equipmentsrecord (equipItems,equipItemCount,equipUpdatedby,equipChangeDate) VALUES 
        ('{otherEquipItem}','{otherEquipCount}','{updatedby}','{currentDate}');
        """

        selectQuery =  f"""SELECT * FROM equipmentsrecord where equipItems='{otherEquipItem}' """
        conn = connections.conndb()
        c = conn.queryResult(selectQuery)
        if c:
          QMessageBox.warning(self, "Duplicate Entry", "This Equipment is already present.\nPlease Update to make specific Changes")
        elif (otherEquipItem == ""):
            QMessageBox.information(self, "Required", "Please specify the Item to be Added")

        else:
            if not (conn.queryExecute(insert_other_equip_item)):
                self.ui.equipOtherItemCombo.setCurrentText("")
                self.ui.equipOtherItemSpinbox.setValue(0)
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
                QMessageBox.information(self, "Status", "Equipment Added Successfully!")
            else:
                QMessageBox.warning(self, "Status", "Error Adding the Equipement")


    def updateExtraEquip(self):
        extraEquipItemCombo = self.ui.equipOtherItemCombo.currentText()
        extraEquipItemCount = self.ui.equipOtherItemSpinbox.value()
        updatedBy = self.ui.sessionUser.text()
    
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string

        row = self.ui.equipRecordTable.currentRow()
        if (row>=5):
            strsql = f"UPDATE equipmentsrecord SET equipItemCount='{extraEquipItemCount}', equipUpdatedby='{updatedBy}', equipChangeDate='{changeDate}' where equipItems='{extraEquipItemCombo}'"
            conn = connections.conndb()
            if not (conn.queryExecute(strsql)):
                self.ui.equipOtherItemCombo.setCurrentText("")
                self.ui.equipOtherItemSpinbox.setValue(0)
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
                QMessageBox.information(self, "Status", "Equipment Updated Successfully!")
        else:
            QMessageBox.information(self, "Status", "Please Select Item to Update.")

    def deleteExtraEquip(self):

        extraEquipItemCombo = self.ui.equipOtherItemCombo.currentText()
        extraEquipItemCount = self.ui.equipOtherItemSpinbox.value()
        row = self.ui.equipRecordTable.currentRow()
        if (row>=5):
            strsql = f"DELETE FROM equipmentsrecord WHERE equipItems='{extraEquipItemCombo}' and equipItemCount='{extraEquipItemCount}'"
            conn = connections.conndb()
            
            if not (conn.queryExecute(strsql)):
                self.ui.equipOtherItemCombo.setCurrentText("")
                self.ui.equipOtherItemSpinbox.setValue(0)
                QMessageBox.information(self, "Status", "Equipment Deleted")  
                conn.queryClose
                EquipInventoryFunctions.displayEquipmentsTable(self,EquipInventoryFunctions.getAllEquipments(self))
        else:
            QMessageBox.information(self, "Status", "Please Select Item to Delete.")  


    def equipmentsGenerateCSV(self):
        msg = QMessageBox()
        try:
            path, _filter = QFileDialog.getSaveFileName(self, 'Save File',QDir.homePath()+"/ymca_EquipmentList.xlsx","CSV_FILES(*.xlsx *.csv)")
            columnHeaders = []
            for j in range(self.ui.equipRecordTable.model().columnCount()):
                columnHeaders.append(self.ui.equipRecordTable.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.equipRecordTable.rowCount()):
                for col in range(self.ui.equipRecordTable.columnCount()):
                    df.at[row,columnHeaders[col]]=self.ui.equipRecordTable.item(row, col).text()
                
            df.to_excel(path,index = False)
            QMessageBox.information(self, "File Saved", f"Excel File Exported to: '{path}'")
        except Exception:
            QMessageBox.warning(self, "Cancel Event", "Cancelled by User")


    def displayEquipmentsTable(self,rows):
       
        if rows is not None: 
            conn = connections.conndb()
            strsql = "SELECT * FROM equipmentsrecord"
            result = conn.queryResult(strsql)
            
            
            row = 0
            self.ui.equipRecordTable.setRowCount(len(result))
            for equips in result:
                self.ui.equipRecordTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(equips[0])))
                self.ui.equipRecordTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(equips[1])))
                self.ui.equipRecordTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(equips[2])))
                self.ui.equipRecordTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(equips[3])))
                self.ui.equipRecordTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(equips[4])))
                row = row + 1
        else:
            print("No Data Found")  
            
        try:

            rowItemKeyboard = int(self.ui.equipRecordTable.item(0,2).text())
            rowItemMouse = int(self.ui.equipRecordTable.item(1,2).text())
            rowItemHeadphones = int(self.ui.equipRecordTable.item(2,2).text())
            rowItemMonitor = int(self.ui.equipRecordTable.item(3,2).text())
            rowItemDocks = int(self.ui.equipRecordTable.item(4,2).text())

            self.ui.txtEquipKeyboardSpin.setValue(rowItemKeyboard)
            self.ui.txtEquipMouseSpin.setValue(rowItemMouse)
            self.ui.txtEquipHeadphoneSpin.setValue(rowItemHeadphones)
            self.ui.txtEquipMonitorSpin.setValue(rowItemMonitor)
            self.ui.txtEquipDockSpin.setValue(rowItemDocks)
        except Exception:
            print("No Equipment Found")
        

    
    