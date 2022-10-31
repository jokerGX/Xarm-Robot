#author Yikang Cheng 
#yikangc@andrew.cmu.edu

import os
import sys
import time
import pickle

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI
filename = "Saved_trajectory/trial1.pkl"

ip = input("input ip address")


arm = XArmAPI(ip, is_radian=False)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)


# Turn on manual mode before recording
arm.set_mode(2)
arm.set_state(0)

# Analog recording process, here with delay instead
storing = []
i = 0
while i<5:
    storing.append(arm.get_position())
    print(arm.get_position())
    i+=0.1
    time.sleep(0.1)

    
openfile = open(filename,"wb")
pickle.dump(storing,openfile)
openfile.close()

time.sleep(1)

result = []
openfile = open(filename,"rb")
result = pickle.load(openfile)
openfile.close()

for j in range (len(result)):
    print(result[j])
    time.sleep(0.01)

# Turn off manual mode after recording
arm.set_mode(0)
arm.set_state(0)
