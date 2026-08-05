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
def balance1_y():
    pin1.write_analog(90+coordinate_degree(y))
def balance2_y():
    pin2.write_analog(90-coordinate_degree(y))
    
#=================

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print (x, y, z)

    if (-90<=coordinate_degree(y)) and (90>=coordinate_degree(y)):
        balance1_y()
        balance2_y()
        
