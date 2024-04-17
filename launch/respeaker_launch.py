from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='respeaker_ros',
            executable='respeaker_node.py',
            name='respeaker_node',
            output='screen',
            parameters=[{'some_parameter': 'value'}]  # If you have parameters to set
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transformer',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'respeaker_base', '100']
        ),
        Node(
            package='respeaker_ros',
            executable='speech_to_text.py',
            name='speech_to_text',
            remappings=[('audio', 'speech_audio')],
            parameters=[{
                'language': 'ja-JP',
                'self_cancellation': True,
                'tts_tolerance': 0.5
            }]
        )
    ])
