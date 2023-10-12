from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite

from eventTemplate import eventTemplate

import zmq

class ClientAction(eventTemplate):
    def __init__(self, i_time, d_time, name, ename):
        super().__init__(i_time, d_time, name, ename)

    def ext_action(self, port):
        #print(f"[Gen][{port}]: {datetime.datetime.now()}")
        print("Action")
        pass

    def out_action(self):
        #print(f"[Gen][OUT]: {datetime.datetime.now()}")
        print("ex : db insert action/AI training")
    
    def int_action(self):
        pass