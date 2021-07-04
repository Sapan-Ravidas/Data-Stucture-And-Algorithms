import atexit, sys, io

buffer = io.StringIO()
sys.stdout = buffer

@atexit.register
def write():
    sys.__stdout__.write(buffer.getvalue())



def job_sequencing(jobs):
    n = len(jobs)
    jobs.sort(key = lambda x: x[2], reverse=True)
    max_deadline = max([x[1] for x in jobs])
    
    # keep track of free time slots
    time_slot = [False] * max_deadline
    
    sequence = [None] * max_deadline
    
    for i in range(n):
        start = min(max_deadline - 1, jobs[i][1] - 1)
        for j in range(start, -1, -1):
            if time_slot[j] == False:
                time_slot[j] = True
                sequence[j] = jobs[i][0]
                break
    print(sequence)       
    

if __name__=="__main__":
    jobs = [
        ('a', 2, 100),
        ('b', 1, 19),
        ('c', 2, 27),
        ('d', 1, 25),
        ('e', 3, 15)
    ]
    job_sequencing(jobs)
