height = int(input('Enter the height: '))
numberOfBounces = int(input('Enter the number of bounces: '))
totalDistance = 0

for bounce in range (numberOfBounces):
    totalDistance += height
    height *= 0.6 
    totalDistance += height

print(totalDistance)
