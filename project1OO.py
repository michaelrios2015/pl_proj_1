# Import JSON module
import json

import math

# feel like I am doing something wrong here
#


class Sphere:
    def __init__(self, name, diameter, circumference):
        self.name = name
        self.diameter = diameter
        self.circumference = circumference

    @classmethod
    def from_diameter(cls, name, diameter):
        return cls(name, diameter, circumference=diameter * 3.14)

    @classmethod
    def from_circumference(cls, name, circumference):
        return cls(name, circumference / 3.14, circumference)

    def volume(self):
        return 1.333 * 3.14 * ((self.diameter / 2) ** 3)


class Sun(Sphere):
    # self.planets = []
    # pass

    def __init__(self, name, diameter, circumference):
        super().__init__(name, diameter, circumference)
        self.planets = []


class Planet(Sphere):
    def __init__(self, name, diameter, circumference):
        super().__init__(name, diameter, circumference)
        self.moons = []


class Moon(Sphere):
    pass


def diam_circ(body):
    if "Circumference" not in body:
        body["Circumference"] = circumfernce(body["Diameter"])

    if "Diameter" not in body:
        body["Diameter"] = diameter(body["Circumference"])

    print(tabs + "Diameter: " + str(body["Diameter"]))
    print(tabs + "Circumference: " + str(body["Circumference"]))


#  V = 4/3 π r³

# sun = Sphere("sol", 1, 2)

# sun = Sphere.from_diameter("sol", 1)

# sun = Sphere.from_circumference("sol", 3.14)


# sun = Sun("sol", 1, 2)

# sun = Sun.from_diameter("sol", 1)

# sun = Sun.from_circumference("sol", 3.14)


# print(sun.name)
# print(sun.diameter)
# print(sun.circumference)
# print(sun.volume())
# print(sun.planets)


# moon = Moon("luna", 1, 2)

# print(moon.name)


# Define JSON string
jsonString = '{"Name": "Sol", "Diameter": 1400000, "Planets": [{"Name": "Mecury", "OrbitalPeriod": 0.39, "Circumference": 15329}, {"Name": "Venus", "DistanceFromSun": 0.72, "Diameter": 12104}, {"Name": "Earth", "DistanceFromSun": 1, "OrbitalPeriod": 1, "Diameter": 12756, "Circumference": 40075, "Moons": [{"Name": "Luna", "Diameter": 3474, "Circumference": 10917}]}, {"Name": "Mars", "DistanceFromSun": 1.52, "Circumference": 21344, "Moons": [{"Name": "Phobos", "Diameter": 22.5}, {"Name": "Deimos", "Circumference": 39}]}, {"Name": "Jupiter", "DistanceFromSun": 5.2, "Diameter": 142984, "Moons": [{"Name": "Ganymede", "Diameter": 5268}, {"Name": "Callisto", "Circumference": 4820.6}, {"Name": "Io", "Circumference": 3643.2}]}, {"Name": "Saturn", "DistanceFromSun": 9.54, "Diameter": 120536, "Moons": []}, {"Name": "Uranus", "DistanceFromSun": 19.2, "Diameter": 51118}, {"Name": "Neptune", "DistanceFromSun": 30.06, "Diameter": 49528}]}'

# Convert JSON String to Python
solar = json.loads(jsonString)

# volumes
sun_vol = 0
planets_vol = 0

if "Circumference" in solar and "Diameter" in solar:
    sun = Sun("sol", solar["Circumference"], solar["Diameter"])


elif "Circumference" not in solar:
    sun = Sun.from_diameter("sol", solar["Diameter"])


else:
    sun = Sun.from_circumference("sol", solar["Circumference"])

counter = 0
for planet in solar["Planets"]:
    if "Circumference" in planet and "Diameter" in planet:
        # temp = planet["Name"]

        sun.planets.append(
            Planet(planet["Name"], planet["Circumference"], planet["Diameter"])
        )

    elif "Circumference" not in planet:
        sun.planets.append(Planet.from_diameter(planet["Name"], planet["Diameter"]))

    else:
        sun.planets.append(
            Planet.from_circumference(planet["Name"], planet["Circumference"])
        )

    if "Moons" in planet:
        for moon in planet["Moons"]:
            print(counter)
            if "Circumference" in moon and "Diameter" in moon:
                # temp = planet["Name"]

                sun.planets[counter].moons.append(
                    Moon(moon["Name"], moon["Circumference"], moon["Diameter"])
                )

            elif "Circumference" not in moon:
                sun.planets[counter].moons.append(
                    Moon.from_diameter(moon["Name"], moon["Diameter"])
                )

            else:
                sun.planets[counter].moons.append(
                    Moon.from_circumference(moon["Name"], moon["Circumference"])
                )

    counter += 1

print(sun.name)
print(sun.diameter)
print(sun.circumference)
print(sun.volume())
print(sun.planets[2].name)
print(sun.planets[2].moons[0].name)
