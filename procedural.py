# Import JSON module
import json

# pi is being approxiamted as 3.14, it's fine for these calculation
pi = 3.14


# a bunch of small functions
# --------------------------------------------


# calculates diameter from circumference
def diameter(circ):
    return int(circ / pi)


# calculates circumference from diameter
def circumfernce(diam):
    return int(diam * pi)


# calulates orbital period from planets distance from sun (au)
def years(au):
    return round((au**3) ** 0.5, 2)


# calculates planet's distance from sun given it's orbital period
def distance(P):
    # print("Hello from a function")
    return round((P**2) ** (1.0 / 3.0), 2)


# volume of a shpere
def volume(r):
    return 1.333 * pi * (r**3)


# bigger functions
# -----------------------------------------------


# checks if circumference or diameter is missing
# calculates missing value, puts it into the dict
def diam_circ(body):

    if "Circumference" not in body:
        body["Circumference"] = circumfernce(body["Diameter"])

    if "Diameter" not in body:
        body["Diameter"] = diameter(body["Circumference"])


# checks if oribital period or distance from sun is missing
# calculates missing value, puts it into the dict
def year_dist(body):

    if "DistanceFromSun" not in body:
        body["DistanceFromSun"] = distance(body["OrbitalPeriod"])

    if "OrbitalPeriod" not in body:
        body["OrbitalPeriod"] = years(body["DistanceFromSun"])


# biggest functions
# ----------------------------------------


# goes through our dictionary and calculates missing data
def make_calculations(solar_system):
    # check sun
    diam_circ(solar_system)
    solar_system["Volume"] = volume(solar_system["Diameter"] / 2)
    # set planets volume to zero
    solar_system["Planets_Volume"] = 0

    # check planets
    for planet in solar_system["Planets"]:
        diam_circ(planet)
        year_dist(planet)
        # and volume to total planets volume
        solar_system["Planets_Volume"] += volume(planet["Diameter"] / 2)

        # check moons if exisit
        if "Moons" in planet and len(planet["Moons"]) > 0:
            for moon in planet["Moons"]:
                diam_circ(moon)


# used by print_results so not as much code needs to be repeated
def print_details(tabs, body):

    tabs = "\t" * tabs

    print(tabs + body["Name"])

    tabs += "\t"

    print(tabs + "Diameter: " + str(body["Diameter"]))
    print(tabs + "Circumference: " + str(body["Circumference"]))

    # not sure if this is the best way to check for planets but it works
    if "OrbitalPeriod" in body:
        print(tabs + "Distance From Sun: " + str(body["DistanceFromSun"]))
        print(tabs + "Orbital Period: " + str(body["OrbitalPeriod"]))


# goes through the dictionary and prints it nicely
def print_results(solar_system):

    print_details(0, solar_system)
    tabs = "\t"

    print(tabs + "Planets" + "\n")

    tabs += "\t"
    for planet in solar_system["Planets"]:
        print_details(1, planet)

        if "Moons" in planet and len(planet["Moons"]) > 0:
            print(tabs + "Moon(s)" + "\n")
            for moon in planet["Moons"]:
                print_details(2, moon)

    print("\n")
    if solar_system["Volume"] > solar_system["Planets_Volume"]:
        print("The sun has a greater volume than the combined volume of the planets")
    elif solar_system["Planets_Volume"] > solar_system["Volume"]:
        print("The combined volume of the planets have a greater volume than the sun")
    else:
        print("The combined volume of the planets is equal to volume of the sun")


# would be better if I read this in from another file... but it is OK
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# this is my main.. but I don't think python has main functions
# Convert JSON String to Python
solar = json.loads(jsonString)
make_calculations(solar)
print_results(solar)
