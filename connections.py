  

import mysql.connector

class conndb:

    def __init__(self):
<<<<<<< HEAD
        self.cnx = mysql.connector.connect(user="root",password="Admin123",host="localhost",database="gmfrost_inv_mgmt")
=======
        self.cnx = mysql.connector.connect(user="nayan",password="Admin123",host="localhost",database="nayan_inventory_management")
>>>>>>> ac7233c0cd6ad81ba3b88d1377a90e0eb6048217
        self.cursor = self.cnx.cursor()
    
    def create_connection(self):
        try:
<<<<<<< HEAD
            cnx = mysql.connector.connect(user="root",password="Admin123",host="localhost",database="gmfrost_inv_mgmt")
=======
            cnx = mysql.connector.connect(user="nayan",password="Admin123",host="localhost",database="nayan_inventory_management")
>>>>>>> ac7233c0cd6ad81ba3b88d1377a90e0eb6048217
            conn = cnx.cursor()
            conn.close()
            return "Connected"
        except mysql.connector.Error:
            return "Disconnected"
        
    def queryResult(self,strsql):
        self.cursor.execute(strsql)
        result = self.cursor.fetchall()
        return result
        
    def queryExecute(self,strsql):
<<<<<<< HEAD
        cnx = mysql.connector.connect(user="root",password="Admin123",host="localhost",database="gmfrost_inv_mgmt")
=======
        cnx = mysql.connector.connect(user="nayan",password="Admin123",host="localhost",database="nayan_inventory_management")
>>>>>>> ac7233c0cd6ad81ba3b88d1377a90e0eb6048217
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()

    def queryClose(self,strsql):
<<<<<<< HEAD
        cnx = mysql.connector.connect(user="root",password="Admin123",host="localhost",database="gmfrost_inv_mgmt")
=======
        cnx = mysql.connector.connect(user="nayan",password="Admin123",host="localhost",database="nayan_inventory_management")
>>>>>>> ac7233c0cd6ad81ba3b88d1377a90e0eb6048217
        conn = cnx.cursor()
        conn.close(strsql)
         
        
 
# import pypyodbc as odbc

# class conndb:

#     def __init__(self):
#         DRIVER_NAME = 'SQL SERVER'
#         SERVER_NAME = 'nayan_inventory_management'
#         DATABASE_NAME = 'nayan_inventory_management'
#         connection_string = f"""
#                                     DRIVER={{{DRIVER_NAME}}};
#                                     SERVER={SERVER_NAME};
#                                     DATABASE={DATABASE_NAME};
#                                     Trust_Connection=yes;
#                                     """    
#         self.cnx = odbc.connect(connection_string)
#         self.cursor = self.cnx.cursor()

#     def create_connection(self):
#         try:
#             DRIVER_NAME = 'SQL SERVER'
#             SERVER_NAME = 'nayan_inventory_management'
#             DATABASE_NAME = 'nayan_inventory_management'
#             connection_string = f"""
#                                     DRIVER={{{DRIVER_NAME}}};
#                                     SERVER={SERVER_NAME};
#                                     DATABASE={DATABASE_NAME};
#                                     Trust_Connection=yes;
#                                     """    
#             cnx = odbc.connect(connection_string)
#             cnx = odbc.SQL_CLOSE
#             return "Connected"
#         except odbc.Error as ex:
#             return "Disconnected"
        
#     def queryResult(self,strsql):
#         DRIVER_NAME = 'SQL SERVER'
#         SERVER_NAME = 'nayan_inventory_management'
#         DATABASE_NAME = 'nayan_inventory_management'

#         # uid=<username>;
#         # pwd=<password>;
#         connection_string = f"""
#                                 DRIVER={{{DRIVER_NAME}}};
#                                 SERVER={SERVER_NAME};
#                                 DATABASE={DATABASE_NAME};
#                                 Trust_Connection=yes;
#                                 """
#         cnx = odbc.connect(connection_string)
#         # conn = cnx.cursor()
#         self.cursor.execute(strsql)
#         result = self.cursor.fetchall()
#         return result
        
#     def queryExecute(self,strsql):
#         DRIVER_NAME = 'SQL SERVER'
#         SERVER_NAME = 'nayan_inventory_management'
#         DATABASE_NAME = 'nayan_inventory_management'

#         # uid=<username>;
#         # pwd=<password>;
#         connection_string = f"""
#                                 DRIVER={{{DRIVER_NAME}}};
#                                 SERVER={SERVER_NAME};
#                                 DATABASE={DATABASE_NAME};
#                                 Trust_Connection=yes;
#                                 """
#         cnx = odbc.connect(connection_string)
#         conn = cnx.cursor()
#         conn.execute(strsql)
#         cnx.commit()
        

#     def queryClose(self,strsql):
#         DRIVER_NAME = 'SQL SERVER'
#         SERVER_NAME = 'nayan_inventory_management'
#         DATABASE_NAME = 'nayan_inventory_management'

#         # uid=<username>;
#         # pwd=<password>;
#         connection_string = f"""
#                                 DRIVER={{{DRIVER_NAME}}};
#                                 SERVER={SERVER_NAME};
#                                 DATABASE={DATABASE_NAME};
#                                 Trust_Connection=yes;
#                                 """
#         cnx = odbc.connect(connection_string)
#         conn = cnx.cursor()
#         conn.close(strsql)
        