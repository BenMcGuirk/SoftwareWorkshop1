newVideos = int(input('Enter number of new video rentals: '))
oldVideos = int(input('Enter number of old video rentals: '))

totalCharge = (newVideos * 3) + (oldVideos * 2)
totalCharge = "{:.2f}".format(totalCharge)
print('Total: $' + str(totalCharge))