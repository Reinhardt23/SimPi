import multiprocessing
import psutil

from simpiProcess import simpi_processing


class SimpiProcessController:
    """SimpiProcessController class for controling simpi child process
    """
    process = None
    processutil = None

    def __init__(self, data):
        """create a new simpi process
        Args:
            data (dictionary): 
        """
        self.process = multiprocessing.Process(target=simpi_processing, args=(data,))
        self.process.start()
        self.processutil = psutil.Process(self.process.pid)

    def suspend(self):
        """suspend simpi process
        """
        if(self.processutil.status() == "running"): 
            self.processutil.suspend()
        else:
            print("Warning: the simpi process is already suspended")

    def resume(self):
        """resume simpi process
        """
        if(self.processutil.status() == "stopped"): 
            self.processutil.resume()
        else:
            print("Warning: the simpi process is already running")

    def kill(self):
        """kill simpi process
        """
        self.process.kill()

