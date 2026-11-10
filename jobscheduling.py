#jobscheduling
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit
    n = max(job[1] for job in jobs)
    slots = [None] * n
    for job in jobs:
        for i in range(job[1]-1, -1, -1):  # Latest free slot
            if slots[i] is None:
                slots[i] = job
                break
    selected = [job[0] for job in slots if job]
    profit = sum(job[2] for job in slots if job)
    return selected, profit
n = int(input("Enter number of jobs: "))
jobs = []
for _ in range(n):
    job_id = input("Job ID: ")
    deadline = int(input("Deadline: "))
    profit = int(input("Profit: "))
    jobs.append((job_id, deadline, profit))
selected_jobs, total_profit = job_scheduling(jobs)
print("\nSelected Jobs:", selected_jobs)
print("Maximum Profit:", total_profit)
