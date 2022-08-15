#!/usr/bin/env python

# from cmath import exp
# from tracemalloc import start
import rospy
from erc_hackathon_22.srv import SetGoalPoint, GetPathPoints, SetStartEndPoint
from erc_hackathon_22.msg import GoalPoint
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from math import floor
import matplotlib.pyplot as plt

class MasterNode():
    def __init__(self):
        self.test_var=0
        self.path_points_list=[]
        self.curr_index=0
        self.curr_x=0
        self.curr_y=0

        self.end_x=33
        self.end_y=8
    
    def navigate(self):
        rospy.wait_for_service('/set_goal_point')
        # try:
        set_goal_point=rospy.ServiceProxy('/set_goal_point', SetGoalPoint)
        max_len=len(self.path_points_list)
        self.curr_index=max_len-1
        resp=set_goal_point(self.path_points_list[self.curr_index-2].x,self.path_points_list[self.curr_index-2].y)
        print("Set Goal point as {},{}".format(self.path_points_list[self.curr_index-2].x,self.path_points_list[self.curr_index-2].y))
        self.curr_index=self.curr_index-1
        # print("Next point")
        if(self.curr_index<0):
            while(True):
                continue
        else:
            # print("Reached")
            pass
    

    
    def path_points(self):
        rospy.wait_for_service('/set_start_end_point')
        try:
            start_end_point=rospy.ServiceProxy('/set_start_end_point', SetStartEndPoint)
            resp=start_end_point(self.curr_x,self.curr_y,self.end_x,self.end_y)
            print("Set start point as:{},{}".format(self.curr_x,self.curr_y))
        except:
            print("Cannot set start end point")

        
        rospy.wait_for_service('/get_path_points')
        try:
            get_path_points=rospy.ServiceProxy('/get_path_points', GetPathPoints)
            resp=get_path_points()
            self.path_points_list=resp.points
            for item in resp.points:
                plt.plot(item.x,item.y,marker="x")
            # plt.grid()
            plt.pause(1e-10)
            plt.grid()
            plt.clf()
            print("Got path points")
            # return resp.points
        except:
            print("Cannot get path points")
        # print("Setting Goal point")


        # rospy.wait_for_service('/set_goal_point')
        # try:
        # set_goal_point=rospy.ServiceProxy('/set_goal_point', SetGoalPoint)
        # max_len=len(self.path_points_list)
        # self.curr_index=max_len-1
        # resp=set_goal_point(self.path_points_list[self.curr_index-2].x,self.path_points_list[self.curr_index-2].y)
        # print("Set Goal point as {},{}".format(self.path_points_list[self.curr_index].x,self.path_points_list[self.curr_index].y))
        # self.curr_index=self.curr_index-1
        # print("Next point")
        # if(self.curr_index<0):
        #     while(True):
        #         continue
        # else:
        #     print("Reached")
            # return resp.result
        # except:
        #     print("Brain halted")
        # rospy.sleep(0.2)

    def odom(self,msg):
        self.curr_x=floor(msg.pose.pose.position.x)
        self.curr_y=floor(msg.pose.pose.position.y)
        # print(self.curr_x,self.curr_y)
        # rospy.sleep(1)
        


    def main(self):
        rospy.init_node('brain',anonymous=True)
        # rospy.Service('/set_goal_point',SetGoalPoint,self.navigate)
        # rospy.Service('/get_path_points',GetPathPoints,self.path_points)
        rospy.Subscriber('/odom',Odometry,self.odom)
        rospy.sleep(1)
        # rospy.Subscriber('/scan',LaserScan,self.path_points)
        rospy.sleep(2)
        # self.path_points()
        while not rospy.is_shutdown():
            # self.path_points_list=self.path_points()
            # max_len=len(self.path_points_list)
            # self.curr_index=max_len-1
            self.path_points()
            self.navigate()
            rospy.loginfo("")
            # rospy.sleep(2)


if __name__=="__main__":
    MasterNode().main()
