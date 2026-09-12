import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/onur/autonomous_robot/install/webots_ros2_tesla'
