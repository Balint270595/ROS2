import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable, IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution, PathJoinSubstitution, Command
from launch_ros.actions import Node


def generate_launch_description():
    # Directories
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    pkg_turtlebot3_description = get_package_share_directory('turtlebot3_description')

    # Config
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_file = LaunchConfiguration('world', default='empty.sdf')

    # Set Gazebo resource path
    set_env_vars_resources = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        os.path.join(pkg_turtlebot3_gazebo, 'models')
    )

    # Launch Gazebo
    gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': [PathJoinSubstitution([
                pkg_turtlebot3_gazebo,
                'worlds',
                world_file
            ]),
            TextSubstitution(text=' -r -v -v1')],
            'on_exit_shutdown': 'true'
        }.items()
    )

    # URDF description (same for both robots)
    urdf_file = os.path.join(pkg_turtlebot3_description, 'urdf', 'turtlebot3_burger.urdf.xacro')
    robot_description = Command(['xacro ', urdf_file])

    # === Robot 1 ===
    tb3_1 = GroupAction([
        # State publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace='tb3_1',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_description
            }],
            output='screen'
        ),
        # Spawner
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(launch_file_dir, 'spawn_multiple_tb3.launch.py')
            ),
            launch_arguments={
                'x_pose': TextSubstitution(text='0.0'),
                'y_pose': TextSubstitution(text='0.0'),
                'robot_namespace': TextSubstitution(text='tb3_1'),
                'robot_name': TextSubstitution(text='tb3_1')
            }.items()
        )
    ])

    # === Robot 2 ===
    tb3_2 = GroupAction([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace='tb3_2',
            parameters=[{
                'use_sim_time': use_sim_time,
                'robot_description': robot_description
            }],
            output='screen'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(launch_file_dir, 'spawn_multiple_tb3.launch.py')
            ),
            launch_arguments={
                'x_pose': TextSubstitution(text='2.0'),
                'y_pose': TextSubstitution(text='0.0'),
                'robot_namespace': TextSubstitution(text='tb3_2'),
                'robot_name': TextSubstitution(text='tb3_2')
            }.items()
        )
    ])

    # Assemble launch description
    ld = LaunchDescription()
    ld.add_action(set_env_vars_resources)
    ld.add_action(gazebo_cmd)
    ld.add_action(tb3_1)
    ld.add_action(tb3_2)

    return ld
