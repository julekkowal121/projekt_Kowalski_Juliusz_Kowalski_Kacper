from setuptools import setup
import os  # <--- WAŻNE
from glob import glob  # <--- WAŻNE

package_name = 'camera_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Camera subscriber node in ROS2',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_node = camera_subscriber.camera_node:main',
	    'simple_sub = camera_subscriber.simple_sub:main',
	    'mouse_node = camera_subscriber.mouse_node:main',
	    'robot_control = camera_subscriber.robot_control:main',
        ],
    },
)
