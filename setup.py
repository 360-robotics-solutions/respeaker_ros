from setuptools import setup

package_name = 'respeaker_ros'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/respeaker_launch.py']),
        ('share/' + package_name, ['requirements.txt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yuki Furuta',
    maintainer_email='furushchev@jsk.imi.i.u-tokyo.ac.jp',
    description='The respeaker_ros package for ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'respeaker_node = respeaker_ros.respeaker_node:main',
            'speech_to_text = respeaker_ros.speech_to_text:main',
        ],
    },
)
