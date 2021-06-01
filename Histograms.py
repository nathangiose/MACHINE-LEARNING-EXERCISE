# Nathan John Giose
# Importing matplotlab as mp

import matplotlib.pyplot as mp
# Inserting data as variables


nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
# Inserting the title, and labels for the x and y axis

mp.xlabel("nums")
mp.ylabel("bins")
mp.title("Histogram of nums against bins")
# Sorting the data with its relevance (Histogram)


mp.hist(nums, bins, color="Aqua")
# Displaying the data in a GUI
mp.show()
