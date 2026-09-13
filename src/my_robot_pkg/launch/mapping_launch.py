import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController

def generate_launch_description():
    package_dir = get_package_share_directory('my_robot_pkg')
    robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')
    rviz_config_path = os.path.join(package_dir, 'rviz', 'robot_view.rviz')
    slam_params_file = os.path.join(package_dir, 'config', 'slam_toolbox_params.yaml')

    # 1. Webots Simülasyonu
    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'house_world.wbt')
    )

    # 2. Webots Robot Sürücüsü
    my_robot_driver = WebotsController(
        robot_name='robot',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )

    # 3. 4 Sonar -> Sanal LaserScan Dönüştürücü
    sonar_to_scan_node = Node(
        package='my_robot_pkg',
        executable='sonar_to_scan',
        name='sonar_to_scan',
        output='screen'
    )

    # 4. SLAM Toolbox (Canlı 2D Grid Haritalama)
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params_file,
            {'use_sim_time': False}
        ]
    )

    # 5. Otonom Süpürge Keşif Düğümü
    explorer_node = Node(
        package='my_robot_pkg',
        executable='explorer_node',
        name='explorer_node',
        output='screen'
    )

    # 6. RViz2 Görselleştirme Arayüzü
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
        slam_node,
        explorer_node,
        rviz_node,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
