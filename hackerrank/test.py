# Given a string representing an organizational hierarchy, it needs to be converted in different format using python. Attempt any 1 output
# Here is how an employee information looks like in the String.
#
# <employee_id>:<Employee_name>:<manager_id>
#
# Input String
# 1:Mike:4, 4:Ron:0, 2:John:4, 3:gerg:1
#
# Output1
# Ron
# -  Mike
# -- Gerg  #
# -   John
#
#                         4-ron-0
#                 2-john-4          1-mike-4
#                                         3-gerg-1
#
# 2k + 1
#
#

#
# Output2
#
# Mike – Gerg
# Ron – Mike, John #  tke emp_id and loop over manager_id of all n show emp name
# John –
# Gerg  –


input = '1:Mike:4, 4:Ron:0, 2:John:4, 3:gerg:1'

# emp = []
# for i in input.split(','):
#     emp_id, emp_name, manager_id = i.split(':')
#     # print(emp_id, emp_name, manager_id)
#     temp = {'emp_id': int(emp_id), 'emp_name': emp_name, 'manager_id': int(manager_id)}
#     emp.append(temp)
#
# print(emp)
#
# for index, id in enumerate(emp):
#     # string =
#     base_id = id['emp_id']
#
#     # print(string, base_id)
#     _list = []
#     for emp_id in emp:
#         if emp_id['manager_id'] == base_id:
#             _list.append(emp_id['emp_name'])
#
#     print(f"{id['emp_name']} - {' '.join(_list)}")


man_id = {}
emp = {}
for i in input.split(', '):
    emp_id, emp_name, manager_id = i.split(':')
    temp = {'emp_id': int(emp_id), 'emp_name': emp_name, 'manager_id': int(manager_id)}

    if man_id.get(int(manager_id), False):
        man_id[int(manager_id)].append(temp)
    else:
        man_id[int(manager_id)] = [temp]

    emp[int(emp_id)] = emp_name

for k, v in emp.items():
    # print(k,v)
    sub = [i['emp_name'] for i in man_id.get(k, '')]
    print(v, '-', ','.join(sub))
