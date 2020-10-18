from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import rospy

import sys
import os

from pynput.keyboard import Key, Listener

from time import sleep

# joint_names: [waist, shoulder, elbow, wrist_angle, wrist_rotate, gripper]
# joint_ids: [1, 2, 3, 4, 5, 6]
# lower_joint_limits: [-3.14159265359, -1.85004900711, -1.65806278939, -2.14675497995, -3.14159265359, 0.0]
# upper_joint_limits: [3.14159265359, 1.74532925199, 1.78023583703, 1.74532925199, 3.14159265359, 0.0]
# velocity_limits: [3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359]
# lower_gripper_limit: 0.015
# upper_gripper_limit: 0.037
# use_gripper: True
# home_pos: [0.0, 0.0, 0.0, 0.0, 0.0]
# sleep_pos: [0.0, -1.8, -1.55, -0.8, 0.0]
# num_joints: 5
# num_single_joints: 6

# This script commands some arbitrary positions to the arm joints
#
# To get started, open a terminal and type 'roslaunch interbotix_sdk arm_run.launch robot_name:=wx250s use_time_based_profile:=true gripper_operating_mode:=pwm'
# Then change to this directory and type 'python joint_position_control.py'



movingTime = 2000.0
accelTime= 600.0
arm = InterbotixRobot(robot_name="rx150", mrd=mrd, moving_time=movingTime, accel_time=accelTime, gripper_pressure=1, use_time=False)

arm.go_to_home_pose()
rospy.sleep(movingTime/1000)
dest = arm.get_joint_positions()


waist = dest[0]
shoulder= dest[1]
elbow = dest[2]
wrist_angle = dest[3]
wrist_rotate = dest[4]
gripper = True

def arrCmp(arr1, arr2):
    print('going')
    for i in range(len(arr1)):
        if(arr1[i] != arr2[i]):
            if((arr1[i] - arr2[i]) <= 0.01):
                pass
            else:
                return False
    return True

def goToPose(djp):
    '''
    cjp = []
    jp = arm.get_joint_positions()
    for i in range(len(jp)) :
        cjp.append(round(jp[i], 20))
    
    while(arrCmp(djp, cjp) == False):
        for i in range(len(cjp)):
            if(cjp[7-i] < djp[7-i]):
                cjp[7-i] = cjp[7-i] + 0.01
            elif(cjp[7-i] > djp[7-i]):
                cjp[7-i] = cjp[7-i] - 0.01
            else:
                pass
                '''
    arm.set_joint_positions(djp)
    arm.open_gripper()
    rospy.sleep(movingTime/1000)

def onChangePose(going, delay):
    arm.set_joint_positions(going)
    rospy.sleep(delay)

def goToHome():
    arm.go_to_home_pose()
    arm.close_gripper()
    rospy.sleep(movingTime/1000)

def goToSleep():
    arm.go_to_sleep_pose()
    arm.close_gripper()
    rospy.sleep(movingTime/1000)
    

def on_press(key):
    # print(key)
    global waist, shoulder, elbow, wrist_angle, wrist_rotate, gripper

    if(key == Key.shift):
        if(elbow <= 1.6):
            elbow = elbow + 0.1

    elif(key == Key.ctrl):
        if(elbow > -1.7):
            elbow = elbow - 0.1

    elif(key == Key.backspace):
        if(wrist_angle <= 1.6 ):
            wrist_angle = wrist_angle + 0.1

    elif(key == Key.enter):
        if(wrist_angle >= -2.0 ):
            wrist_angle = wrist_angle - 0.1
    
    elif(key == Key.down):
        if(shoulder <= 1.6):
            shoulder = shoulder + 0.1

    elif(key == Key.up):
        if(shoulder > -1.60):
            shoulder = shoulder - 0.1

    elif(key == Key.right):
        if(waist <= 3.04):
            waist = waist + 0.05
            
    elif(key == Key.left):
        if(waist >= -3.04):
            waist = waist - 0.05

    elif(key == Key.space):

        if(gripper):
            arm.open_gripper()
            rospy.sleep(movingTime/1000)
            gripper = False
            return

        else:
            arm.close_gripper()
            rospy.sleep(movingTime/1000)
            gripper = True
            return
            
            
    elif(key == Key.esc):
        goToSleep()
        listener.stop()
        dest = [waist, shoulder, elbow, wrist_angle, wrist_rotate]
        print(dest)
	os._exit(1)

    
    dest = [waist, shoulder, elbow, wrist_angle, wrist_rotate]
    print(dest)
    onChangePose(dest, 0.01)
	    
def on_unpress(key):
    #print('Unpressed')
    pass
listener = Listener(on_press=on_press, on_release=on_unpress, suppress=True)
listener.start()



def main():
    pass


# lower_joint_limits: [-3.14159265359, -1.85004900711, -1.65806278939, -2.14675497995, -3.14159265359, 0.0]
# upper_joint_limits: [3.14159265359, 1.74532925199, 1.78023583703, 1.74532925199, 3.14159265359, 0.0]
# velocity_limits: [3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359, 3.14159265359]

if __name__=='__main__':
    while True :
        try:
            main()
        except KeyboardInterrupt:
            listener.stop()
            break
