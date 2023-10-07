import signal
from xbox360controller import Xbox360Controller
import pyfirmata
import time

def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, int(axis.x), int(axis.y)))
    if int(axis.x) == -1 and int(axis.y) == 1:
        board.digital[mypins[0]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == -1 and int(axis.y) == 0:
        board.digital[mypins[1]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == -1 and int(axis.y) == -1:
        board.digital[mypins[2]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == 0 and int(axis.y) == -1:
        board.digital[mypins[3]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == 1 and int(axis.y) == -1:
        board.digital[mypins[4]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == 1 and int(axis.y) == 0:
        board.digital[mypins[5]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == 1 and int(axis.y) == 1:
        board.digital[mypins[6]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)

    elif int(axis.x) == 0 and int(axis.y) == 1:
        board.digital[mypins[7]].write(1)
        time.sleep(0.005)
        for i in range(0, 8):
            board.digital[mypins[i]].write(0)      
            
        


board = pyfirmata.Arduino('/dev/ttyACM0')
mypins= [2,3,4,5,6,7,8,9]

for i in range(0, 8):

        board.digital[mypins[i]].mode = pyfirmata.OUTPUT


while True:


    try:
        with Xbox360Controller(0, axis_threshold=0.3) as controller:
        
            controller.axis_r.when_moved = on_axis_moved
                


            signal.pause()
    except KeyboardInterrupt:
        pass