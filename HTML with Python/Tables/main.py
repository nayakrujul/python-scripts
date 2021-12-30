# Read 'README.txt' for more info.

import webbrowser
import os

try:
    webbrowser.open('file://' + os.getcwd() + '/index.html')
except:
    print("Unable to open file.")
