from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'autonomous_robot_bridge'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Onur Altunbas',
    maintainer_email='onur@hilalavize.com',
    description='High-speed communication bridge between Unreal Engine 5 simulation and ROS 2',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'bridge_node = autonomous_robot_bridge.bridge_node:main',
            'sim_mock_node = autonomous_robot_bridge.sim_mock_node:main',
        ],
    },
)
