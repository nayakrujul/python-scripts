import cv2
import PIL.Image
import numpy


def invert(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new[-1].append(list(reversed(y)))
    cv2.imwrite(f'{name.split(".")[0]}_inverted.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_inverted.{name.split(".")[1]}').show()


def darken(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new_y = [y[0] - 50, y[1] - 50, y[2] - 50]
            new[-1].append(new_y)
    cv2.imwrite(f'{name.split(".")[0]}_darkened.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_darkened.{name.split(".")[1]}').show()


def lighten(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new_y = [y[0] + 50, y[1] + 50, y[2] + 50]
            new[-1].append(new_y)
    cv2.imwrite(f'{name.split(".")[0]}_lightened.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_lightened.{name.split(".")[1]}').show()


def boost_r(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new_y = [y[0] - 50, y[1] - 50, y[2] + 100]
            new[-1].append(new_y)
    cv2.imwrite(f'{name.split(".")[0]}_red-boosted.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_red-boosted.{name.split(".")[1]}').show()


def boost_g(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new_y = [y[0] - 50, y[1] + 100, y[2] - 50]
            new[-1].append(new_y)
    cv2.imwrite(f'{name.split(".")[0]}_green-boosted.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_green-boosted.{name.split(".")[1]}').show()


def boost_b(data, name):

    new = []
    for x in data:
        new.append([])
        for y in x:
            new_y = [y[0] + 100, y[1] - 50, y[2] - 50]
            new[-1].append(new_y)
    cv2.imwrite(f'{name.split(".")[0]}_blue-boosted.{name.split(".")[1]}', numpy.array(new))
    PIL.Image.open(f'{name.split(".")[0]}_blue-boosted.{name.split(".")[1]}').show()


filename = input("Filename: ")
option = input("""Select option:
  [1] Invert to BGR
  [2] Darken image
  [3] Lighten image
  [4] Boost Red
  [5] Boost Green
  [6] Boost Blue
      > """
               )

image = cv2.imread(filename, cv2.IMREAD_COLOR)

if option == "1":
    invert(image, filename)
if option == "2":
    darken(image, filename)
if option == "3":
    lighten(image, filename)
if option == "4":
    boost_r(image, filename)
if option == "5":
    boost_g(image, filename)
if option == "6":
    boost_b(image, filename)
