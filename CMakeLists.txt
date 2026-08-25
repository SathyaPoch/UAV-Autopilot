cmake_minimum_required(VERSION 3.8)
project(assembly_1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find ros2 build dependencies
find_package(ament_cmake REQUIRED)

install(DIRECTORY
  assembly_1/config
  assembly_1/launch
  assembly_1/meshes
  assembly_1/urdf
  assembly_1/world
  DESTINATION share/${PROJECT_NAME}
)
# Optional
install(FILES
  README.md
  DESTINATION share/${PROJECT_NAME}
  OPTIONAL
)

ament_package()