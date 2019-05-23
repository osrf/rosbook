cmake_minimum_required(VERSION 2.8.3)
project(cpp)

find_package(catkin REQUIRED
  COMPONENTS
  roscpp
  message_generation
  actionlib
  actionlib_msgs
  std_msgs)

add_service_files(FILES WordCount.srv)

add_action_files(DIRECTORY action FILES Sample.action)

generate_messages(DEPENDENCIES std_msgs actionlib_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cpp
  CATKIN_DEPENDS message_runtime roscpp std_msgs
#  DEPENDS system_lib
)

include_directories(${catkin_INCLUDE_DIRS})

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
add_dependencies(service_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(service_client
  ${catkin_LIBRARIES}
)
add_dependencies(service_client ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(action_server
  ${catkin_LIBRARIES}
)
add_dependencies(service_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(action_client
  ${catkin_LIBRARIES}
)
add_dependencies(service_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
