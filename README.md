# Frosty-Inv-Management
<p align="center">
  <img src="https://raw.githubusercontent.com/GM-Frost/Frosty-Inv-Management/master/Images/App-Logo-Main.png" width="350" title="hover text">
  <img src="https://raw.githubusercontent.com/GM-Frost/Frosty-Inv-Management/master/Images/App-Icon.png" width="350" alt="accessibility text">
</p>

# 🔗 Setup File 
currently being uploaded

# Background
Frosty Inventory Management Project was initially built as a side project for a multinational motor company and is currently being used by their IT Service department to keep track of their inventory. 
Note that some logos and functionalities have been changed.

The application allows users to stock a laptop with its unique serial key and assign it to an employee along with other equipment.
The equipment records act as stock that follows a count of items. When an onboarding request is assigned, following up with the laptop being provided, equipment stocks get deducted and the application keeps track of the remaining stock in the inventory. 
The application also has the functionality of managing repair stocks, where all the repaired laptops are stocked and presented with their status.

# Functionality

**Stock management:** Keep track of inventory of laptops and other equipment.
**On-boarding and off-boarding request:** Assign laptops and equipment to employees and keep track of their status.
**Equipment stocks:** Keep track of the remaining stock of equipment in the inventory.
**Search features:** Search for laptops and equipment by serial key or other attributes.
**Convert SQL database to CSV (excel) file:** Export the inventory data as a CSV file for further analysis.
**Admin dashboard:** View and manage the inventory data in a user-friendly dashboard.

# PIP List

The following Python packages are required to run the application:

custom_widgets
PyQt5
session
datetime
PySide2
CairoSVG
Cairocffi
Pandas
iconify
et-xmlfile
mysql.connector

# Getting Started
1) Clone the repository:
git https://github.com/GM-Frost/Frosty-Inv-Management.git

2) Download SQL
upload the Databasefiles provided.
Current Database Info: user=nayan,password=Admin123,host=localhost,database=nayan_inventory_management

3) Install the required packages

4) Run the Application
python main.py

# License
This project is licensed under the MIT License - see the <a href="https://nayanbastola.com/wp-content/uploads/2023/05/license.txt" target="_blank">LICENSE file</a>  for details.
