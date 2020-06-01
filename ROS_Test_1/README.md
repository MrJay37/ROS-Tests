# ROS TEST 1
## Aim: Picking up an object from one position and putting it down in another position

This is the first ROS test I conducted. In this test, there are two stages involved. Before running the code, the ROS MASTER needs to be on. This can be done by launching the interbotix_sdk launch file. 
```
$ roslaunch interbotix_sdk arm_run.launch robot_name:=rx150s use_time_based_profile:=true gripper_operating_mode:=pwm
```

1. First was finding the positions for the arm to go to. This was done by the get_joint_data.py code. To use this code, you need to first call the ROS service /{arm_name}/torque_joints_off. 
    ```
    $ rosservice call /rx150/torque_joints_off
    ```
    This will allow you to move the arm freely to the point where you want it to go to. After taking the arm there, while holding it in that position, call the service /{arm_name]/torque_joints_on.
    ```
    $ rosservice call /rx150/torque_joints_on
    ```
    Then execute the get_joint_data.py
    ```
    $ python get_joint_data.py
    ```
    This will give you an array of 8 values which include the joint values of the robot arm's correspoding joint names:
    ```
    [waist, shoulder, elbow, wrist_angle, wrist_rotate, gripper, left_finger, right_finger]
    ```
    You only need the first five values. Copy these values  and the turn the torques off again. Take the arm back to the sleep position (or repeat the procedure if you have other positions to record). Do not forget to call the serve torque_joints_on again otherwise the next code won't execute.
    
2. After you have recorded the positions, store these positions in an array in the joint_position_control.py code. In the given code, there are 5 positions recorded. In the main() function, the set_joint_position(arr) is called 5 times. So in the course of the demonstration, there are 5 custom positions to go to. You can include more positions as you desire. The structure of the main() code will have to change in order to execute your desired path. Then execute the code.
    ```
    $ python joint_position_control.py
    ```
    
There is another code included in the folder called log_joint_data.py. This code is to check the values of the joints in the arm in real-time. The above mentioned 8-values array is logged at a rate of 0.1 second. This code is to study the possible values of the arm in all possible positions.
