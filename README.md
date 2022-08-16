# Complete autonomous navigation stack for ERC Hackathon '22

# Video demonstration
https://user-images.githubusercontent.com/79915569/184886184-19eea786-baeb-4013-9788-f6c42a76c6ef.mp4 <br/>
__This video demonstrates live obstacle detection and planning__

# Services
```/get_path_points``` Can be called to get all the points to be traversed to reach the end co-ordinate. <br/>
```/set_start_end_point``` Can be called to set the start and end point for planning. <br/>
```/get_obstacles_grid``` Can be called to get the co-ordinates of obstacles in the current map. <br/>
```/set_goal_point``` Can be called to set the immediate next point for turtlebot. <br/>

# rqt_graph of the stack

![](https://github.com/suchetanrs/erc-hackathon-automation/blob/master/live_map/rosgraph.png)

