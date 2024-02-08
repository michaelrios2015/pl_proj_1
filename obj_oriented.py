# Import JSON module
import json

# should be a cloase enough approximation
pi = 3.14


# this works, not sure if it how it is supposed to be done
class Display:
    def print_details(self, tabs, body):
        tabs = "\t" * tabs
        print(tabs + "Name: " + body.Name)

        tabs += "\t"
        print(tabs + "Diameter: " + str(body.Diameter))
        print(tabs + "Circumference: " + str(body.Circumference))

        if hasattr(body, "DistanceFromSun"):
            print(tabs + "Orbital Period: " + str(body.OrbitalPeriod))
            print(tabs + "Distance From Sun: " + str(body.DistanceFromSun))

    def print_volume(self, body):

        if body.Volume > body.Planets_Volume:
            print(
                "The sun has a greater volume than the combined volume of the planets"
            )
        elif body.Planets_Volume > body.Volume:
            print(
                "The combined volume of the planets have a greater volume than the sun"
            )
        else:
            print("The combined volume of the planets is equal to volume of the sun")


# also works, again not really sure if this is how it's supposed to be done
class Calculate:
    def calc_missing(self, body):

        # checks to see if diamtere is zero and if so calculates it
        if body.Diameter == 0:
            body.Diameter = round((body.Circumference / pi), 1)

        # checks to see if Circumferene is zero and if so calculates it
        if body.Circumference == 0:
            body.Circumference = round((body.Diameter * pi), 1)

        # calculates volume
        body.Volume = 1.333 * pi * ((body.Diameter / 2) ** 3)

        if hasattr(body, "DistanceFromSun"):
            if body.OrbitalPeriod == 0:
                body.OrbitalPeriod = round((body.DistanceFromSun**3) ** 0.5, 2)

            if body.DistanceFromSun == 0:
                body.DistanceFromSun = round((body.OrbitalPeriod**2) ** (1.0 / 3.0), 2)


# i used the setattr function from the example you sent me
class Sphere:
    #   so intiating everything as blank or zero
    def __init__(self, my_dict):
        self.Name = ""
        self.Diameter = 0
        self.Circumference = 0
        self.Volume = 0

        # this fills in any data supplied by our dictionary
        for key in my_dict:
            setattr(self, key, my_dict[key])


class Sun(Sphere):
    # so the only thing we need to add is the plantes array
    def __init__(self, my_dict):
        super().__init__(my_dict)
        # this overrides the planets taken from my_dict, those are a list of dictionaries and I don't know how to convert them
        self.Planets = []
        # not sure if this really belongs here but could not think of a better place to put it
        self.Planets_Volume = 0


class Planet(Sphere):
    # orbit period, distance from sun and moons array added
    def __init__(self, my_dict):
        self.OrbitalPeriod = 0
        self.DistanceFromSun = 0
        # the sphere init will also check for all the keys in the dictionary
        super().__init__(my_dict)
        # same as Planets list in Sun
        self.Moons = []


class Moon(Sphere):
    # nothing but the sphere needed
    def __init__(self, my_dict):
        super().__init__(my_dict)


# Define JSON string
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# Convert JSON String to Python
solar = json.loads(jsonString)

# so I assume these should be functions ....
# converting the dictionary into objects
# -------------------------------------------------------
sun = Sun(solar)

# # used to get our place in the planets array
counter = 0

for planet in solar["Planets"]:
    currentPlanet = Planet(planet)
    sun.Planets.append(currentPlanet)

    m_counter = 0
    if "Moons" in planet and len(planet["Moons"]) > 0:

        for moon in planet["Moons"]:
            currentMoon = Moon(moon)
            sun.Planets[counter].Moons.append(currentMoon)

            m_counter += 1

    counter += 1

# calculate missing values
# ------------------------------------------

calc_o = Calculate()
calc_o.calc_missing(sun)

for planet in sun.Planets:
    calc_o.calc_missing(planet)
    sun.Planets_Volume += planet.Volume

    for moon in planet.Moons:
        calc_o.calc_missing(moon)


# print details
# -----------------------------------------------

print("Sun:")
disp_o = Display()
disp_o.print_details(0, sun)

print("\t---------")
print("\tPlanets:\n")
for planet in sun.Planets:
    disp_o.print_details(1, planet)

    if planet.Moons:
        print("\t\t---------")
        print("\t\tMoon(s):")

        for moon in planet.Moons:
            disp_o.print_details(2, moon)


disp_o.print_volume(sun)
