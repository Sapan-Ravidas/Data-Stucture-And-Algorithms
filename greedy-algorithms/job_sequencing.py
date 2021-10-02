# job sequencing within deadline for getting maximum profit

class Job:
    def __init__(self, name, profit, deadline):
        self.name = name
        self.profit = profit
        self.deadline = deadline
        
    def __repr__(self):
        return f"JOB(j='{self.name}', p={self.profit}, d={self.deadline})"
    

def job_sequencing(jobs):
    n = len(jobs)
    # sort accordance with profit
    jobs.sort(key = lambda x : x.profit, reverse=True)
    max_deadline = max(x.deadline for x in jobs)
    max_profit = 0
    
    # print('\n'.join(map(str, jobs)))
    # print(max_deadline)
    
    # keep track of time-slot
    time_slot = [False] * max_deadline
    sequence = [None] * max_deadline
    
    for i in range(n):
        start = min(max_deadline - 1, jobs[i].deadline - 1)
        for j in range(start, -1, -1):
            if time_slot[j] == False:
                time_slot[j] = True
                sequence[j] = jobs[i]
                max_profit += jobs[i].profit
                break
    
    print('\n'.join(map(str, sequence)))
    print('maximum-profit', max_profit)


if __name__ == '__main__':
    jobs = [
        Job('a', 2, 3), 
        Job('b', 4, 3), 
        Job('c', 3, 3), 
        Job('d', 1, 4), 
        Job('e', 10, 4) 
    ]
    
    job_sequencing(jobs)