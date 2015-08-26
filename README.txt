To be able to run this code you'll need to install the Pypot library: https://github.com/poppy-project/pypot/tree/master/pypot A big thanks to them for making such a flexible framework.

While it is not mandatory to run the code I'd still like you to take a look at Travis DeWolf's posts about DMPs: https://studywolf.wordpress.com/2013/11/16/dynamic-movement-primitives-part-1-the-basics/
His implementation of Discrete DMPs was used at the core of this code.

In order to execute the code you merely need to run auto1.py. Quadratot_config corresponds to a configuration of the robot, where each dynamixel servo is identified with a
different id number. There can't be 2 servos with the same id. If there are the communication packets will get mixed and will, most likely, not produce any satisfactory results.

At the tips go the uneven servos and at the joints connecting the legs to the torso we have the even servos. 

'port' attribute should be changed to reflect the port at which you'll connect to the USB2Dynamixel. Com[number] on windows, usually /dev/ttyUSB0 on linux.

The Behaviour parameter lets you select one of the 3 gaits: hard-coded one is constructed_gait, repeat_recorded is the gait read from the .json file and DMP_generated is... well, you guessed.

For a clear understanding on the inner workings of Pypot's primitives (not to be confused with DMPs), refer to Pypot's documentation.

One of the main problems I faced was synching the DMP reproduction with the actual commands given to the servos and the delay time given for them to act. Modifying the tau
value (line 56 DMPQ.py) allows you to speed up or slow down the movement, but keep in mind you'll have to compensate for this by changing the value of the condition at line
54.

The .json files are generated for every single repetition of the hard-coded gait, they do not correspond to separate motor information, each one encodes a full cycle.

The m[number].txt files encode the information of the positions of the servos for the cycle gait.json, they are used to teach the DMP the parameters of the f forcing function.
[Used to construct the given y,y' and y'' that define a taught trajectory]

To access the .STL files (for 3d printing of the parts) and checking other information, please refer to the original project page: http://yosinski.com/quadratot