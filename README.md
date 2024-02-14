Output looks a bit nicer than what I submitted on black board

Procedural

```
Sun
Name: Sol
        Diameter: 1,400,000.0 km
        Circumference: 4,396,000.0 km
        Planets

        Name: Mecury
                Diameter: 4,881.0 km
                Circumference: 15,329.0 km
                Distance From Sun: 0.5 au
                Orbital Period: 0.4 yr
        Name: Venus
                Diameter: 12,104.0 km
                Circumference: 38,006.0 km
                Distance From Sun: 0.7 au
                Orbital Period: 0.6 yr
        Name: Earth
                Diameter: 12,756.0 km
                Circumference: 40,075.0 km
                Distance From Sun: 1.0 au
                Orbital Period: 1.0 yr
                Moon(s)

                Name: Luna
                        Diameter: 3,474.0 km
                        Circumference: 10,917.0 km
        Name: Mars
                Diameter: 6,797.0 km
                Circumference: 21,344.0 km
                Distance From Sun: 1.5 au
                Orbital Period: 1.9 yr
                Moon(s)

                Name: Phobos
                        Diameter: 22.5 km
                        Circumference: 70.0 km
                Name: Deimos
                        Diameter: 12.0 km
                        Circumference: 39.0 km
        Name: Jupiter
                Diameter: 142,984.0 km
                Circumference: 448,969.0 km
                Distance From Sun: 5.2 au
                Orbital Period: 11.9 yr
                Moon(s)

                Name: Ganymede
                        Diameter: 5,268.0 km
                        Circumference: 16,541.0 km
                Name: Callisto
                        Diameter: 1,535.0 km
                        Circumference: 4,820.6 km
                Name: Io
                        Diameter: 1,160.0 km
                        Circumference: 3,643.2 km
        Name: Saturn
                Diameter: 120,536.0 km
                Circumference: 378,483.0 km
                Distance From Sun: 9.5 au
                Orbital Period: 29.5 yr
        Name: Uranus
                Diameter: 51,118.0 km
                Circumference: 160,510.0 km
                Distance From Sun: 19.2 au
                Orbital Period: 84.1 yr
        Name: Neptune
                Diameter: 49,528.0 km
                Circumference: 155,517.0 km
                Distance From Sun: 30.1 au
                Orbital Period: 164.8 yr


The sun has a greater volume than the combined volume of the planets
```
Object Oriented 

```

  {
  "Name": "Sol",
  "Diameter": 1400000,
  "Planets": [
    {
      "Name": "Mecury",
      "OrbitalPeriod": 0.39,
      "Circumference": 15329
    },
    {
      "Name": "Venus",
      "DistanceFromSun": 0.72,
      "Diameter": 12104
    },
    {
      "Name": "Earth",
      "DistanceFromSun": 1,
      "OrbitalPeriod": 1,
      "Diameter": 12756,
      "Circumference": 40075,
      "Moons": [
        {
          "Name": "Luna",
          "Diameter": 3474,
          "Circumference": 10917
        }
      ]
    },
    {
      "Name": "Mars",
      "DistanceFromSun": 1.52,
      "Circumference": 21344,
      "Moons": [
        {
          "Name": "Phobos",
          "Diameter": 22.5
        },
        {
          "Name": "Deimos",
          "Circumference": 39
        }
      ]
    },
    {
      "Name": "Jupiter",
      "DistanceFromSun": 5.2,
      "Diameter": 142984,
      "Moons": [
        {
          "Name": "Ganymede",
          "Diameter": 5268
        },
        {
          "Name": "Callisto",
          "Circumference": 4820.6
        },
        {
          "Name": "Io",
          "Circumference": 3643.2
        }
      ]
    },
    {
      "Name": "Saturn",
      "DistanceFromSun": 9.54,
      "Diameter": 120536,
      "Moons": []
    },
    {
      "Name": "Uranus",
      "DistanceFromSun": 19.2,
      "Diameter": 51118
    },
    {
      "Name": "Neptune",
      "DistanceFromSun": 30.06,
      "Diameter": 49528
    }
  ]
}
```
