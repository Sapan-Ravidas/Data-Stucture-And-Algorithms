import atexit, sys, io

buffer = io.StringIO()
sys.stdout = buffer

@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())



def job_sequencing(jobs):
    pass

if __name__=="__main__":
    pass
