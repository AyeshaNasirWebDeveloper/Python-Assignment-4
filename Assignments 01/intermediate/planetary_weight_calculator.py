gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

earth_weight = float(input("Enter a weight on Earth: "))

planet_input = input("Enter a planet: ").capitalize()

if planet_input in gravity_constants:
    planet_weight = round(earth_weight * gravity_constants[planet_input], 2)
    print(f"The equivalent weight on {planet_input}: {planet_weight}")
else:
    print("That planet is not in the list. Please enter a valid planet.")