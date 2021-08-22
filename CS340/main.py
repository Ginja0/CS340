from AnimalShelter import AnimalShelter

test = AnimalShelter()
animal_data = [
    {
        "name":"Star",
        "type":"panda"
    },
    {
        "name":"Mapache",
        "type":"panda"
    },
    {
        "name":"Blackeyes",
        "type":"panda"
    },
    {
        "name":"Whatcha",
        "type":"Silver"
    }
]

for i in animal_data:
    test.create(i)

pandas = test.read( {"type":"panda"}  )
for panda in pandas:
    print(panda)