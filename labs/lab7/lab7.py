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
    else 'Top Secret')}, pl))
print(p1)


# 4

zs = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]

zz= list(filter(lambda x: x['active_from'] <= 8 and x['active_to'] >= 18, zs))

print(zz)


# 5

import re

rs = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]

rs1 = list(filter(lambda x: 'http' in x['text'], rs))
rs2 = list(map(lambda x: {'author': x['author'],
    'text': re.sub(r'https?://\S+', '[ДАННЫЕ УДАЛЕНЫ]', x["text"])}, rs1))

print(rs2)


# 6

scp_objs = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]

sd = list(filter(lambda x: x['class'] != 'Safe', scp_objs))

print(sd)


# 7

ids = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]

ids = sorted(ids, key=lambda x: x['staff'], reverse=True)

print(ids[:3])


# 8

pls = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

pls1 = list(map(lambda x: f'Protocol {x[0]} - Criticality {x[1]}', pls))

print(pls1)


# 9

shs = [6, 12, 8, 24, 10, 4]
shs = list(filter(lambda x: 8 <= x <= 12, shs))
print(shs)


# 10

es = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]

es1 = max(es, key=lambda x: x['score'])
print(es1['name'], es1['score'])