# Complete autonomous navigation stack for ERC Hackathon '22

# Services
```/get_path_points``` Can be called to get all the points to be traversed to reach the end co-ordinate. <br/>
```/set_start_end_point``` Can be called to set the start and end point for planning. <br/>
```/get_obstacles_grid``` Can be called to get the co-ordinates of obstacles in the current map. <br/>
```/set_goal_point``` Can be called to set the immediate next point for turtlebot. <br/>

# rqt_graph of the stack

![](https://github.com/suchetanrs/erc-hackathon-automation/blob/master/live_map/rosgraph.png)

# Video demonstration

__This video demonstrates real time obstacle detection and planning__

https://user-images.githubusercontent.com/79915569/184886612-29ac9e93-3fb2-459d-bf43-6195e36f3505.mp4


# Running the code
__The code is currently set to pre-mapped obstacles (A maze) and live obstacles mapping have been turned off__

# Hackathon submission
1. Run the command ```roslaunch erc_hackathon_22 automation_task.launch```
2. In another terminal run ```roslaunch erc_hackathon_22 automation_task_scripts.launch```

# How to run real-time obstacle and planning
