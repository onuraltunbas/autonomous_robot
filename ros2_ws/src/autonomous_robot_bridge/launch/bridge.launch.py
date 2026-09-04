from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    desc_pkg_share = FindPackageShare('autonomous_robot_description')
    bridge_pkg_share = FindPackageShare('autonomous_robot_bridge')

    with open('/home/onur/autonomous_robot/ros2_ws/src/autonomous_robot_description/urdf/robot.urdf', 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([
        # 1. Robot State Publisher (TF Tree for robot links)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),

        # 2. Joint State Publisher
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),

        # 3. Unreal - ROS 2 Bridge Node
        Node(
            package='autonomous_robot_bridge',
            executable='bridge_node',
            name='unreal_ros_bridge',
            output='screen',
            parameters=[{
                'host': '127.0.0.1',
                'port': 9876
            }]
        )
    ])
