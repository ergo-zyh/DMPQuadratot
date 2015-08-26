import pypot.primitive
import time

class StandUpPrimitive(pypot.primitive.Primitive):

	def __init__(self,robot,amp = 30, freq = 0.5):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self,robot)
		self.filename = ""

	def run(self):
		self.robot.motors[1].goto_position(160.0,0.3,control=None,wait=False)
		self.robot.motors[0].goto_position(-110.0,0.1,control=None,wait=False)
		time.sleep(0.7)
		self.robot.motors[3].goto_position(160.0,0.3,control=None,wait=False)
		self.robot.motors[2].goto_position(-110.0,0.1,control=None,wait=False)
		time.sleep(0.7)
		self.robot.motors[5].goto_position(160.0,0.3,control=None,wait=False)
		self.robot.motors[4].goto_position(-110.0,0.1,control=None,wait=False)
		time.sleep(0.7)
		self.robot.motors[7].goto_position(160.0,0.3,control=None,wait=False)
		self.robot.motors[6].goto_position(-110.0,0.1,control=None,wait=False)
		time.sleep(0.7)
		self.robot.motors[0].goto_position(-90.0,0.1,control=None,wait=False)
		self.robot.motors[2].goto_position(-90.0,0.1,control=None,wait=False)
		self.robot.motors[4].goto_position(-90.0,0.1,control=None,wait=False)
		self.robot.motors[6].goto_position(-90.0,0.1,control=None,wait=False)
		time.sleep(0.8)
		self.robot.motors[1].goto_position(100.0,0.3,control=None,wait=False)
		self.robot.motors[3].goto_position(100.0,0.3,control=None,wait=False)
		self.robot.motors[5].goto_position(100.0,0.3,control=None,wait=False)
		self.robot.motors[7].goto_position(100.0,0.3,control=None,wait=False)
		time.sleep(0.8)
		#Alternative standup sequence:
		#for m in self.robot.motors:
		#	if m.id == 1 or m.id == 3 or m.id == 5 or m.id == 7:
		#		m.goto_position(-90.0,0.3, control = None, wait = False)
		#		time.sleep(0.4)
		#	if m.id == 4 or m.id == 2 or m.id == 6 or m.id == 8:
		#		m.goto_position(100.0,0.3, control = None, wait = False)
		#		time.sleep(0.4)
