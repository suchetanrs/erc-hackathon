import rospy
from std_msgs.msg import int32

class Student():
    def __init__(self): #initializes the class, all class variables should be declared here
        #we just add all the class variables
        self.var=0 #self. shows it is a class variables, the scope of these variables is the whole class
        self.var2=0
    
    def main(self):
        while(True):
            print(self.var)


if __name__=="__main__":
    Student().main() #calling the main method of the class. Here __init__ method is called before main.