from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
import datetime

from abc import abstractmethod

class doubleEventTemplate(BehaviorModelExecutor):
    def __init__(self, i_time, d_time, name, ename):
        super().__init__(i_time, d_time, name, ename)

        #state
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)

        #input port
        self.insert_input_port("event1")
        self.insert_input_port("event2")

 
    def ext_trans(self,port, msg):
        if port == "event1":
            print(f"[Gen][IN]: {datetime.datetime.now()}")
            self._cur_state = "Generate"

            self.ext_event1_action(msg)

        elif port == "envent2":
            self.ext_event2_action(msg)

    def output(self):
        if self._cur_state == "Generate":
            return self.out_action()
            
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Wait"
        else:
            self._cur_state = "Wait"
        self.int_action()

    @abstractmethod
    def ext_event1_action(self,msg):
        pass

    @abstractmethod
    def ext_event2_action(self,msg):
        pass

