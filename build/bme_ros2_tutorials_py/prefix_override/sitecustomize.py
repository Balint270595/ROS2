import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/balint/ros2_ws/install/bme_ros2_tutorials_py'
