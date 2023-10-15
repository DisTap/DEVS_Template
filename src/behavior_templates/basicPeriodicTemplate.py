from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage

import datetime

from abc import abstractmethod

class BasicPeriodicTemplate(BehaviorModelExecutor):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename)

        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", freq)

        self.insert_input_port("start")

    def ext_trans(self,port, msg):
        if port == "start":
            self._cur_state = "Generate"

    def output(self):
        return  self.out_action()
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"
        self.int_action()

