# Complete autonomous navigation stack for ERC Hackathon '22

# Video demonstration
https://user-images.githubusercontent.com/79915569/184882640-b3912b4b-38f2-4a72-b577-92d19efcb0b7.mp4 <br/>
__This video demonstrates live obstacle detection and planning__

# Services
```/get_path_points``` Can be called to get all the points to be traversed to reach the end co-ordinate. <br/>
```/set_start_end_point``` Can be called to set the start and end point for planning. <br/>
```/get_obstacles_grid``` Can be called to get the co-ordinates of obstacles in the current map. <br/>
```/set_goal_point``` Can be called to set the immediate next point for turtlebot. <br/>

# rqt_graph of the stack

![](https://github.com/suchetanrs/erc-hackathon-automation/blob/master/live_map/rosgraph.png)

