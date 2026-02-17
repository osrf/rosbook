cmake_minimum_required(VERSION 3.8)
project(followbot)

# if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
#   add_compile_options(-Wall -Wextra -Wpedantic)
# endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(OpenCV REQUIRED)
find_package(image_transport REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

# Install directories
 install(DIRECTORY
   models launch
   DESTINATION share/${PROJECT_NAME}
 )

# Install Python package
ament_python_install_package(
    followbot
    PACKAGE_DIR python/followbot)

# Install Python scripts
install(PROGRAMS
    scripts/follower_p.py
#    scripts/test_cmd_vel.py
    scripts/test_move_base.py
    scripts/test_vision.py
    DESTINATION lib/${PROJECT_NAME}
)

# Install C++ nodes
# set(AUTONOMY_SOURCES
#     src/navigation_behaviors.cpp 
#     src/vision_behaviors.cpp
# )
set(TARGET_DEPENDS
    nav2_msgs sensor_msgs cv_bridge image_transport
    tf2 tf2_ros tf2_geometry_msgs
)
include_directories(include)
# add_executable(autonomy_node_cpp src/autonomy_node.cpp ${AUTONOMY_SOURCES})
# install(TARGETS
#     autonomy_node_cpp
#     DESTINATION lib/${PROJECT_NAME}
# )
#ament_target_dependencies(${TARGET_DEPENDS})
#target_link_libraries(${OpenCV_LIBS} ${YAML_CPP_LIBRARIES})

ament_package()
