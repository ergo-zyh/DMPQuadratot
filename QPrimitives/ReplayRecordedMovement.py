import pypot.primitive
from pypot.primitive.move import *
import time

class ReplayRecordedMovement(pypot.primitive.primitive.LoopPrimitive):

	def __init__(self,robot, freq):
		self.robot = robot
		f = open('gait.json', 'r')
		a = Move.load(f)
		robot.attach_primitive(MovePlayer(robot,a),'replay')
		pypot.primitive.primitive.LoopPrimitive.__init__(self,robot,freq)

	def update(self):
		a = 0
		while(a < 10):
			self.robot.replay.start()
    		time.sleep(2.2)
    		a = a+1

