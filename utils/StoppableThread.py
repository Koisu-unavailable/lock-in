import threading

class StoppableThread(threading.Thread):
    '''
    THE THREAD DOES HAVE TO CHECK FOR THE STOP EVENT REGULARLY
    '''
    def __init__(self,  *argsfunc, **kwargs):
        self._stop_event = threading.Event()
        super(StoppableThread, self).__init__(args=(self._stop_event,), *argsfunc, **kwargs)
        

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()