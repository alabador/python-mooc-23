# WRITE YOUR SOLUTION HERE:
# Please write a function named 
# count_subordinates(employee: Employee) which 
# recursively counts the number of subordinates each employee has.



class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    count = 0
    # base case - if employee has no subs, add 0.
    if len(employee.subordinates) < 1: #[]
        return 0 
    # Recursive case - 
    # Loop through subordinates list.
    # For each employee in list, increase employee count by 1.
    # Recursively call function again and add the return to the total.
    
    for i in employee.subordinates: #[t4, t6]
        count += 1 
        count += count_subordinates(i)
    # Return at end
    return count

# Planning:
# How this works is there will be a list of employee objects.
# Inside of a list, could be a nested list.
# We will need to find a way to recursively go through the function to count the amount of subordinates inside.
# Meaning.. we will not only need to find the direct subordinates, but also the sub of the subs.
# So we need to find total amount of elements inside the list, including nested. 

# Recursion:
# - Base Case
# - Case to stop recursing (recursive case)

if __name__ == "__main__":
    t1 = Employee("Sally")
    t2 = Employee("Eric")
    t3 = Employee("Matthew")
    t4 = Employee("Emily")
    t5 = Employee("Adele")
    t6 = Employee("Claire")
    t1.add_subordinate(t4)
    t1.add_subordinate(t6)
    t4.add_subordinate(t2)
    t4.add_subordinate(t3)
    t4.add_subordinate(t5)
    # t1.subordinate = [t4, t6]
    # t4.suborindate = [t2, t3, t5]
    print(count_subordinates(t1))
    print(count_subordinates(t4))
    print(count_subordinates(t5))