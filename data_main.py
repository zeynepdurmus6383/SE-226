from data_package import analyzer
from data_package import cleaner

userInput = input("Enter a comma-separated list of numbers")
cleanedList = cleaner.strip_whitespaces(userInput)
cleanedList = cleaner.remove_duplicates(cleanedList)

print("Mean:" , analyzer.calculate_mean(cleanedList))
print("Maximum:", analyzer.find_maximum(cleanedList))
print("Minimum:", analyzer.find_minimum(cleanedList))


