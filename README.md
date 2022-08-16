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
__The code is currently set to pre-mapped obstacles (A maze) and live obstacles mapping have been turned off__<br/>
Clone the repository into your ```catkin_workspace``` and do ```catkin_make```

# Hackathon submission
1. ```roscore```
2. ```export TURTLEBOT3_MODEL=waffle```
3. Run the command ```roslaunch erc_hackathon_22 automation_task.launch```
4. In another terminal run ```roslaunch erc_hackathon_22 automation_task_scripts.launch```

# How to run real-time obstacle and planning
1. ```roscore```
2. ```export TURTLEBOT3_MODEL=waffle```
3. Cd into workspace by ```roscd erc_hackathon_22/scripts```
4. Run the command ```roslaunch erc_hackathon_22 automation_task.launch```
5. In another terminal run ```roslaunch erc_hackathon_22 automation_task_live_map_scripts.launch```
6. Open a new terminal and run ```rosrun erc_hackathon_22 Astar.py```
7. Open a new terminal and run ```python live_map.py``` to see the live obstacle plot and path plan.
