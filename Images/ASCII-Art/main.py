import cv2
import math
from colorama import Fore


def file_data(filename: str) -> list[tuple[int, int], list[list[tuple[int, int, int]]]]:

    f = cv2.imread(filename, cv2.IMREAD_COLOR)
    data = []
    for x in f:
        data.append([])
        for y in x:
            data[-1].append(tuple(y))
    return [(len(f[0]), len(f)), data]


def rgb_to_grayscale(rgb: list[int, int, int] or tuple[int, int, int]) -> float:
    return (0.21 * rgb[0]) + (0.72 * rgb[1]) + (0.07 * rgb[2])


(dim_x, dim_y), pixels = file_data(input("File name (e.g. test_img.png): "))
print("Image is", dim_x, "x", dim_y, "px", Fore.GREEN)
grayscale_list = []
for a in pixels:
    grayscale_list.append([])
    for b in a:
        grayscale_list[-1].append(rgb_to_grayscale(b))

img = open("image.txt", "w+")

ascii_darkness = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
for c in grayscale_list:
    for d in c:
        print(ascii_darkness[math.floor(d / (255 / 64))], end="")
        img.write(ascii_darkness[math.floor(d / (255 / 64))])
    print("")
    img.write("\n")

print(Fore.WHITE)
