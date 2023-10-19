from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from pyevsim.system_message import SysMessage

from waitPeriodicTemplate import WaitPeriodicTemplate
import datetime

from abc import abstractmethod

class waitPeriodic(WaitPeriodicTemplate):


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

    def out_action(self):
        pass
    
    def int_action(self):
        pass

    def prepare_output_msg1(self, msg):
        return SysMessage(self.get_name(), "msg1")

