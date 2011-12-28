import time

from pulsar.apps import tasks


class RunPyCode(tasks.Job):
    '''execute python code in *code*. There must be a *task_function*
function defined wich accept key-valued parameters only.'''
    def __call__(self, consumer, code, **kwargs):
        code_local = compile(code, '<string>', 'exec')
        ns = {}
        exec(code_local,ns)
        func = ns['task_function']
        return func(**kwargs)
        

class Addition(tasks.Job):
    
    def __call__(self, consumer, a, b):
        return a+b
    
    
class NotOverLap(tasks.Job):
    can_overlap = False
    
    def __call__(self, consumer, lag, *args, **kwargs):
        time.sleep(lag)
        return 'OK'