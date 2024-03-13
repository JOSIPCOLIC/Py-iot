from sense_emu import SenseHat
import time

hat = SenseHat()

hat.clear
hat.set_pixel(0, 2, [0, 255, 0])
hat.set_pixel(0, 1, [255, 0, 0])

hat.clear()
r = [255, 0, 0] #red
g = [0, 255, 0] #green
b = [0, 0, 255] #blue
w = [255, 255, 255] #white
black = [0, 0, 0] #black

time.sleep(1)
flag = [
    g, g, g, g, g, g, g, g, 
    black, r, r, r, r, r, r, black,
    black, r, r, r, r, r, r, black,
    black, w, w, w, w, w, w, black,
    black, w, w, w, w, w, w, black,
    black, b, b, b, b, b, b, black,
    black, b, b, b, b, b, b, black,
    black, g, g, g, g, g, g, black,
]

hat.set_pixels(pixel_list = flag)
time.sleep(1)

