x = input("Enter an amount of seconds to convert:")
y = int(x)
seconds = y%60
totalMinutes = y//60
minutes = totalMinutes%60
hours = totalMinutes//60
print(y , "seconds is " , hours , " hours, " , minutes , " minutes, and " , seconds , " seconds.")
