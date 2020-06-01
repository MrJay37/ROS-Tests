from interbotix_sdk.robot_manipulation import InterbotixRobot
from interbotix_descriptions import interbotix_mr_descriptions as mrd

jp = [[0.653475821018219, 0.3221359848976135, 0.4693981409072876, -1.653631329536438, -0.006135923322290182],
      [0.6718835830688477, 0.2485048919916153, 0.1564660519361496, -1.4296700954437256, -0.015339808538556099],
      [-2.9421751499176025, 0.7501166462898254, 0.6289321184158325, -0.951068103313446, 0.08897088468074799],
      [-2.9866607189178467, 0.11504856497049332, 0.882038950920105, -1.3222914934158325, 0.08743690699338913],
      [-0.026077674701809883, -1.7594760656356812, -1.6290876865386963, -0.7915341258049011, 0.006135923322290182]]

def main():
    arm = InterbotixRobot(robot_name="rx150", mrd=mrd)
    arm.go_to_home_pose()

    arm.set_joint_positions(jp[0])
    arm.set_gripper_pressure(1.0)
    arm.open_gripper()

    arm.set_joint_positions(jp[1])
    arm.close_gripper()

    arm.go_to_home_pose()

    arm.set_joint_positions(jp[2])
    arm.open_gripper()
    arm.set_joint_positions(jp[3])
    arm.close_gripper()

    arm.go_to_home_pose()
    arm.set_joint_positions(jp[4])

if __name__=='__main__':
    main()
