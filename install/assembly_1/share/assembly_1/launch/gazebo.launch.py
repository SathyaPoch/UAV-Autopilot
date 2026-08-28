import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('assembly_1')
    
    world_path = os.path.join(pkg_share, 'world', 'rice_field.sdf')
    model_file = os.path.join(pkg_share, 'urdf', 'assembly_1.sdf')

    # launch the worlds
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world_path}'}.items()
    )
    # spawn the SDF model file directly into Gazebo
    drone = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-file', model_file,
            '-name', 'assembly_1',
            '-x', '0',
            '-y', '0',
            '-z', '2.0'
        ]
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock]',
            '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU]',
            '/navsat@sensor_msgs/msg/NavSatFix[gz.msgs.NavSatFix]',
            '/camera/image_raw@sensor_msgs/msg/Image[gz.msgs.Image]',
            '/camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo]'
        ],
        output='screen'
    )

    world_start_delay = 5.0

    return LaunchDescription([
        gazebo,
        TimerAction(period=world_start_delay, actions=[drone]),
        TimerAction(period=world_start_delay + 1.0, actions=[bridge]),
    ])