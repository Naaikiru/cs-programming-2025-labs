ids = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]

ids = sorted(ids, key=lambda x: x['staff'], reverse=True)

print(ids[:3])