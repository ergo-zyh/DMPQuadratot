import pypot.primitive

class QuadratotRecord(pypot.primitive.LoopPrimitive):
    def __init__(self, robot, refresh_freq, amp=30, freq=0.5):
        self.robot = robot
        LoopPrimitive.__init__(self, robot, refresh_freq)

    # The update function is automatically called at the frequency given on the constructor
    def update(self):
        amp = self.amp
        freq = self.freq
        x = amp * numpy.sin(2 * numpy.pi * freq * self.elapsed_time)

        self.robot.base_pan.goal_position = x
        self.robot.head_pan.goal_position = -x