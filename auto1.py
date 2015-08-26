import pypot.robot
from pypot.primitive.move import *
import time
from QPrimitives.SlidePrimitive import *
from QPrimitives.StandUpPrimitive import *
from QPrimitives.MovementPrimitive import *
from QPrimitives.ReplayRecordedMovement import *
from QPrimitives.DMPQ import *
from pypot.robot.config import ergo_robot_config


Quadratot_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['leg1','leg2','leg3','leg4'],
            'port': 'COM12'
        }
    },
    'motorgroups': {
        'leg1': ['m1', 'm2'],
        'leg2': ['m3', 'm4'],
        'leg3': ['m5', 'm6'],
        'leg4': ['m7', 'm8']
    },
    'motors': {
        'm1': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 1,
            'angle_limit': [-135.0, 46.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 2,
            'angle_limit': [-2.0, 160.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 3,
            'angle_limit': [-135.0, 46.0],
            'offset': 0.0
        },
        'm4': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 4,
            'angle_limit': [-2.0, 160.0],
            'offset': 0.0
        },
        'm5': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 5,
            'angle_limit': [-135.0, 46.0],
            'offset': 0.0
        },
        'm6': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 6,
            'angle_limit': [-2.0, 160.0],
            'offset': 0.0
        },
        'm7': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 7,
            'angle_limit': [-135.0, 46.0],
            'offset': 0.0
        },
        'm8': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 8,
            'angle_limit': [-2.0, 160.0],
            'offset': 0.0
        }
    }
}

Behaviour = 'DMP_generated' # 'constructed_gait' , 'repeat_recorded' , 'DMP_generated'
robot = pypot.robot.from_config(Quadratot_config)
robot.attach_primitive(StandUpPrimitive(robot),'StandUp')
robot.StandUp.start()
time.sleep(5.0)
if (Behaviour == 'repeat_recorded'):
    robot.attach_primitive(ReplayRecordedMovement(robot, 50),'replayrecord') #playback at 40 hz of a gait recorded at 50hz
    robot.replayrecord.start()
    time.sleep(20)
elif (Behaviour == 'constructed_gait'):
    robot.attach_primitive(SlidePrimitive(robot), 'Slide') # Discrete gait repeated by MovementPrimitive, calls upon MoveRecorder to store motor data
    robot.attach_primitive(MoveRecorder(robot,50,robot.motors), 'recorder') #used to record motor data at 50 hz
    robot.attach_primitive(MovementPrimitive(robot, 10.0), 'movement') # Primitive that executes Slide Primitive 10 times and gives filename to write to
    robot.movement.start()
    time.sleep(10.0)

elif (Behaviour == 'DMP_generated'):
    robot.attach_primitive(DMPQ(robot),'DMP')
    b = 0
    while(b < 6):
        robot.DMP.start()
        time.sleep(3.8)
        b = b+1

robot.close()

