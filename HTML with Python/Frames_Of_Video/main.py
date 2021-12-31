import cv2
import os
import arrow
import shutil
import webbrowser

name = input("Video name (e.g. my_vid.mp4): ")

vid = cv2.VideoCapture(name)
success, image = vid.read()

count = 1
prefix = name.split(".")[0].replace(" ", "_") + arrow.utcnow().format("__YYYY-MM-DD_HH:mm:ss")

while success:
    cv2.imwrite(prefix + f"__frame_{count}.jpg", image)
    success, image = vid.read()
    os.system('clear')
    print("Frames completed:", count)
    count += 1

path_to_files = os.getcwd()
new_path = os.path.join(path_to_files, prefix) + "/"
os.mkdir(new_path)
for filename in os.listdir(path_to_files):
    if prefix in filename and prefix != filename:
        path_to_file = os.path.join(path_to_files, filename)
        shutil.move(path_to_file, new_path + filename)

os.system('clear')
num = input("Open frame ")

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{'frame_' + str(num)}</title>
</head>
<body>
    <img id='img' src='{new_path + prefix + '__frame_' + str(num) + '.jpg'}' width=1500>
    <br />
    <label for='width'>Width:</label>
    <input type='number' value=1500 id='width' onkeyup='javascript:resize_w();' />
    <br />
    <label for='height'>Height:</label>
    <input type='number' value=1000 id='height' onkeyup='javascript:resize_h();' />
    <script src='script.js'></script>
</body>
</html>
"""

f = open('index.html', 'w')
f.write(html_template)
f.close()

webbrowser.open("file://" + os.path.join(os.getcwd(), "index.html"))
