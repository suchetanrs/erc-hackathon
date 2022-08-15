#!/usr/bin/env python

from math import cos,sin
import rospy
from sensor_msgs.msg import LaserScan
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from math import tan,radians,degrees
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class Plots():
    def __init__(self):
        # self.ani=animation.FuncAnimation(self.fig, animate, interval=1000)
        plt.ion()
        plt.show()
        self.curr_x=0
        self.curr_y=0
        self.rot_q=0
        self.roll=0
        self.pitch=0
        self.theta=0
        self.scan_data=[]

    def mapping(self,msg):
        self.scan_data=msg.ranges

    def localization(self,msg):
        self.curr_x=msg.pose.pose.position.x
        self.curr_y=msg.pose.pose.position.y

        self.rot_q=msg.pose.pose.orientation
        (self.roll,self.pitch,self.theta)=euler_from_quaternion([self.rot_q.x,self.rot_q.y,self.rot_q.z,self.rot_q.w])
        if(self.theta<0):
            self.theta=360-abs(degrees(self.theta))
            self.theta=radians(self.theta)
        for items in self.scan_data:
            if(items<float('inf')):
                try:
                    print(self.theta)
                    index=self.scan_data.index(items) 
                    x=items*cos(radians(index)+self.theta)
                    y=items*sin(radians(index)+self.theta)
                    plt.plot(self.curr_x+x,self.curr_y+y,marker="o")
                except:
                    print("Exception")
        # self.ax.xlim(-10,10)
        # self.ax.ylim(-10,10)
        # self.fig.canvas.draw()
        # self.fig.canvas.flush_events()
        plt.grid()
        plt.pause(1e-10)
        plt.grid()

    def main(self):
        rospy.init_node('map',anonymous=True)
        sub=rospy.Subscriber('/scan',LaserScan,self.mapping,queue_size=1)
        sub2=rospy.Subscriber('/odom',Odometry,self.localization,queue_size=1)
        rospy.spin()

if __name__=="__main__":
    Plots().main()