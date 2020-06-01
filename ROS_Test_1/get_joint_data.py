from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd
import sys
from time import sleep

# This script commands some arbitrary positions to the arm joints
#
# To get started, open a terminal and type 'roslaunch interbotix_sdk arm_run.launch robot_name:=wx250s use_time_based_profile:=true gripper_operating_mode:=pwm'
# Then change to this directory and type 'python joint_position_control.py'

def main():
    arm = InterbotixRobot(robot_name="rx150", mrd=mrd)
    print arm.get_joint_positions()
    
if __name__=='__main__':
    main()


