# author Yikang Cheng 
# yikangc@andrew.cmu.edu
# Trajectory Motion

import os
import sys
import time
import pickle

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

filename = "Saved_trajectory/trial1.pkl"
ip = input('Please input the xArm ip address:')

arm = XArmAPI(ip)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

print(arm.get_position)

result = []
openfile = open(filename,"rb")
result = pickle.load(openfile)
openfile.close()

for j in range (len(result)):
    # print(result[j])
    a,b=result[j]
    x1,y1,z1,roll1,pitch1,yaw1 = b
    # print("\n\n\n\n")
    # print("x: ",x1)
    # print("y: ",y1)
    # print("z: ",z1)
    # print("roll: ",roll1)
    # print("pitch: ",pitch1)
    # print("yaw: ",yaw1)
    arm.set_position(x=x1, y=y1, z=z1, roll=roll1, pitch=pitch1, yaw=yaw1, speed=600, wait=True)


arm.reset(wait=True)
arm.disconnect()
