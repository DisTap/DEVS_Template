from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage
import datetime

from abc import abstractmethod

class WaitPeriodicTemplate(BehaviorModelExecutor):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename)
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", freq)

        self.insert_input_port("start")
        self.insert_input_port("stop")

        self.insert_output_port("msg1")
        
    def ext_trans(self,port, msg):
        if port == "start":
            print(f"[Gen][IN]: {datetime.datetime.now()}")
            self._cur_state = "Generate"
            self.ext_start_action(msg)
        elif port == "stop":
            self._cur_state = "Wait"
            self.ext_stop_action(msg)

        #self.ext_action(port)

    def output(self):
        #print(f"[Gen][OUT]: {datetime.datetime.now()}")
        return self.out_action()
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"
        self.int_action()

    @abstractmethod
    def ext_start_action(self, msg):
        """
        Action to perform upon receiving a message through the 'start' port.
        """
        pass

    @abstractmethod
    def ext_stop_action(self, msg):
        """
        Action to perform upon receiving a message through the 'stop' port.
        """
        pass

    def prepare_output_msg1(self, msg):
        return SysMessage(self.get_name(), "msg1")

