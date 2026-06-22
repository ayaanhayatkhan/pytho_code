people = [
    {"name": "Ayaan", "number": "+1-617-495-10000"},
    {"name": "Hayat", "number": "+1-617-495-1000"},
    {"name": "Khan", "number": "+1-949-468-2750"},
]
name = input("Name: ")

for person in people:
    if person["name"] == name:
        print(f"Found: {person["number"]}")
        break
    else:
        print("Not found")
        