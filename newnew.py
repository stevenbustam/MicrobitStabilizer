from microbit import *
display.off()

last_log_time = running_time()  # Record the initial time
log_interval = 250

#=====storage=====
storage_x = []
storage_y = []
storage_z = []
#=================

#=======def=======
def coordinate_degree(n):
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
    current_time = running_time()

    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print (x, y, z)
    
    if current_time - last_log_time >= log_interval:
        if len(storage_z) < 3:
            storage_z += [z]
        else:
            storage_z = storage_z[1:] + [z]
        print (storage_z)
        last_blink_time = current_time  # Update the timer
    if acc(storage_z)>=4:
        print ('stabilizing')
    if (-22.5<=coordinate_degree(y)) and (22.5>=coordinate_degree(y)):
        balance_y()
    if (-45<=coordinate_degree(x)) and (45>=coordinate_degree(x)):
        balance_x()
