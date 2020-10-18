import rospy
from sensor_msgs.msg import JointState

def callback(data):
	rospy.loginfo(data)

def listener():
	rospy.init_node('JointStateListenerNode')
	rospy.Subscriber("/rx150/joint/commands", JointState, callback)
	rospy.spin()
	rospy.sleep(1)

while(True):
	listener()
	rospy.sleep(1)
