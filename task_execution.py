#!/usr/bin/env python
import os
import sys
import re
import rospy
import datetime
from std_srvs.srv import Empty
from wam_srvs.srv import *

class WamController:
	def __init__(self):
		ns = "zeus"
		self.DOF = 7
		self.dir_path = "/home/froglake/AssistiveRobotics/motion_scripts/"
		# self.textfiles = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(".txt")]
		self.textfiles = [f for f in os.listdir(self.dir_path) if f.lower().endswith('.txt')]
		rospy.wait_for_service("/" + ns + "/wam/go_home")
		self.joint_move_srvs = rospy.ServiceProxy("/" + ns + "/wam/joint_move", JointMove)
		rospy.wait_for_service("/" + ns + "/bhand/initialize")
		self.initialize_hand_srvs = rospy.ServiceProxy("/" + ns + "/bhand/initialize", Empty)
		rospy.wait_for_service("/" + ns + "/bhand/open_grasp")
		self.open_grasp_srvs = rospy.ServiceProxy("/" + ns + "/bhand/open_grasp", Empty)
		rospy.wait_for_service("/" + ns + "/bhand/close_grasp")
		self.close_grasp_srvs = rospy.ServiceProxy("/" + ns + "/bhand/close_grasp", Empty)
		rospy.wait_for_service("/" + ns + "/bhand/open_spread")
		self.open_spread_srvs = rospy.ServiceProxy("/" + ns + "/bhand/open_spread", Empty)
		rospy.wait_for_service("/" + ns + "/bhand/close_spread")
		self.close_spread_srvs = rospy.ServiceProxy("/" + ns + "/bhand/close_spread", Empty)
		rospy.wait_for_service("/" + ns + "/wam/teach_motion")
		self.teach_motion_srvs = rospy.ServiceProxy("/" + ns + "/wam/teach_motion", Teach)
		rospy.wait_for_service("/" + ns + "/wam/play_motion")
		self.play_motion_srvs = rospy.ServiceProxy("/" + ns + "/wam/play_motion", Play)
		rospy.wait_for_service("/" + ns + "/wam/go_home")
		self.go_home_srvs = rospy.ServiceProxy("/" + ns + "/wam/go_home", Empty)
		print "Connected to WAM services"
		
	def display_user_options(self, textfiles):
		# display options by number
		for option in textfiles:
			print(textfiles.index(option) +  ": " +option + "\n")

	def initial_position(self):
		try:
			if self.DOF == 7:
				pos = [0.0, -1.57, 0.0, 1.57, 0.0, 0.0, 0.0]
			else:
				pos = "[0.0, -1.57, 0.0, 1.57]"
  			self.joint_move_srvs(pos)
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def initialize_hand(self):
		try:
  			self.initialize_hand_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def open_grasp(self):
		try:
  			self.open_grasp_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def close_grasp(self):
		try:
  			self.close_grasp_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def open_spread(self):
		try:
  			self.open_spread_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def close_spread(self):
		try:
  			self.close_spread_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def teach_motion(self):
		name = raw_input("Please enter task name >> ")
		time = datetime.datetime.now().strftime("%Y%m%d%H%M")
		filename = name + "_" + time[2:]
		try:
  			self.teach_motion_srvs(filename)
			print "Saving motion to " + filename
			self.textfiles.append(filename)
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))

	def play_motion(self):
		print "\n".join(f for f in self.textfiles)
		x = raw_input("Please enter the name of the file you would like to play >> ")
		if re.search(r".*(txt)", x.lower()):
			filename = self.dir_path + x
		else:
			filename = self.dir_path + x + ".txt"
		if os.path.isfile(filename):
			try:
	  			self.play_motion_srvs(filename)
			except rospy.ServiceException as exc:
	  			print("Service Error: " + str(exc))
	  	else:
			print "The specified file does not exist\nPlease enter one of the following files:"
	  		self.play_motion()

	def go_home(self):
		try:
  			self.go_home_srvs()
		except rospy.ServiceException as exc:
  			print("Service Error: " + str(exc))