#module used for square root function
import math

#Function taking multiple user inputs (on multiple different lines) and parsing it into a list
def read_list():
    #empty lists for storing user inputs
    nums = []
    nums_int = []

    #user input
    number = input()
    #loops until user hits enter
    while number != "":
        #adds input to the list, separates each input by a space
        nums.append(number.split(sep=" "))
        number = input()
    #for loop adding all values to another list
    for i in sum(nums, []):
      #appends the integer version of all the numbers (without spaces) to another list
      nums_int.append(float(i))
    return nums_int

#Function finding the mean/average of the numbers in the list
def get_mean(nums_int):
    sum = 0
    count = 0
    #for loop iterating through all the numbers in the list
    for n in nums_int:
        #Adding each number to the sum
        sum += n
        #counting how many numbers are in the list
        count += 1
    #returns the mean/average
    return sum/count

#Function finding the range of the numbers in the list
def get_range(nums_int):
    return max(nums_int) - min(nums_int)
    #Last index - first index

#Function finding the median of the numbers in the list
def get_median(nums_int):
    # if list length is odd
    if len(nums_int) % 2 == 1:
        return nums_int[len(nums_int) // 2]
    # list length is even
    left = nums_int[len(nums_int) // 2 - 1]
    right = nums_int[len(nums_int) // 2]
    return (left + right) / 2

#Function finding the standard deviation of the numbers in the list
def get_std_dev(nums_int):
  #finding the mean
  mean = get_mean(nums_int)
  squared_distances = []
  #for loop for looping through the list of numbers
  for num in nums_int:
    #finds squared distance of each point to the mean
    squared_distances.append((mean-num)**2)
  mean_of_distances = get_mean(squared_distances)
  #uses the math module for the sqare root function
  return math.sqrt(mean_of_distances)

def main():
    #Greeting print statement
    print("Welcome to the Stats Calc! Enter a list of nums: ")
    #creates the initial list
    mylist = read_list()
    #all the supported functions for the list
    mean = get_mean(mylist)
    range  = get_range(mylist)
    median = get_median(mylist)
    standard_deviation = get_std_dev(mylist)
  
    #prints all the calculated values of the list
    print(f"Mean: {mean:.2f}")
    print(f"Range: {range:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {standard_deviation:.2f}")

main()
