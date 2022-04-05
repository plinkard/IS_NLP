from unicornhatmini import UnicornHATMini
import time

uh = UnicornHATMini()

uh.set_brightness(0.5)

#top left pixel is 0, 0 and the bottom right pixel is 16, 6

#lights top pixel red
uh.set_pixel(0, 0, 255, 0, 0)
uh.show()
#####

#clears screen
uh.clear()
uh.show()
#####


#makes the full thing show up cyan
for x in range(17):
    for y in range(7):
        uh.set_pixel(x, y, 0, 255, 255)
uh.show()
#####
