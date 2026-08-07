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
    return n/1000*90
def balance_y():
    pin1.write_analog(90+coordinate_degree(y))
    pin2.write_analog(90-coordinate_degree(y))
def balance_x():
    pin10.write_analog(90+coordinate_degree(x))
    pin13.write_analog(90-coordinate_degree(x))
def acc(lst):
    return (lst[2]-lst[1])/(lst[1]-lst[0])
#================= 

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print (x, y, z)
    sleep(1000)
        
    if (-22.5<=coordinate_degree(y)) and (22.5>=coordinate_degree(y)):
        balance_y()
    if (-45<=coordinate_degree(x)) and (45>=coordinate_degree(x)):
        balance_x()
