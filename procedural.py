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

    print(tabs + "Name: " + body["Name"])

    tabs += "\t"

    print(tabs + "Diameter: {:,.1f} km".format(body["Diameter"]))
    print(tabs + "Circumference: {:,.1f} km".format(body["Circumference"]))

    # not sure if this is the best way to check for planets but it works
    if "OrbitalPeriod" in body:
        print(tabs + "Distance From Sun: {:,.1f} au".format(body["DistanceFromSun"]))
        print(tabs + "Orbital Period: {:,.1f} yr".format(body["OrbitalPeriod"]))


# goes through the dictionary and prints it nicely
def print_results(solar_system):

    print("Sun")
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


# Opening JSON file
file = open("JSONPrintyPrint.txt")

# returns JSON object as
# a dictionary
solar = json.load(file)

# close file
file.close()

# this is my main.. but I don't think python has main functions
make_calculations(solar)
print_results(solar)
