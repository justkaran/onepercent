import math
print(math.pi)

#The formular to calculate the surface area of a sphere is 4 timed pi * r^2. 

# Lets say the radius of sphere is 6.371 km, then the surface area is 6.371 ° 2 * 4 * (math.pi)
surfaceRaw = 6371000 ** 2 * 4 * (math.pi)
landRaw = surfaceRaw * 0.29
habitatRaw = landRaw * 0.57
habitatRawSinAgriculture = habitatRaw * 0.23
perPerson = round((habitatRawSinAgriculture / 7800000000))


surface = round((6371 ** 2 * 4 * (math.pi))/1000000)
land = round(surface * 0.29)
habitat = round(land * 0.57)


print("Die Fläche der Erde beträgt",  surface, "millionen Quadratkilometer.")

print("Land beträgt", land,  "millionen Quadratkilometer.")

print("Bewohnbares Land beträgt", habitat,  "millionen Quadratkilometer.")

print("Das bedeutet", perPerson, "Quadratmeter pro Person")