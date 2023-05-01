import os
import sys
import connections
from Custom_Widgets.Widgets import *
from interface_ui import *
from PySide2.QtWidgets import QTableWidgetItem

# Import the necessary classes
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import Qt


class HomeDashBoardFunctions():
    def __init__(self,arg):
        super(HomeDashBoardFunctions,self).__init__()
        self.arg = arg
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

    def getServerCount(self):
        conn = connections.conndb()
        get_laptop_data =  """SELECT COUNT(DISTINCT LaptopSerial) FROM laptopinventory"""
        try:
            c = conn.queryResult(get_laptop_data)
            count = str(c[0][0])
            return count
        except Exception as e:
            print("Couldnt get all Laptops")

    def getEquipmentCount(self):
        conn = connections.conndb()
        get_equip_data =  """SELECT SUM(equipItemCount) FROM equipmentsrecord"""
        try:
            c = conn.queryResult(get_equip_data)
            count = int(c[0][0])
            return count
        except Exception as e:
            print("Couldnt get all Equipments")

    def getRepairsCount(self):
        conn = connections.conndb()
        get_repairs_data =  """SELECT COUNT(DISTINCT RepairLaptopSerial) FROM repairsrecord"""
        try:
            c = conn.queryResult(get_repairs_data)
            count = str(c[0][0])
            return count
        except Exception as e:
            print("Couldnt get all Repairs Data")
    
    def getInuseCount(self):
        conn = connections.conndb()
        get_inuse_data =  """SELECT COUNT(DISTINCT LaptopSerial) FROM inuseinventory"""
        try:
            c = conn.queryResult(get_inuse_data)
            count = str(c[0][0])
            return count
        except Exception as e:
            print("Couldnt get all In-Use Data")
    