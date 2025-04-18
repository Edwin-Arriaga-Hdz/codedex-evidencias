
for i in range(1, 101, +1):
  output = ""
  if i % 3 == 0:
    output += "Fizz"
  if i % 5 == 0:
    output += "Buzz"
  if i % 7 == 0:
    output += "Bazz"
  if output == "":
    print(i)
  else:
    print(output)