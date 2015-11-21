cmake_minimum_required(VERSION 2.8.3)
project(cpp)

find_package(catkin REQUIRED roscpp)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cpp
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

add_executable(minimal src/minimal.cpp)
add_executable(topic_publisher src/topic_publisher.cpp)
add_executable(topic_subscriber src/topic_subscriber.cpp)
add_executable(service_server src/service_server.cpp)
add_executable(service_client src/service_client.cpp)
add_executable(action_server src/action_server.cpp)
add_executable(action_client src/action_client.cpp)


target_link_libraries(minimal
  ${catkin_LIBRARIES}
)

target_link_libraries(topic_publisher
  ${catkin_LIBRARIES}
)

target_link_libraries(topic_subscriber
  ${catkin_LIBRARIES}
)

target_link_libraries(service_server
  ${catkin_LIBRARIES}
)

target_link_libraries(service_client
  ${catkin_LIBRARIES}
)

target_link_libraries(action_server
  ${catkin_LIBRARIES}
)

target_link_libraries(action_client
  ${catkin_LIBRARIES}
)

