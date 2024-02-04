# Import JSON module
import json

# should be a cloase enough approximation
pi = 3.14


# not really sure if I should be doing it like this but seems to work well enough
class Sphere:
    #   so intiating everything as zero except the name
    def __init__(self, name):
        self.name = name
        self.diameter = 0
        self.circumference = 0
        self.volume = 0

    # lets use get circumference from diamter
    def cal_circ(self):
        self.circumference = int(self.diameter * pi)

    # diamtere from circumference
    def cal_diam(self):
        self.diameter = int(self.circumference / pi)

    # volume calculator
    def cal_vol(self):
        self.volume = 1.333 * pi * ((self.diameter / 2) ** 3)

    # seems easier in here, but maybe should be somewhere else
    def display(self, tabs):
        if tabs == 0:
            tabs = ""
        else:
            tabs = "\t" * tabs

        print(tabs + "Name: " + self.name)
        print(tabs + "\t" + "Diameter: " + str(self.diameter))
        print(tabs + "\t" + "Circumference: " + str(self.circumference))


class Sun(Sphere):
    # so the only thing we need to add is the plantes array
    def __init__(self, name):
        super().__init__(name)
        self.planets = []

        # should the checking of volumes go in here???


class Planet(Sphere):
    # orbit period, distance from sun and moons array added
    def __init__(self, name):
        super().__init__(name)
        self.orbit = 0
        self.distance = 0
        self.moons = []

    # lets use get circumference from diamter
    def cal_orbit(self):
        self.orbit = round((self.distance**3) ** 0.5, 2)

    # diamtere from circumference
    def cal_distance(self):
        self.distance = round((self.orbit**2) ** (1.0 / 3.0), 2)

    def display_planet(self, tabs):
        if tabs == 0:
            tabs = ""
        else:
            tabs = "\t" * tabs

        print(tabs + "Orbital Period: " + str(self.orbit))
        print(tabs + "DIstance From Sun: " + str(self.distance))


class Moon(Sphere):
    # nothing but the sphere needed
    def __init__(self, name):
        super().__init__(name)


# Define JSON string
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# Convert JSON String to Python
solar = json.loads(jsonString)

# volume for planets
planets_vol = 0

sun = Sun("sol")
# this should be it's own function but does it go into sphere or is it just a seperate function
# we need to see what information is in the json
if "Circumference" in solar and "Diameter" in solar:
    sun.circumference = solar["Circumference"]
    sun.diameter = solar["Diameter"]

elif "Circumference" not in solar:
    # sun.circumference = solar["Circumference"]
    sun.diameter = solar["Diameter"]
    sun.cal_circ()

else:
    sun.circumference = solar["Circumference"]
    # sun.diameter = solar["Diameter"]


sun.display(0)
sun.cal_vol()
# used to get our place in the planets array
counter = 0

print("\tPlanets:\n")
for planet in solar["Planets"]:

    sun.planets.append(Planet(planet["Name"]))
    # this shopuld be it's own function but does it go in the object??
    if "Circumference" in planet and "Diameter" in planet:
        sun.planets[counter].circumference = planet["Circumference"]
        sun.planets[counter].diameter = planet["Diameter"]

    elif "Circumference" not in planet:
        sun.planets[counter].diameter = planet["Diameter"]
        sun.planets[counter].cal_circ()

    else:
        sun.planets[counter].circumference = planet["Circumference"]
        sun.planets[counter].cal_diam()

    if "DistanceFromSun" in planet and "OrbitalPeriod" in planet:
        sun.planets[counter].distance = planet["DistanceFromSun"]
        sun.planets[counter].orbit = planet["OrbitalPeriod"]

    elif "DistanceFromSun" not in planet:
        sun.planets[counter].orbit = planet["OrbitalPeriod"]
        sun.planets[counter].cal_distance()
    else:
        sun.planets[counter].distance = planet["DistanceFromSun"]
        sun.planets[counter].cal_orbit()

    # so this works but I don't think I am supposed to do it like this
    sun.planets[counter].display(1)
    sun.planets[counter].display_planet(2)

    sun.planets[counter].cal_vol()
    planets_vol += sun.planets[counter].volume

    m_counter = 0
    if "Moons" in planet and len(planet["Moons"]) > 0:
        print("\t\tMoon(s):")

        for moon in planet["Moons"]:

            sun.planets[counter].moons.append(Moon(moon["Name"]))
            if "Circumference" in moon and "Diameter" in moon:
                sun.planets[counter].moons[m_counter].circumference = moon[
                    "Circumference"
                ]
                sun.planets[counter].moons[m_counter].diameter = moon["Diameter"]

            elif "Circumference" not in moon:
                sun.planets[counter].moons[m_counter].diameter = moon["Diameter"]
                sun.planets[counter].moons[m_counter].cal_circ()

            else:
                sun.planets[counter].moons[m_counter].circumference = moon[
                    "Circumference"
                ]
                sun.planets[counter].moons[m_counter].cal_diam()

            sun.planets[counter].moons[m_counter].display(2)

        m_counter += 1

    counter += 1


print(planets_vol)
print(sun.volume)

# print(sun.planets)
