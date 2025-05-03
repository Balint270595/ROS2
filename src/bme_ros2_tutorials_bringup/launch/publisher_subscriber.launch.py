from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    publisher_node = Node(
        package="bme_ros2_tutorials_py",
        executable="py_publisher",
        name="my_publisher",
    )

    subscriber_node = Node(
        package="bme_ros2_tutorials_py",
        executable="py_subscriber",
        name="my_subscriber",
    )

    ld.add_action(publisher_node)
    ld.add_action(subscriber_node)
    return ld