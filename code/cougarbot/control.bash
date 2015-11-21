rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["hip", "shoulder", "elbow", "wrist"], points: [{positions: [0.1, -0.5, 0.5, 0.75], time_from_start: [1.0, 0.0]}]}'
