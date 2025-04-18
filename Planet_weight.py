
Mercury = 0.38
Venus = 0.91
Mars = 0.38
Jupiter = 2.53
Saturn = 1.07
Uranus = 0.89
Neptune = 1.14


earth_weight = float(input("Please type your weight here in Kg: "))
planet_number = int(input("Choose a planet from 1 to 7: "))

if planet_number == 1:
  print("destination weight: " + str(earth_weight*Mercury))
elif planet_number == 2:
  print("destination weight: " + str(earth_weight*Venus))
elif planet_number == 3:
  print("destination weight: " + str(earth_weight*Mars))
elif planet_number == 4:
  print("destination weight: " + str(earth_weight*Jupiter))
elif planet_number == 5:
  print("destination weight: " + str(earth_weight*Saturn))
elif planet_number == 6:
  print("destination weight: " + str(earth_weight*Uranus))
elif planet_number == 7:
  print("destination weight: " + str(earth_weight*Neptune))
else:
  print("Invalid planet number" )