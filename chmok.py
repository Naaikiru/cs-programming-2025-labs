protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

# Используем map и лямбда для создания нового списка строк
result = list(map(lambda protocol: f"Protocol {protocol[0]} - Criticality {protocol[1]}", protocols))

print(result)
