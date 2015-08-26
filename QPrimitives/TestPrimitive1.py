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
		m1 = self.robot.motors[2]
		m2 = self.robot.motors[3]
		m3 = self.robot.motors[4]
		m4 = self.robot.motors[5]

		while self.elapsed_time < 15:
			m4.goto_position(70.0,0.4,control=None,wait=False)
			m3.goto_position(0.0,0.3,control=None,wait=False)
			m2.goto_position(70.0,0.4,control=None,wait=False)
			m1.goto_position(0.0,0.3,control=None,wait=False)
			time.sleep(0.3)
			m3.goto_position(46.0,0.1,control=None,wait=False)
			m1.goto_position(46.0,0.1,control=None,wait=False)
			time.sleep(0.1)
			m4.goto_position(148.0,0.3,control=None,wait=False)
			m2.goto_position(148.0,0.3, control = None, wait = False)
			time.sleep(0.5)
			#for m in self.robot.leg2:
			#	print m.present_position
			#	if m.id == 4:
			#		m.goto_position(70.0,0.4,control=None,wait=False)
			#		m.goto_position(0.0,0.3,control=None,wait=False)
			#		time.sleep(0.3)
			#		m.goto_position(46.0,0.1,control=None,wait=False)
			#		time.sleep(0.1)
			#		m.goto_position(148.0,0.3, control = None, wait = False)
			#		time.sleep(0.5)
