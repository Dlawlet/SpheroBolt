13/02/23
############ on Ir brodcasting and follow ############
1° in sphero_edu.py
    def start_ir_broadcast(self, near: int, far: int):
        """Sets the IR emitters to broadcast on two specified channels, from 0 to 7, so other BOLTs can follow or evade.
        The broadcaster uses two channels because the first channel emits near IR pulses (< 1 meter), and the second
        channel emits far IR pulses (1 to 3 meters) so the following and evading BOLTs can detect these messages on
        their IR receivers with a sense of relative proximity to the broadcaster. You can't use a channel for more than
        one purpose at time, such as sending messages along with broadcasting, following, or evading. For example,
        use ``start_ir_broadcast(0, 1)`` to broadcast on channels 0 and 1, so that other BOLTs following or evading on
        0 and 1 will recognize this robot."""
        ToyUtil.start_robot_to_robot_infrared_broadcasting(self.__toy, bound_value(0, far, 7), bound_value(0, near, 7))

change to : 
    def start_ir_broadcast(self, far: int, near: int):
Same for : 
    def start_ir_follow(self, far: int, near: int):
same goes for similar methods just under this one
     

2° in bolt.py
    start_robot_to_robot_infrared_broadcasting = Sensor.start_robot_to_robot_infrared_broadcasting
change to : 
    start_robot_to_robot_infrared_broadcasting = partialmethod(Sensor.start_robot_to_robot_infrared_broadcasting, proc=Processors.SECONDARY)
same for all similar methods just under this one

########### On message sending ###########
############## not yet validated ################
3°in sensor.py
    @staticmethod
    def send_robot_to_robot_infrared_message(toy, s, s2, s3, s4, s5, proc=None):  # Untested / Unknown param names
        toy._execute(Sensor._encode(toy, 42, proc, [s, s2, s3, s4, s5]))
change to :
    def send_robot_to_robot_infrared_message(toy, channel, intensity, proc=None):  
        toy._execute(Sensor._encode(toy, 42, proc, [channel, intensity]))

4° in bolt.py
    send_robot_to_robot_infrared_message = Sensor.send_robot_to_robot_infrared_message
change to :
    send_robot_to_robot_infrared_message = partialmethod(Sensor.send_robot_to_robot_infrared_message, proc=Processors.SECONDARY)

5° in utils.py
    def send_robot_to_robot_infrared_message(toy: Toy, channel: int, intensity: int,
                                             not_supported_handler: Callable[[], None] = None):
        # if toy.implements(Sensor.send_robot_to_robot_infrared_message): TODO: BOLT
        #     toy.send_robot_to_robot_infrared_message(channel, intensity, intensity, intensity, intensity)
        if toy.implements(Sensor.send_infrared_message):
            toy.send_infrared_message(channel, intensity, intensity, intensity)
        elif not_supported_handler:
            not_supported_handler()
change  specific line to :
    toy.send_robot_to_robot_infrared_message(channel, intensity)