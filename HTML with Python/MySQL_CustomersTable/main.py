import mysql.connector
import arrow
import webbrowser
import os

mydb = mysql.connector.connect(
    host="127.0.0.1",
    password="password",
    port="3306",
    user="root",
    database="mydatabase"
)

my_cursor = mydb.cursor()

insert = input("Insert row in table (Y/N)? ").lower()

if "y" in insert:

    val = (input('Name: '), input('Address: '))
    my_cursor.execute(
        "INSERT INTO customers (name, address) VALUES (%s, %s)", val
    )
    mydb.commit()


order = input("Order by (name, address, id): ").lower()

if order not in ["name", "address", "id"]:
    order = "id"

sql = f"SELECT * FROM customers ORDER BY {order}"

my_cursor.execute(sql)

my_result = my_cursor.fetchall()

html_file = open('table.html', 'w+')

html_template = f"""
<html>
<head>
    <title>customers: {arrow.now().format("YYYY/MM/DD HH:mm")}</title>
</head>
<body>
    <h1>table: customers</h1>
    <h4>Last refreshed: {arrow.now().format("HH:mm:ss")}</h4>
    <table border='1px solid black' id='table'>
        <tr>
            <th>name</th>
            <th>address</th>
            <th>id</th>
        </tr>

"""

for row in my_result:

    html_template += f"        <tr>\n" \
                     f"            <td>{row[0]}</td>\n" \
                     f"            <td>{row[1]}</td>\n" \
                     f"            <td>{row[2]}</td>\n" \
                     f"        </tr>\n"

html_template += "    </table>\n" \
                 "    <br />\n" \
                 "    <input type='text' id='colour' value='colour' />\n" \
                 "    <input type='button' value='switch' onclick='javascript:recolour();' />\n" \
                 "    <script src='script.js'></script>\n" \
                 "</body>\n" \
                 "</html>"

html_file.write(html_template)

html_file.close()

if not webbrowser.get('chrome').open('file://' + os.getcwd() + '/table.html', new=1):
    print("An error occurred. Try again later.")
