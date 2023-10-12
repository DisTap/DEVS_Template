from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
import datetime

from abc import abstractmethod

from waitPeriodicTemplate import WaitPeriodicTemplate
import time

import zmq

class ZmqServer(WaitPeriodicTemplate):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename, freq)
        print("zmq server start")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUSH)
        self.socket.bind("tcp://127.0.0.1:5555")

    def ext_action(self, port):
        #print(f"[Gen][{port}]: {datetime.datetime.now()}")
        pass

    def out_action(self):
        print(f"[Gen][OUT]: {datetime.datetime.now()}")
        print("> send message")
        work_message = {"zmq test" : "test messsage part"}
        self.socket.send_json(work_message)
        time.sleep(1)
            
    def int_action(self):
        pass


ss = SystemSimulator()

ss.register_engine("first", "REAL_TIME", 1)
ss.get_engine("first").insert_input_port("start")
gen = ZmqServer(0, Infinite, "Gen", "first", 1)
ss.get_engine("first").register_entity(gen)

ss.get_engine("first").coupling_relation(None, "start", gen, "start")

ss.get_engine("first").insert_external_event("start", None)
ss.get_engine("first").simulate()


