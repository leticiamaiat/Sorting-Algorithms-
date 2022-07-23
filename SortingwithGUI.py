from tkinter import *
from tkinter import ttk
import numpy as np
import time



def show(n: int, data: list, colours: list):

	# n is length of the array data
	# data is the array itself
	# colours is an array of colors
	canvas.delete('all')

	#width of each bar
	width = 1560/(3*n-1)

	#spacing between the bars
	gap = width/2

	for i in range(n):

		#display an array of "bar"
		canvas.create_rectangle(7+i*width+i*gap, 0, 7 +
								(i+1)*width+i*gap, data[i],
								fill=colours[i])
	
	# this function will help us to see every step
	# of the sorting algorithm
	# the purpose of this function is to update the screen
	# in runtime
	win.update_idletasks()


def shuffle():
	np.random.shuffle(arr)
	show(N, arr, color)

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                show(N, arr, ['yellow' if x == j+1 else 'grey' for x in range(N)])
                time.sleep(1/speed)	
                    

def mergesort(arr, left, right):
	if left < right:
		m = (left+right)//2
		mergesort(arr, left, m)
		mergesort(arr, m+1, right)

		j = m+1
		if arr[m] <= arr[m+1]:
			return

		while left <= m and j <= right:
			show(N, arr, ['yellow' if x == left or x ==
						j else 'grey' for x in range(N)])
			time.sleep(1/speed)
			if arr[left] <= arr[j]:
				left += 1
			else:
				show(N, arr, ['red' if x == left or x ==
							j else 'grey' for x in range(N)])
				
				# array of colours where only the focused bars
				# are displayed red since left >arr[j]
				time.sleep(1/speed)
				temp = arr[j]
				
				# storing the smaller element in temp variable
				i = j
				while i != left:
					arr[i] = arr[i-1]
					show(N, arr, ['red' if x == i or x ==
								j else 'grey' for x in range(N)])
					time.sleep(1/speed)
					i -= 1
				
				# this while loop will shift all the elements one step
				# to right to make the place empty for the temp variable
				# upon reaching the desired location
				arr[left] = temp

				show(N, arr, ['green' if x == left or x ==
							j else 'grey' for x in range(N)])
				time.sleep(1/speed)
				left += 1
				m += 1
				j += 1

# Function to find the partition position
def partition(arr, low, high):
  
  # Choose the rightmost element as pivot
  pivot = arr[high]
  
  # Pointer for greater element
  i = low - 1
  
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if arr[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
  
      # Swapping element at i with element at j
      (arr[i], arr[j]) = (arr[j], arr[i])
  
  # Swap the pivot element with the greater element specified by i
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  
  # Return the position from where partition is done
  return i + 1
  
# Function to perform quicksort
def quick_sort(arr, low, high):
  if low < high:
  
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(arr, low, high)
  
    # Recursive call on the left of pivot
    quick_sort(arr, low, pi - 1)
  
    # Recursive call on the right of pivot
    quick_sort(arr, pi + 1, high)


# this function call the mergesort function which will
# start the animation.
def start():
	a = value_inside.get()
	if a == "Merge Sort":
		mergesort(arr, 0, N-1)
	elif a == "Bubble Sort":
		bubbleSort(arr)
	elif a == "Heap Sort":
		print("ok heap")
	
	show(N, arr, ['blue' for _ in range(N)])


# Function to print the submitted option-- testing purpose

	

win = Tk()


# Create the list of options
options_list = ["Merge Sort", "Bubble Sort", "Heap Sort", "Merge Sort"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = StringVar(win)

# Set the default value of the variable
value_inside.set("Select an Option")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = ttk.OptionMenu(win, value_inside, *options_list)
question_menu.pack()




N = 20 # length of the array
speed = 20 # how fast the array will be sorted

# creating the array using linspace function
# from numpy
arr = np.linspace(10, 390, N, dtype=np.uint16)

color = ['grey' for _ in range(N)]

ttk.Label(win, text='Sorting visualizer').pack()
canvas = Canvas(win, width=800, height=400, bg='black')
canvas.pack()

ttk.Button(win, text='Start sorting', command= start).pack(
	side='right', padx=5, pady=5)

ttk.Button(win, text='Shuffle array', command=shuffle).pack(side='right')
shuffle()
show(N, arr, color)

win.mainloop()
