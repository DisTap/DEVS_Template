from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
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

    def ext_trans(self,port, msg):
        if port == "start":
            #print(f"[Gen][IN]: {datetime.datetime.now()}"ㅊ)
            self._cur_state = "Generate"
        elif port == "stop":
            self._cur_state = "Generate"

        self.ext_action(port)

    def output(self):
        #print(f"[Gen][OUT]: {datetime.datetime.now()}")
        self.out_action()
        return None
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"
        self.int_action()

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

