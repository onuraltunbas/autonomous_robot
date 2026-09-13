import os
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController

def generate_launch_description():
    package_dir = get_package_share_directory('my_robot_pkg')
    robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')
    rviz_config_path = os.path.join(package_dir, 'rviz', 'robot_view.rviz')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'house_world.wbt')
    )

    my_robot_driver = WebotsController(
        robot_name='robot',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )

    sonar_to_scan_node = Node(
        package='my_robot_pkg',
        executable='sonar_to_scan',
        name='sonar_to_scan',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen'
    )

    return LaunchDescription([
        webots,
        my_robot_driver,
        sonar_to_scan_node,
        rviz_node,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
