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
    
    # Kaydedilen Harita Dosyası
    map_yaml_file = os.path.join(package_dir, 'maps', 'house_map.yaml')

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

    # 3. 4 Sonar -> Sanal LaserScan
    sonar_to_scan_node = Node(
        package='my_robot_pkg',
        executable='sonar_to_scan',
        name='sonar_to_scan',
        output='screen'
    )

    # 4. Kayıtlı Haritayı Yükleyen Map Server
    map_server_node = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[
            {'yaml_filename': map_yaml_file},
            {'use_sim_time': False}
        ]
    )

    # 5. Map Server Yaşam Döngüsü Yöneticisi (Lifecycle Manager)
    lifecycle_manager_node = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_map',
        output='screen',
        parameters=[
            {'use_sim_time': False},
            {'autostart': True},
            {'node_names': ['map_server']}
        ]
    )

    # 6. RViz2
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
        map_server_node,
        lifecycle_manager_node,
        rviz_node,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
