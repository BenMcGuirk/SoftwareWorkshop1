"""
Write a program representing how far a bouncy ball has travelled. The 'bounciness' is determined by a ratio of its height 
dropped against the height reached after bouncing. For example if its dropped from 10m and bounces 6m, its ratio is 0.6.
Allow user to input the inital height and the number of times its allowed to bounce, and return total distance travelled 
by the ball.
"""
height = int(input('Enter the height: '))
numberOfBounces = int(input('Enter the number of bounces: '))
totalDistance = 0

for bounce in range (numberOfBounces):
    totalDistance += height
    height *= 0.6 
    totalDistance += height

print(totalDistance)
