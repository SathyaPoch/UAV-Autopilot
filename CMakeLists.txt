cmake_minimum_required(VERSION 3.0.2)
project(assembly_1_urdf)

find_package(catkin REQUIRED)
catkin_package()
# find_package(ament_cmake REQUIRED)
# find_package(rclcpp REQUIRED)
# find_package(std_msgs REQUIRED)
# find_package(geometry_msgs REQUIRED)

# Install URDF and mesh files
install(DIRECTORY
  .
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  FILES_MATCHING PATTERN "*.urdf"
  PATTERN "CMakeLists.txt" EXCLUDE
)

install(FILES
  README.md
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  OPTIONAL
)

ament_package()