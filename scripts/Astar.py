#!/usr/bin/env python

import rospy
from erc_hackathon_22.srv import GetPathPoints, GetPathPointsResponse, SetStartEndPoint, SetStartEndPointResponse
from erc_hackathon_22.msg import GoalPoint
import draw_graph as astar
import time
import sys

#############ID###############
# index 0 - X
# index 1 - Y
# index 2:
    #-1 - obstacle - black
    #0 - not touched - white
    #1 - closed - red
    #2 - open - green
    #3 - start point
    #4 - end point
# index 3 - h distance
# index 4 - g distance
# index 5 - f distance
# index 6 - coords of node it came from ( if sent to closed set)

class Planner():
    def __init__(self):
        self.openset=[]
        self.closedset=[]
        self.tracerset=[]
        self.start_coord=[0,0]
        print("STARTCOORD:{}".format(self.start_coord))
        self.end_coord=[33,33]
        hdist=astar.h_value([self.start_coord[0],self.start_coord[1]],[self.end_coord[0],self.end_coord[1]])
        # print("STARTCOORD:{}".format(self.start_coord))
        self.start_coord_id=[self.start_coord[0],self.start_coord[1],3,hdist,0,(hdist+0),[self.start_coord[0],self.start_coord[1]]]
        self.loopflag=False
        self.end_coord_id=[]
        # time.sleep(1)

        self.path_points=[]
    
    def algorithm(self,msg):
        print("Algo")
        curr_coord_id=self.start_coord_id
        self.openset.append(curr_coord_id)
        # print(self.openset)
        # print("****************")
        while(self.loopflag==False):
            # time.sleep(0.01)
            lowest_f_val_id=[0,0,0,0,0,100000000000000,0]
            # print("Lowest f_val_before_check:{}".format(lowest_f_val_id))
            for item in self.openset:
                if(item[5]<lowest_f_val_id[5]):
                    lowest_f_val_id=item
            curr_coord_id=lowest_f_val_id
            # print("Lowest f_val after check:{}".format(lowest_f_val_id))
            # print("Currect coordinates:{}".format(curr_coord_id))
            # print("Open set:{}".format(self.openset))
            self.openset.remove(curr_coord_id)
            self.closedset.append(curr_coord_id)

            if(curr_coord_id[0]==self.end_coord[0] and curr_coord_id[1]==self.end_coord[1]):
                print("Goal reached")
                print(self.start_coord)

                print("Tracer")
                point=[self.end_coord[0],self.end_coord[1]]
                print(point)
                obj=GoalPoint()
                obj.x=point[0]
                obj.y=point[1]
                self.path_points.append(obj)
                astar.draw_node(point[0],point[1],'g')
                print("Plotting")
                while(True):
                    flag=False
                    time.sleep(0.05)
                    for x in self.closedset:
                        if(x[0]==point[0] and x[1]==point[1]):
                            # print(point)
                            if(point==self.start_coord):
                                flag=True
                            point=x[6]
                            astar.draw_node(point[0],point[1],'b')
                            obj=GoalPoint()
                            obj.x=point[0]+0.5
                            obj.y=point[1]+0.5
                            self.path_points.append(obj)
                    if(flag==True):
                        break
                # astar.animate_plot()
                # astar.show_plot()
                break

            neighbour_list=astar.get_neighbor_list(curr_coord_id[0],curr_coord_id[1])
            neighbour_list_id=[]
            # print("(((((((((((((((((((((((((((((((((((((((((((((((((")
            for coords in neighbour_list:
                temp_list=['None'] * 7
                temp_list[0]=coords[0]
                temp_list[1]=coords[1]
                temp_list[2]=2
                # h=astar.h_value([coords[0],coords[1]],[self.end_coord[0],self.end_coord[1]])
                h=astar.h_value(coords,self.end_coord)
                temp_list[3]=h
                g=curr_coord_id[4]
                if(coords[0]==curr_coord_id[0] or coords[1]==curr_coord_id[1]):
                    g_added=1
                else:
                    g_added=1.4
                temp_list[4]=g+g_added
                temp_list[5]=temp_list[4]+temp_list[3]
                temp_list[6]=[curr_coord_id[0],curr_coord_id[1]]
                neighbour_list_id.append(temp_list)
                # print(neighbour_list_id)
            # print("--------------")
            # print("Neighbout list ids:{}".format(neighbour_list_id))
            # print("Open set:{}".format(self.openset))
            # print("Closed set:{}".format(self.closedset))

            for item in neighbour_list_id:
                in_closed_set=False
                for elem in self.closedset:
                    if(elem[0]==item[0] and elem[1]==item[1]):
                        in_closed_set=True
                if(in_closed_set==False):
                    n_in_open=False
                    n_f_value=0
                    n_x_value=0
                    n_y_value=0
                    for x in self.openset:
                        if(x[0]==item[0] and x[1]==item[1]):
                            n_in_open=True
                            n_f_value=x[5]
                            n_x_value=x[0]
                            n_y_value=x[1]
                    if(n_in_open==True and item[5]<n_f_value):
                        for x in self.openset:
                            if(x[0]==n_x_value and x[1]==n_y_value):
                                x[5]=item[5]
                                g=curr_coord_id[4]
                                if(x[0]==curr_coord_id[0] or x[1]==curr_coord_id[1]):
                                    g_added=1
                                else:
                                    g_added=1.4
                                g+=g_added
                                x[4]=g
                                x[6]=[curr_coord_id[0],curr_coord_id[1]]
                    if(n_in_open==False):
                        self.openset.append(item)
                        
            # time.sleep(0)
            # print("END OF ITERATION")
        
        return GetPathPointsResponse(self.path_points)

    def set_start_end_point(self,msg):
        self.openset=[]
        self.closedset=[]
        self.tracerset=[]
        self.start_coord=[msg.start_point_x,msg.start_point_y]
        print("STARTCOORD:{}".format(self.start_coord))
        self.end_coord=[msg.end_point_x,msg.end_point_y]
        hdist=astar.h_value([self.start_coord[0],self.start_coord[1]],[self.end_coord[0],self.end_coord[1]])
        print("ENDCOORD:{}".format(self.end_coord))
        self.start_coord_id=[self.start_coord[0],self.start_coord[1],3,hdist,0,(hdist+0),[self.start_coord[0],self.start_coord[1]]]
        self.loopflag=False
        self.end_coord_id=[]
        # time.sleep(1)

        self.path_points=[]
        return SetStartEndPointResponse(0)
    
    
    def main(self):
        rospy.init_node('Astar',anonymous=True)
        serv1=rospy.Service('/get_path_points',GetPathPoints,self.algorithm)
        serv2=rospy.Service('/set_start_end_point',SetStartEndPoint,self.set_start_end_point)

        rospy.spin()

                    
if(__name__=="__main__"):
    print("Playing")
    Planner().main()