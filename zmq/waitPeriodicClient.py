from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
import datetime

from abc import abstractmethod

import zmq

from waitPeriodicTemplate import WaitPeriodicTemplate

from eventAction import ClientAction
 

class ZmqClient(WaitPeriodicTemplate):
    def __init__(self, i_time, d_time, name, ename, freq):
        super().__init__(i_time, d_time, name, ename, freq)

        #self.insert_output_port("receive")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.connect("tcp://127.0.0.1:5555")

    def ext_start_action(self, msg):
        print(f"[Gen][]: {datetime.datetime.now()}")
        pass

    def ext_stop_action(self, msg):
        pass
        

    def out_action(self):
        print(f"[Gen][OUT]: {datetime.datetime.now()}")
        work_message = self.socket.recv_json()
        print(f"> Received work")
        msg = self.prepare_output_msg1(work_message)

        return msg
    
    def int_action(self):
        pass


ss = SystemSimulator()

ss.register_engine("first", "REAL_TIME", 1)
ss.get_engine("first").insert_input_port("start")

client = ZmqClient(0, Infinite, "Gen", "first", 1)
ss.get_engine("first").register_entity(client)

action = ClientAction(0, Infinite, "Act", "first")
ss.get_engine("first").register_entity(action)

ss.get_engine("first").coupling_relation(None, "start", client, "start")
ss.get_engine("first").coupling_relation(client, "msg1", action, "start")

ss.get_engine("first").insert_external_event("start", None)
ss.get_engine("first").simulate()