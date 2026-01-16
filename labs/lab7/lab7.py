# 1

objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]

objects = sorted(objects, key=lambda x: x[1])
print(objects)


# 2

ss = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]

s1 = list(map(lambda x: {'name': x['name'], 'all_cost': x['shift_cost'] * x['shifts']}, ss))
s2 = max(s1, key=lambda x: x["all_cost"])
print(s1)
print(s2)


# 3

pl = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]

p1 = list(map(lambda x: {'name': x['name'], 'clearance': x['clearance'], 'category': (
    'Restricted' if x['clearance'] == 1
    else 'Confidential' if 2 <= x['clearance'] <= 3
    else 'Top Secret'
    ) }, pl))
print(p1)