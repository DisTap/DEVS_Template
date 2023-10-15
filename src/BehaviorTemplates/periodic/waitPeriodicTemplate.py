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
        pass

    @abstractmethod
    def ext_stop_action(self, msg):
        pass

    def prepare_output_msg1(self, msg):
        return SysMessage(self.get_name(), "msg1")

'''

class PEx(WaitPeriodicTemplate):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename, freq)
        pass

    def ext_action(self, port):
        print(f"[Gen][{port}]: {datetime.datetime.now()}")

    def out_action(self):
        print(f"[Gen][OUT]: {datetime.datetime.now()}")
    
    def int_action(self):
        pass

ss = SystemSimulator()

ss.register_engine("first", "REAL_TIME", 1)
ss.get_engine("first").insert_input_port("start")
gen = PEx(0, Infinite, "Gen", "first", 1)
ss.get_engine("first").register_entity(gen)

ss.get_engine("first").coupling_relation(None, "start", gen, "start")

ss.get_engine("first").insert_exxternal_event("start", None)
ss.get_engine("first").simulate()

'''

