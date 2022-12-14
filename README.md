# SpheroBolt
The Purpose of the project in this repository is to :
1) Understand and get full control of sphero bolt robot
2) Implement swarm behaviour over Bolt    
Link to the drive : https://drive.google.com/drive/folders/1IiVMOUZykn09_1tVKfp_dGZxOYvhKSlI
# Requirement 
To run the project, the requirement are : 
* bluetooth (bt) ( can handle up to 7 connexions at once)
* Python > 3.7 
* lib Spherov2 (https://github.com/artificial-intelligence-class/spherov2.py)
* |__lib Bleak

# Usage 
1) Clone the repository 
2) Install the dependencies previously mentionned 
3) Execute the following command : " python main.py 'XXXXX' " whre XXXX is the name of the bolt such as 'SB-AA77'

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

