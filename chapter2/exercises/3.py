"""
Write a program that returns the total charge to a customer depending on the number of new videos($3.00) and old videos ($2.00) they've bought.
"""
newVideos = int(input('Enter number of new video rentals: '))
oldVideos = int(input('Enter number of old video rentals: '))

totalCharge = (newVideos * 3) + (oldVideos * 2)
totalCharge = "{:.2f}".format(totalCharge)
print('Total: $' + str(totalCharge))