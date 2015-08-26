import pypot.primitive
import time

class TestPrimitive(pypot.primitive.Primitive):

	def __init__(self,robot,amp = 30, freq = 0.5):
		self.robot = robot
		self.amp = amp
		self.freq = freq
		pypot.primitive.Primitive.__init__(self,robot)

	def run(self):
		amp = self.amp
		freq = self.freq
		x = -130
		m5 = self.robot.motors[4]
		m3 = self.robot.motors[2]
		m7 = self.robot.motors[6]
		m6 = self.robot.motors[5]
		m1 = self.robot.motors[0]
		m2 = self.robot.motors[1]

		while self.elapsed_time < 8:

			m6.goto_position(60.0,0.1,control=None,wait=False)
			m5.goto_position(-120.0,0.1,control=None,wait=False)
			time.sleep(0.3)
	
			m1.goto_position(-130.0,0.1,control=None,wait=False) #reloading

			time.sleep(0.3)

			m5.goto_position(-100.0,0.1,control=None,wait=False)
			m6.goto_position(100.0,0.1,control=None,wait=False)
			time.sleep(0.4)
			m1.goto_position(-60.0,0.2,control=None,wait=False) #pushing to advance

			time.sleep(0.7)
		m1.goto_position(-90.0,0.1,control= None, wait = False)
		time.sleep(0.1)