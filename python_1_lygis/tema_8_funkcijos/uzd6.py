# Užduočių tvarkaraštis

from datetime import datetime, timedelta
from typing import Dict, List

def sorted_schedule(task_schedule: List[Dict[str, str]]) -> List[str]:
    date_format = "%Y-%m-%d"
    for task in task_schedule:
        deadline_date = datetime.strptime(task['deadline'], date_format)
        task["start_date"] = deadline_date - timedelta(days=task["duration"])
    task_schedule.sort(key=lambda x: x["start_date"])
    return [task['name'] for task in task_schedule]


task_schedule = []
task_count = int(input("Enter number of tasks: "))
for task in range(task_count):
    name = input("Enter task name:")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    duration = int(input("Enter duration (days): "))
    task_schedule.append({"name": name, "deadline": deadline, "duration": duration})

print("\nList of tasks:")
for task in task_schedule:
    print(task)

sorted_tasks = sorted_schedule(task_schedule)
print(f"\nScheduled tasks: {sorted_tasks}")