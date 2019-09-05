def createEmployee(base, employee):
    if employee in base:
        print("Employee " + employee["name"] + " " + employee["surname"] + " it already exists.")
    else:
        base.append(employee)

def readEmployee(base, emp):
    if emp in base:
        return emp
    else:
        print("There is no such employee!")

def updateEmployee(base, old, new):
    if not old in base:
        print("There is no such employee!")
    else:
        index = base.index(old)
        base[index]["name"] = new["name"]
        base[index]["surname"] = new["surname"]
        base[index]["position"] = new["position"]
        base[index]["salary"] = new["salary"]

def removeEmployee(base, emp):
    if not emp in base:
        print("There is no such employee!")
    else:
        base.remove(emp)


def searchByPosition(base, position):
    list = []
    for emp in base:
        if emp["position"] == position:
            list.append(emp)
    if len(list) == 0:
        print("There are no employees in this position!")
    return list

def bestSalary(base):
    if(len(base) == 0):
        print("Employee base is empty!")
        return
    best = 0
    emp = []
    for x in base:
        if x["salary"] > best:
            emp.clear()
            emp.append(x)
            best = x["salary"]
        elif x["salary"] == best:
            emp.append(x)
            best = x["salary"]
    return emp

def worstSalary(base):
    if(len(base) == 0):
        print("Employee base is empty!")
        return
    worst = -1
    emp = []
    for x in base:
        if x["salary"] < worst or worst == -1:
            emp.clear()
            emp.append(x)
            worst = x["salary"]
        elif x["salary"] == worst:
            emp.append(x)
            worst = x["salary"]
    return emp

def avgSalary(base):
    if(len(base) == 0):
        print("Employee base is empty!")
        return
    sum = 0
    for x in base:
        sum += x["salary"]

    return sum / len(base)


##Test:

db = []

emp = {
    "name" : "John",
    "surname" : "Rambo",
    "stanowisko" : "soldier",
    "salary": 5000
}

createEmployee(db, emp)
createEmployee(db, {
    "name" : "Mary",
    "surname" : "James",
    "stanowisko" : "singer",
    "salary": 7000
})

createEmployee(db, {
    "name" : "Ron",
    "surname" : "Tumor",
    "stanowisko" : "doctor",
    "salary": 4000
})


removeEmployee(db, {
    "name" : "Ron",
    "surname" : "Tumor",
    "stanowisko" : "doctor",
    "salary": 4000
})


print(db)