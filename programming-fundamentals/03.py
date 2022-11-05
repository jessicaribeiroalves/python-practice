def sort_employees(employees, sort_by):
    if sort_by == 'name':
        return sorted(employees)
    elif sort_by == 'age':
        return sorted(employees, key=lambda x: x[1])
    elif sort_by == 'salary':
        return sorted(employees, key=lambda x: x[2])


employees = [
    ['John', 33, 65000],
    ['Jennifer', 31, 70000],
    ['Karen', 35, 80000],
    ['Khan', 42, 52000],
    ['Juan', 39, 94000],
    ['Ben', 41, 92000]
]
sort_employees(employees, 'salary')
