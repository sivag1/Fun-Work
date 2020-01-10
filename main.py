# Program to find type of Triangle formed by side lengths entered

# Function to return if a variable is number or not
def isNumber(side):
  try:
    int(side)
    return True
  except ValueError:
    return False

# Function to accept an Input and return that ONLY if it is a nu
def acceptSide(inputText):
  var = input(inputText)
  while not isNumber(var):
    var = input("Oops, only numbers are allowed, " + inputText)
  return var

# Accepting line or side lengths as input
side1 = acceptSide("Enter length of Side 1: ")
side2 = acceptSide("Enter length of Side 2: ")
side3 = acceptSide("Enter length of Side 3: ")

if side1 == side2 and side2 == side3:
  # All sides are equal
  print("Your triangle is equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
  # Any two sides are equal
  print("Your triangle is isoceles")
else:
  # No equal side
  print("Your triangle is scalene")