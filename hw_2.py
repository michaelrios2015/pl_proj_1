# Import JSON module
import json


def diameter(circ):
    return circ / 3.14


def circumfernce(diam):
    return diam * 3.14


def years():
    print("Hello from a function")


def distance():
    print("Hello from a function")


def volume():
    print("Hello from a function")


# Define JSON string
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# Convert JSON String to Python
solar = json.loads(jsonString)

# Print Dictionary
print(solar)

# Print values using keys
print(solar["Name"])

# this should be it's own function
if "Diameter" in solar and "Circumference" in solar:
    print(solar["Diameter"])
    print(solar["Circumference"])

elif "Diameter" in solar:
    print(solar["Diameter"])
    print(circumfernce(solar["Diameter"]))
else:
    print(diametere(solar["Circumference"]))
    print(solar["Circumference"])

for planet in solar["Planets"]:
    print("\t" + planet["Name"])

    if "Moons" in planet:
        for moon in planet["Moons"]:
            print("\t" + "\t" + moon["Name"])


# print(solar["Planets"][3]["Moons"])
