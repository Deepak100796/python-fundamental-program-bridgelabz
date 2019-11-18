task=int(input("Enter the task: "))
deadline=[0]*task
minute=[0]*task
for i in range(len(minute)):
    print("task " , i , " time");
    minute.append(int(input("ENter the value: ")))
    print("task " , i , " deadline");
    deadline.append(int(input("Enter the deadline")))