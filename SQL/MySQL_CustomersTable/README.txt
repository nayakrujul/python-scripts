MySQL Customers Table


Setting up the MySQL Server

For this program to work, you need a MySQL server. To set this up:
1. Go to https://dev.mysql.com/downloads/
2. Download both 'MySQL Community Server' and 'Connector/Python'
3. Type in the password 'password' when prompted
4. Run the setup.py file once to create the database and table.


This project allows the user to add to a table (customers) in a database
and also shows the table in a HTML file. The HTML file also lets the user
change the background colour of the table. Just run the main.py file, then
if you don't want to change anything press N. If you do want to add a row
in the table, press Y and enter the details. Then, enter the sorting column
(name, address, or ID) and the program will open the file in a new tab in
Chrome. You can enter a colour in the text input box as the name (e.g.
'red', 'blue', 'yellowgreen') or as '#' followed by the hex code (e.g.
'#FF0000', '#0000FF', '#9ACD32'), then press 'switch' to change the
background colour of the table.


Python version:
 - 3.6+ (written in 3.9.9)

PIP installations required:
 - MySQL-Connector
 - Arrow

Other requirements:
 - Google Chrome


January 2022
www.github.com/nayakrujul/python-scripts
