from pynput.mouse import Listener
from time import sleep
from threading import Thread
from os import system


clicks = 0

try:
    starting = int(input("Seconds: "))
except ValueError:
    starting = 15
counter = starting

# last_move = (-1, -1)
# moved = 0


def timer():

    global counter
    while counter > 0:
        sleep(0.1)
        counter -= 0.1
        system('clear')
        print(round(counter + 0.1, 1), "seconds left |", clicks, "clicks")

    print("\nCLICK FOR RESULTS")


def on_move(x, y):
    # global last_move, moved
    # if last_move != (-1, -1):
    #     moved += abs(last_move[0] - x) + abs(last_move[1] - y)
    # last_move = x, y
    if counter <= 0:
        return False


def on_click(x, y, button, pressed):
    global clicks
    if pressed and counter > 0:
        clicks += 1
    if counter <= 0:
        return False


def on_scroll(x, y, dx, dy):
    if counter <= 0:
        return False


system('clear')
print("Starting in...")
sleep(1)

system('clear')
print('3...')
sleep(1)

system('clear')
print('2...')
sleep(1)

system('clear')
print('1...')
sleep(1)


my_thread = Thread(target=timer)
my_thread.start()


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
system('clear')
print(f"You got {clicks} clicks in {starting} seconds",
      f"({round(clicks / starting, 1)} clicks per second).")
# print(f"Your mouse moved {int(round(moved, 0))}",
#       f"pixels in {starting} seconds",
#       f"({round(moved / starting, 1)} pixels per second).")
