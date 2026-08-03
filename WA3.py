from microbit import *
display.off()
#=====config=====
#perpendicular_normal(x, y, -1056)
#perpendicular_front(x, -972, z)
#perpendicular_back(x, 988, z)
#perpendicular_right(1000, y, z)
#perpendicular_left(-1016, y, z)

#range_x -250<=x<=250
#range_y -250<=y<=250

#================

#=======def=======
def coordinate_degree(n):
    #by mean, parameter = 1006.4
    return n/1006.4*90
def balance_front():
    pin1.write_analog(abs(coordinate_degree(y)))
    print('balance_front')
def balance_back():
    pin2.write_analog(coordinate_degree(y))
    print('balance_back')
def balance_right():
    pin10.write_analog(coordinate_degree(x))
    print('balance_right')
def balance_left():
    pin13.write_analog(abs(coordinate_degree(x)))
    print('balance_left')
#=================

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print (x, y, z)

    if not -250<=y<=250:
        if y>=0:
            balance_back()
        else:
            balance_front()
    if not -300<=x<=300:
        if x>=0:
            balance_right()
        else:
            balance_left()
            
