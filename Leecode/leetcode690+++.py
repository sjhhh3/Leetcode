employee = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1

class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

employees = [Employee(1,5,[2,3]), Employee(2, 3, []), Employee(3, 3, [])]

# print(sum(employees[i-1].importance for i in employees[id-1].subordinates)+employees[id-1].importance)
#
# print(employees[1].id)

dic = {employee.id: employee for employee in employees}


def val(employee): return employee.importance + sum(val(dic[sub]) for sub in employee.subordinates)


print(val(dic[id]))
