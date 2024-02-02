# Import JSON module
import json


def diameter(circ):
    return int(circ / 3.14)


def circumfernce(diam):
    return int(diam * 3.14)


def years(au):
    # print("Hello from a function")
    return round((au**3) ** 0.5, 2)


def distance(P):
    # print("Hello from a function")
    return round((P**2) ** (1.0 / 3.0), 2)


def volume(r):
    return 1.333 * 3.14 * (r**3)


def diam_circ(body, tabs):
    if tabs == 0:
        tabs = ""
    else:
        tabs = "\t" * tabs

    if "Circumference" not in body:
        body["Circumference"] = circumfernce(body["Diameter"])

    if "Diameter" not in body:
        body["Diameter"] = diameter(body["Circumference"])

    print(tabs + "Diameter: " + str(body["Diameter"]))
    print(tabs + "Circumference: " + str(body["Circumference"]))


def year_dist(body, tabs):
    if tabs == 0:
        tabs = ""
    else:
        tabs = "\t" * tabs

    if "DistanceFromSun" not in body:
        body["DistanceFromSun"] = distance(body["OrbitalPeriod"])

    if "OrbitalPeriod" not in body:
        body["OrbitalPeriod"] = years(body["DistanceFromSun"])

    print(tabs + "Distance From Sun: " + str(body["DistanceFromSun"]))
    print(tabs + "Orbital Period: " + str(body["OrbitalPeriod"]))


# Define JSON string
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# Convert JSON String to Python
solar = json.loads(jsonString)

# volumes
sun_vol = 0
planets_vol = 0

# Print values using keys
print(solar["Name"])

diam_circ(solar, 1)
sun_vol = volume(solar["Diameter"] / 2)

print("\n\t" + "Planets\n")
for planet in solar["Planets"]:
    print("\t" + planet["Name"])

    diam_circ(planet, 2)
    year_dist(planet, 2)
    # print("\n")
    planets_vol += volume(planet["Diameter"] / 2)

    if "Moons" in planet and len(planet["Moons"]) > 0:
        print("\n\t\t" + "Moon(s)\n")
        for moon in planet["Moons"]:
            print("\t" + "\t" + moon["Name"])
            diam_circ(moon, 3)
            # print("\n")


if sun_vol > planets_vol:
    print("The sun is bigger than the planets")
elif sun_vol < planets_vol:
    print("The planets are bigger than the sun")
else:
    print("The planets and sun are of equal volume")

print(sun_vol)
print(planets_vol)
