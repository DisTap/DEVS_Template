from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
import datetime

from abc import abstractmethod

class eventTemplate(BehaviorModelExecutor):
    def __init__(self, i_time, d_time, name, ename):
        super().__init__(i_time, d_time, name, ename)
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate",0)

        self.insert_input_port("event")

    def ext_trans(self,port, msg):
        if port == "event":
            print(f"[Gen][IN]: {datetime.datetime.now()}")
            self._cur_state = "Generate"

        self.ext_action(port)

    def output(self):
        if self._cur_state == "Generate":
            #print(f"[Gen][OUT]: {datetime.datetime.now()}")
            self.out_action()
            return None
            
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"
        else:
            self._cur_state = "Wait"
        self.int_action()
