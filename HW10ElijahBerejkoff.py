class SolarObject:
    def __init__(self, distance_au, spin_duration, orbit_days):
        # Attributes of the SolarObject
        self.distance_au = distance_au
        self.spin_duration = spin_duration
        self.orbit_days = orbit_days
    #Figuring out our colonization potential
    def colonization(self):
        earth_population = 6_000_000_000
        colonization_potential = earth_population / self.distance_au
        #Rounding to nearest hundredth
        return round(colonization_potential, 2)
#Planet class spins slightly elliptical, but not crazy :(
class Planet(SolarObject):
    def spin(self):
        # Override the spin method to always be "slightly elliptical"
        return "slightly elliptical"
#Comet class, spins like crazy!
class Comet(SolarObject):
    def spin(self):
        # Override the spin method to always be "like crazy"
        return "like crazy"

#Assign our data to the objects. Will print later.
halleys_comet = Comet(distance_au=17.8, spin_duration=2.2, orbit_days=27403)
hale_bopp = Comet(distance_au=186, spin_duration=11.2, orbit_days=97000)
earth = Planet(distance_au=1.0, spin_duration=24, orbit_days=365)
mars = Planet(distance_au=1.52, spin_duration=24.6, orbit_days=687)

#Define a function so we can print attributes and colonization potential
def print_solar_object_info(obj, name):
    print(f"{name} Attributes:")
    print(f"Distance from Sun (AU): {obj.distance_au}")
    print(f"Spin Duration (hours): {obj.spin_duration}")
    print(f"Orbital Period (days): {obj.orbit_days} (years: {obj.orbit_days / 365:.2f})")
    print(f"Spin: {obj.spin()}")
    print(f"Colonization Potential: {obj.colonization()} billion people\n")

# Print information for all four objects using our function above
print_solar_object_info(earth, "Earth")
print_solar_object_info(mars, "Mars")
print_solar_object_info(halleys_comet, "Halley's Comet")
print_solar_object_info(hale_bopp, "Hale-Bopp")

#NOTE: The example in canvus named OOPS exercise result.png isn't letting me click on it. Anyway, thanks for the lessons see you around!