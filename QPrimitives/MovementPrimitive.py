import pypot.primitive
import time

class MovementPrimitive(pypot.primitive.Primitive):

	def __init__(self,robot,iterations):
		self.robot = robot
		self.iterations = iterations
		pypot.primitive.Primitive.__init__(self,robot)

	def run(self):
		a = 0
		while a < self.iterations:
			f = str(a) + ".json"
			self.robot.Slide.f_name(f)
			self.robot.Slide.start()
			time.sleep(2.1)
			a = a+1

		self.robot.motors[0].goto_position(-90.0,0.1,control= None, wait = False) # questionable
		time.sleep(0.1) #questionable