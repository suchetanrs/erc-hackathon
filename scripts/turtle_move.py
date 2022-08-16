#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point,Twist
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from math import atan2,degrees,radians
from erc_hackathon_22.srv import GoalPoint, GoalPointResponse

class Navigate():
    def __init__(self):
        self.x=0.0
        self.y=0.0
        self.theta=0.0
        self.rot_q=0
        self.goal = Point()
        self.goal.x=0
        self.goal.y=0

        self.goal_reached_flag=False
    
    def callback(self,msg):
        self.x=msg.pose.pose.position.x
        self.y=msg.pose.pose.position.y
        
        self.rot_q=msg.pose.pose.orientation
        (self.roll,self.pitch,self.theta)=euler_from_quaternion([self.rot_q.x,self.rot_q.y,self.rot_q.z,self.rot_q.w])
        


        speed = Twist()


        inc_x=self.goal.x - self.x
        inc_y=self.goal.y - self.y
        print(self.goal.x,self.goal.y)
        print(inc_x,inc_y)
        print(self.x,self.y)

        

        angle_to_goal = atan2(inc_y,inc_x)
        if(angle_to_goal<0):
            angle_to_goal=360-abs(degrees(angle_to_goal))
            angle_to_goal=radians(angle_to_goal)
        print("angle to goal: {}".format(angle_to_goal))
        if(self.theta<0):
            self.theta=360-abs(degrees(self.theta))
            self.theta=radians(self.theta)
        print("current angle: {}".format(self.theta))
        print(self.theta)


        if(abs(inc_x)<0.05 and abs(inc_y)<0.05):
            speed.linear.x=0
            speed.angular.z=0
            print("Goal reached")
            self.goal_reached_flag=True
        elif(abs(angle_to_goal - self.theta) > 0.05 and angle_to_goal > self.theta and abs(angle_to_goal - self.theta) < 3.1415):
            print("acw")
            speed.linear.x=0.0
            speed.angular.z=0.15
        elif(abs(angle_to_goal - self.theta) > 0.05 and angle_to_goal > self.theta and abs(angle_to_goal - self.theta) > 3.14159):
            speed.linear.x=0.0
            speed.angular.z=-0.15
            print("cw")
        elif(abs(angle_to_goal - self.theta) > 0.05 and angle_to_goal < self.theta and abs(angle_to_goal - self.theta) < 3.1415):
            print("cw")
            speed.linear.x=0.0
            speed.angular.z=-0.15
        elif(abs(angle_to_goal - self.theta) > 0.05 and angle_to_goal < self.theta and abs(angle_to_goal - self.theta) > 3.14159):
            speed.linear.x=0.0
            speed.angular.z=0.15
            print("acw")
        elif(abs(inc_x)>0.05 or abs(inc_y)>0.05):
            print("Forward")
            speed.linear.x=0.22
            speed.angular.z=0.0
        else:
            speed.linear.x=0
            speed.angular.z=0

################################
        # speed.angular.z=0.1
        # if(self.theta>radians(230) and self.theta<radians(232)):
        #     speed.angular.z=0

##############################
        self.pub.publish(speed)

    def adjust_goal(self,msg):
        self.goal_reached_flag=False
        self.goal=Point()
        self.goal.x=msg.x
        self.goal.y=msg.y
        # rospy.sleep(0.5)
        return GoalPointResponse(0)
        while(True):
            if(self.goal_reached_flag==True):
                break
        # return GoalPointResponse(0)

    def main(self):
        rospy.init_node('turtle_move', anonymous=True)
        sub=rospy.Subscriber('/odom',Odometry,self.callback)
        self.pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
        
        serv1 = rospy.Service('/set_goal_point', GoalPoint, self.adjust_goal)
        self.pub2=rospy.Publisher('/odom', Odometry,queue_size=1)
        obj=Odometry()
        obj.pose.pose.position.x=1
        obj.pose.pose.position.y=10
        self.pub2.publish(obj)
        rospy.spin()

if __name__ == "__main__":
    Navigate().main()