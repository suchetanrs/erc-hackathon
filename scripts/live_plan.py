import cv2
import os
import rospy


os.chdir('..')
currdir=os.getcwd()
currdir=currdir+'/live_map/'
print(currdir)

# currdir='/home/suchetan/Desktop/Path-graphs/'
rospy.init_node('live_plan',anonymous=True)
while not rospy.is_shutdown():
    try:
        img=cv2.imread(currdir+'path.jpg')

        cv2.imshow("plan",img)
        cv2.waitKey(1)
        rospy.loginfo("")
    except:
        print("Broken image")