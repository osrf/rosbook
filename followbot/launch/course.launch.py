from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

def generate_launch_description():
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='-1.75')
    y_pose = LaunchConfiguration('y_pose', default='0.2')
    yaw = LaunchConfiguration('yaw', default='1.57')

    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'Circuit.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose,
            'yaw': yaw
        }.items()
    )

    return LaunchDescription(
        [
            # Arguments
            DeclareLaunchArgument(
                "location_file",
                default_value=TextSubstitution(text=default_world_dir),
                description="YAML file name containing map locations in the world.",
            ),
            DeclareLaunchArgument(
                "target_color",
                default_value=TextSubstitution(text="blue"),
                description="Target object color (red, green, or blue)",
            ),
            DeclareLaunchArgument(
                "tree_type",
                default_value=TextSubstitution(text="queue"),
                description="Behavior tree type (naive or queue)",
            ),
            DeclareLaunchArgument(
                "enable_vision",
                default_value=TextSubstitution(text="True"),
                description="Enable vision behaviors. If false, do navigation only.",
            ),
            # Main follower node
            Node(
                package="followbot",
                executable="follower.py",
                name="follower_node_python",
                output="screen",
                emulate_tty=True,
                parameters=[
                    {
                        "use_sim_time": LaunchConfiguration("use_sim_time"),
                        "debug": LaunchConfiguration("debug"),
                        "world_name": LaunchConfiguration("world_name"),
                    }
                ],
            ),
            # Behavior tree visualization
            ExecuteProcess(cmd=["py-trees-tree-viewer", "--no-sandbox"]),
        ]
    )
    
# <launch>

#   <!-- Fake laser -->
#   <node pkg="nodelet" type="nodelet" name="laserscan_nodelet_manager" args="manager"/>
#   <node pkg="nodelet" type="nodelet" name="depthimage_to_laserscan"
#         args="load depthimage_to_laserscan/DepthImageToLaserScanNodelet laserscan_nodelet_manager">
#     <param name="scan_height" value="10"/>
#     <param name="output_frame_id" value="/camera_depth_frame"/>
#     <param name="range_min" value="0.45"/>
#     <remap from="image" to="/camera/depth/image_raw"/>
#     <remap from="scan" to="/scan"/>
#   </node>
# </launch>

