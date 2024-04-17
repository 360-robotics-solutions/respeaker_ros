cmake_minimum_required(VERSION 3.5)
project(respeaker_ros)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Default settings for C++ compiler warnings
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(audio_common_msgs REQUIRED)  # Check if this package exists in ROS 2
find_package(geometry_msgs REQUIRED)

# Note: Dynamic reconfigure is not available in ROS 2
# Instead, ROS 2 uses parameters for dynamic configuration
# which can be updated at runtime using parameter services.

# Install Python nodes
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  ${PROJECT_NAME}/respeaker_node.py
  ${PROJECT_NAME}/speech_to_text.py
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

install(FILES
  requirements.txt
  DESTINATION share/${PROJECT_NAME})

# If testing is enabled, set up tests for ROS 2
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  # Here you would add any specific tests
endif()

# Macro for ament package
ament_package()
