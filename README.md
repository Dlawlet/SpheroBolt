# SpheroBolt
The Purpose of the project in this repository is to :
1) Understand and get full control of sphero bolt robot
2) Implement swarm behaviour over Bolt    
Link to the drive : https://drive.google.com/drive/folders/1IiVMOUZykn09_1tVKfp_dGZxOYvhKSlI
# Requirement 
To run the project, the requirement are : 
* lib Spherov2 [https://github.com/artificial-intelligence-class/spherov2.py/tree/bd2f0b326e86dd336fa86ba64b6844731f9249d7]
* lib Bleak

# Usage 
1) Clone this repository
2) Install the dependencies previously mentionned 
3) Execute the following command : ``` python main.py 'XXXXX' ``` whre XXXX is the name of the bolt such as 'SB-AA77'

# Quick Start 
Actually, the project is a simple pong, it can be launch through the following step.
1) In a terminal clone the repository with : ```git clone https://github.com/Dlawlet/SpheroBolt.git```
2) Install python if not yet installed with ```sudo apt install python3 -y``` on linux, or just download a version>=3.7 from [https://www.python.org/downloads/windows/] on windows 
3) install pip with ```sudo apt install python3-pip``` (only for linux)
4) Install Bleak library with : ```pip install bleak==0.19.5```
5) install spherov2 unofficial library with : ```pip install spherov2==0.11.4```
6) Enter the repo with ```cd SpheroBolt```  
8) run the main with ```python3 main.py "SB-AA77"``` where "SB-AA77" is the name of the bolt i want to use.  
the bolt will roll and turn at 180° on collision
# WorkFlow 
## Finished 
    * Test every robot 
    * Library overview
    * Collision detection and event response ( to be optimized )
    * Installation and config on a raspberry pi 4 
    * Test the code over the raspberry through ssh 
    * Connect 15 bolts using the raspberry and a pc 
    
## Ongoing
    * Connect more than 8 bolts on the raspberry using bt dongle [need specific dongle for linux]
    * IR communication : 
        |_* Broadcasting  IR 
        |_* Follow and escape Broadcasted IR
    * Test TCPadapter connexion [connexion refused]

## Future
    * Create and animation with 15 bolts using IR communication, LED main display and collision ( before January )
    * Create a launcher to start multiple bots at once ( already started )
    * More advanced behaviour of the swarm (to be define)
# License
   This Project is released under the MIT License. See the MIT (LICENSE) file for more details.

