import os
import sys
import connections
from Custom_Widgets.Widgets import *
from interface_ui import *
from PySide2.QtWidgets import QTableWidgetItem
import pandas as pd


from datetime import datetime

class RepairsRecord():
    def __init__(self,arg):
        super(RepairsRecord,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        
    def getData(self):
        row = self.ui.RepairsRecordTable.currentRow()
        rowItemSerial = self.ui.RepairsRecordTable.item(row,1).text()
        rowItemModel = self.ui.RepairsRecordTable.item(row,2).text()
        rowItemLastUse = self.ui.RepairsRecordTable.item(row,3).text()
        rowItemSpareProvided = self.ui.RepairsRecordTable.item(row,4).text()
        rowItemLaptopID = self.ui.RepairsRecordTable.item(row,0).text()
        rowItemStatus = self.ui.RepairsRecordTable.item(row,7).text()

        self.ui.txtSentForRepairSerial.setText(rowItemSerial)
        self.ui.txtSentForRepairModel.setText(rowItemModel)
        self.ui.txtSentForRepairLastUser.setText(rowItemLastUse)
        self.ui.txtSentForRepairStatus.setCurrentText(rowItemSpareProvided)
        self.ui.txtRepairLaptopID.setText(rowItemLaptopID)
        self.ui.txtSentForRepairStatus.setCurrentText(rowItemStatus)

        if (self.ui.RepairsRecordTable.item(row,6).text()!="From InUse"):
            self.ui.txtSSRSerial.setText(rowItemSerial)
        else:
            self.ui.txtSSRSerial.setText("")

        if (self.ui.RepairsRecordTable.item(row,6).text()=="From InUse"):
            self.ui.txtSSUSerial.setText(rowItemSerial)
            self.ui.txtSSUSpare.setText(rowItemSpareProvided)
        else:
            self.ui.txtSSUSerial.setText("")
            self.ui.txtSSUSpare.setText("")

    def getAllLaptops(self):
        conn = connections.conndb()
        get_all_laptops =  """SELECT * FROM repairsrecord"""
        try:
            c = conn.queryResult(get_all_laptops)
            return c
        except Exception as e:
            print("Couldnt get all Laptops")

    def addLaptop(self):
        msg = QMessageBox()

        repairLapSerial = self.ui.txtSentForRepairSerial.text().upper()
        repairLapModel = self.ui.txtSentForRepairModel.text().upper()
        repairLapUser = self.ui.txtSentForRepairLastUser.text().title()
        repairLapStatus = self.ui.txtSentForRepairStatus.currentText()
        updatedBy = self.ui.sessionUser.text()
        repairSource = ""
        repairSpareModel = ""
        repairSpare=""

        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        currentDate = changeDate
        insert_repairlaptop_data = f"""
        INSERT INTO repairsrecord (RepairLaptopSerial,RepairLaptopModel,RepairLaptopUser,RepairSource,RepairSpareProvided,RepairSpareModel,RepairLaptopStatus,UpdatedBy,ChangeDate) VALUES
        ('{repairLapSerial}','{repairLapModel}','{repairLapUser}','{repairSource}','{repairSpare}','{repairSpareModel}','{repairLapStatus}','{updatedBy}','{currentDate}');
        """

        dupEntryQuery =  f"""SELECT * FROM repairsrecord where RepairLaptopSerial='{repairLapSerial}'"""
        conn = connections.conndb()
        dupEntry = conn.queryResult(dupEntryQuery)

        dupEntryQuery2 =  f"""SELECT * FROM laptopinventory where LaptopSerial='{repairLapSerial}'"""
        conn2 = connections.conndb()
        dupEntry2 = conn2.queryResult(dupEntryQuery2)

        dupEntryQuery3 =  f"""SELECT * FROM inuseinventory where LaptopSerial='{repairLapSerial}'"""
        conn3 = connections.conndb()
        dupEntry3 = conn3.queryResult(dupEntryQuery3)


        if (repairLapSerial=="" or repairLapModel==""):
            QMessageBox.warning(self, "Incomplete", "Please Enter the Required Values")
        elif dupEntry:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial is present in records")
        elif dupEntry2:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial is present in Server Inventory")
        elif dupEntry3:
            QMessageBox.warning(self, "Duplicate Entry", "This Laptop Serial is present in In-Use Inventory")
        else:
            conn = connections.conndb()
            if not (conn.queryExecute(insert_repairlaptop_data)):
                conn.queryClose
                self.ui.txtSentForRepairSerial.setText("")
                self.ui.txtSentForRepairModel.setText("")
                self.ui.txtSentForRepairLastUser.setText("")
                self.ui.txtSentForRepairStatus.setCurrentText("")
                self.ui.txtRepairLaptopID.setText("")
                self.ui.txtSSRSerial.setText("")
                self.ui.txtSSRStatus.setCurrentText("")
                self.ui.txtSSUSerial.setText("")
                self.ui.txtSSUSpare.setText("")
                RepairsRecord.displayRepairsLaptopTable(self,RepairsRecord.getAllLaptops(self))
                QMessageBox.information(self, "Success", "Laptop Has been Added")
            else:
                print("Couldnot Insert Laptop Data")

   

    def updateLaptop(self):
        msg = QMessageBox()
        conn = connections.conndb()
        repairlaptopID = self.ui.txtRepairLaptopID.text()
        repairLaptopSerial = self.ui.txtSentForRepairSerial.text()
        repairLaptopModel = self.ui.txtSentForRepairModel.text()
        repairlastUser = self.ui.txtSentForRepairLastUser.text()
        repairlaptopStatus = self.ui.txtSentForRepairStatus.currentText()
        updatedBy = self.ui.sessionUser.text()
        
        get_repair_serial = f"""SELECT * FROM repairsrecord WHERE RepairLaptopSerial='{repairLaptopSerial}' and RepairLaptopModel='{repairLaptopModel}'"""
        query = conn.queryResult(get_repair_serial)

        

        if (repairlaptopID==""):
            QMessageBox.information(self, "Required", "Please Select Item to be Updated")
        else:
            row = self.ui.RepairsRecordTable.currentRow()
            isSpare = self.ui.RepairsRecordTable.item(row,4).text()
            if not query:
                QMessageBox.warning(self, "Update Failure", "Laptop Serial | Model cannot be updated!")
            elif isSpare !="":
                QMessageBox.warning(self, "Update Failure", "Spare Laptops Cannot Be Updated!")
            else:
                
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                changeDate = dt_string

                strsql = "UPDATE repairsrecord SET RepairLaptopUser='"+repairlastUser+"',RepairLaptopStatus ='"+repairlaptopStatus+"',UpdatedBy='"+updatedBy+"',ChangeDate='"+changeDate+"' where idrepairsRecord='"+repairlaptopID+"'"
                
                if not (conn.queryExecute(strsql)):
                    conn.queryClose
                    self.ui.txtSentForRepairSerial.setText("")
                    self.ui.txtSentForRepairModel.setText("")
                    self.ui.txtSentForRepairLastUser.setText("")
                    self.ui.txtSentForRepairStatus.setCurrentText("")
                    self.ui.txtRepairLaptopID.setText("")
                    self.ui.txtSSRSerial.setText("")
                    self.ui.txtSSRStatus.setCurrentText("")
                    self.ui.txtSSUSerial.setText("")
                    self.ui.txtSSUSpare.setText("")
                    QMessageBox.warning(self, "Success", "Laptop Has been Updated")
                    RepairsRecord.displayRepairsLaptopTable(self,RepairsRecord.getAllLaptops(self))

    def clearOption(self):
        self.ui.txtSentForRepairSerial.setText("")
        self.ui.txtSentForRepairModel.setText("")
        self.ui.txtSentForRepairLastUser.setText("")
        self.ui.txtSentForRepairStatus.setCurrentText("")
        self.ui.txtRepairLaptopID.setText("")
        self.ui.txtSSRSerial.setText("")
        self.ui.txtSSRStatus.setCurrentText("")


    def search(self):
        searchText = self.ui.txtSearchRepairs.text().lower()
        input = self.ui.repairLaptopSearchCombo.currentText()
        selection = ""
        if input == "Serial (A-Z)":
            selection = "RepairLaptopSerial"
        elif input == "Model (A-Z)":
            selection = "RepairLaptopModel"
        else:
            selection = "RepairLaptopUser"
            
        if searchText!= "":

            conn = connections.conndb()
            strsql = f"SELECT * FROM repairsrecord WHERE '{selection}' LIKE '%{searchText}%'"
            result = conn.queryResult(strsql)
            row = 0
            records = self.ui.RepairsRecordTable.setRowCount(len(result))
            for repairlaptops in result:
                self.ui.RepairsRecordTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(repairlaptops[0])))
                self.ui.RepairsRecordTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(repairlaptops[1])))
                self.ui.RepairsRecordTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(repairlaptops[2])))
                self.ui.RepairsRecordTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(repairlaptops[3])))
                self.ui.RepairsRecordTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(repairlaptops[4])))
                self.ui.RepairsRecordTable.setItem(row,5,QtWidgets.QTableWidgetItem(str(repairlaptops[5])))
                self.ui.RepairsRecordTable.setItem(row,6,QtWidgets.QTableWidgetItem(str(repairlaptops[6])))
            row = row + 1
        else:
            RepairsRecord.displayRepairsLaptopTable(self,RepairsRecord.getAllLaptops(self))


    def sendBacktoServer(self):
        msg = QMessageBox()
        conn = connections.conndb()
        from serverInventory import LaptopInventoryFunctions as li
        row = self.ui.RepairsRecordTable.currentRow()
        laptopSerial= self.ui.txtSSRSerial.text()
        
        laptopStatus = self.ui.txtSSRStatus.currentText()
        updatedBy = self.ui.sessionUser.text()
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        changeDate = dt_string
        
        if (row==""):
            QMessageBox.warning(self, "Required", "Please select item to be sent")

        elif (laptopSerial==""):
            # msg.setWindowTitle("Required!")
            # msg.setText("Please select Laptops other than from Source: In-Use Inventory")
            # x = msg.exec_()
            QMessageBox.warning(self, "Warning", "Please select Laptops other than from Source: In-Use Inventory")

        elif (laptopStatus==""):
            QMessageBox.warning(self, "Required", "Please Select Status of Laptop")

        else:
            laptopModel = self.ui.RepairsRecordTable.item(row,2).text()
            laptopUser = self.ui.RepairsRecordTable.item(row,3).text()
            send_back_to_server = f"""
                INSERT INTO laptopinventory (LaptopSerial,LaptopModel,LastUser,LaptopStatus,UpdatedBy,ChangeDate) VALUES
                ('{laptopSerial}','{laptopModel}','{laptopUser}','{laptopStatus}','{updatedBy}','{changeDate}');
                """
            delete_laptop_from_repairs = f"DELETE FROM repairsrecord WHERE RepairLaptopSerial='{laptopSerial}'"
            if not (conn.queryExecute(send_back_to_server)):
                if not (conn.queryExecute(delete_laptop_from_repairs)):
                    QMessageBox.information(self, "Success", "Laptop Sent Back to Server Room")
                    self.ui.txtSentForRepairSerial.setText("")
                    self.ui.txtSentForRepairModel.setText("")
                    self.ui.txtSentForRepairLastUser.setText("")
                    self.ui.txtSentForRepairStatus.setCurrentText("")
                    self.ui.txtRepairLaptopID.setText("")
                    self.ui.txtSSRSerial.setText("")
                    self.ui.txtSSRStatus.setCurrentText("")
                    self.ui.txtSSUSerial.setText("")
                    self.ui.txtSSUSpare.setText("")
                    
                    li.displayLaptopTable(self,li.getAllLaptops(self))
                    RepairsRecord.displayRepairsLaptopTable(self,RepairsRecord.getAllLaptops(self))

    def sendBacktoUser(self):
        msg = QMessageBox()
        conn = connections.conndb()
        actuallaptopSerial = self.ui.txtSSUSerial.text()
        spareLaptopSerial = self.ui.txtSSUSpare.text()

        if actuallaptopSerial!="" or spareLaptopSerial!="":
            row = self.ui.RepairsRecordTable.currentRow()
            actualLaptopModel = self.ui.RepairsRecordTable.item(row,2).text()
            lastUser = self.ui.RepairsRecordTable.item(row,3).text()
            spareLaptopModel = self.ui.RepairsRecordTable.item(row,5).text()
            updatedBy = self.ui.sessionUser.text()
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            changeDate = dt_string

            update_inuse_inventory = f"""UPDATE inuseinventory SET LaptopSerial='{actuallaptopSerial}',ModelNumber='{actualLaptopModel}',PreviousLaptopSerial='',CurrentStatus='Repaired',UpdatedBy='{updatedBy}',ChangeDate='{changeDate}' WHERE CurrentStatus='Sent For Repairs' and users='{lastUser}'"""
            send_to_server_inv = f"""INSERT INTO laptopinventory (LaptopSerial,LaptopModel,LastUser,LaptopStatus,UpdatedBy,ChangeDate) VALUES ('{spareLaptopSerial}','{spareLaptopModel}','{lastUser}','Spare','{updatedBy}','{changeDate}')"""
            delete_laptop_from_repairs = f"""DELETE FROM repairsrecord WHERE RepairLaptopSerial='{actuallaptopSerial}'"""

            if not (conn.queryExecute(update_inuse_inventory)):
                if not (conn.queryExecute(send_to_server_inv)):
                    if not (conn.queryExecute(delete_laptop_from_repairs)):

                        QMessageBox.information(self, "Sucess", "Laptop Sent Back to User")
                        self.ui.txtSentForRepairSerial.setText("")
                        self.ui.txtSentForRepairModel.setText("")
                        self.ui.txtSentForRepairLastUser.setText("")
                        self.ui.txtSentForRepairStatus.setCurrentText("")
                        self.ui.txtRepairLaptopID.setText("")
                        self.ui.txtSSRSerial.setText("")
                        self.ui.txtSSRStatus.setCurrentText("")
                        self.ui.txtSSUSerial.setText("")
                        self.ui.txtSSUSpare.setText("")
                        
                        from inuseInventory import InuseInvFunctions as iu
                        iu.displayInuseTable(self,iu.getAllInuseItems(self))
                        RepairsRecord.displayRepairsLaptopTable(self,RepairsRecord.getAllLaptops(self))
                        from serverInventory import LaptopInventoryFunctions as li
                        li.displayLaptopTable(self,li.getAllLaptops(self))


                    else:
                        QMessageBox.information(self, "Failed", "Laptop couldnt be delete from the records")
                else:
                    QMessageBox.information(self, "Failed", "Laptop couldnt be sent to Server Room")
            else:
                QMessageBox.information(self, "Failed", "Laptop couldnt updated to Inuse Inventory Records")
        else:
            QMessageBox.warning(self, "Required", "Please Select item from Record")
          

    def returnGenerateCSV(self):
        try:
            msg = QMessageBox()
            path, _filter = QFileDialog.getSaveFileName(self, 'Save File',QDir.homePath()+"/ymca_RepairRecords.xlsx","CSV_FILES(*.xlsx *.csv)")
            columnHeaders = []
            for j in range(self.ui.RepairsRecordTable.model().columnCount()):
                columnHeaders.append(self.ui.RepairsRecordTable.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.RepairsRecordTable.rowCount()):
                for col in range(self.ui.RepairsRecordTable.columnCount()):
                    df.at[row,columnHeaders[col]]=self.ui.RepairsRecordTable.item(row, col).text()

            df.to_excel(path,index = False)
            QMessageBox.information(self, "File Saved", f"Excel File Exported to: '{path}'")
        except Exception:
            QMessageBox.warning(self, "Cancel Event", "Cancelled by User")
          
    def displayRepairsLaptopTable(self,rows):
        if rows is not None: 
            conn = connections.conndb()
            strsql = "SELECT * FROM repairsrecord"
            result = conn.queryResult(strsql)
            row = 0
            self.ui.RepairsRecordTable.setRowCount(len(result))
            self.ui.RepairsRecordTable.setSortingEnabled(True)
            for repairlaptops in result:
                self.ui.RepairsRecordTable.setItem(row,0,QtWidgets.QTableWidgetItem(str(repairlaptops[0])))
                self.ui.RepairsRecordTable.setItem(row,1,QtWidgets.QTableWidgetItem(str(repairlaptops[1])))
                self.ui.RepairsRecordTable.setItem(row,2,QtWidgets.QTableWidgetItem(str(repairlaptops[2])))
                self.ui.RepairsRecordTable.setItem(row,3,QtWidgets.QTableWidgetItem(str(repairlaptops[3])))
                self.ui.RepairsRecordTable.setItem(row,4,QtWidgets.QTableWidgetItem(str(repairlaptops[4])))
                self.ui.RepairsRecordTable.setItem(row,5,QtWidgets.QTableWidgetItem(str(repairlaptops[5])))
                self.ui.RepairsRecordTable.setItem(row,6,QtWidgets.QTableWidgetItem(str(repairlaptops[6])))
                self.ui.RepairsRecordTable.setItem(row,7,QtWidgets.QTableWidgetItem(str(repairlaptops[7])))
                self.ui.RepairsRecordTable.setItem(row,8,QtWidgets.QTableWidgetItem(str(repairlaptops[8])))
                self.ui.RepairsRecordTable.setItem(row,9,QtWidgets.QTableWidgetItem(str(repairlaptops[9])))
                row = row + 1
        else:
            print("No Data Found")

