""" 
Make function bubble_sort using bubble sort algorithm to sort numbers given by user; order numbers into the ascending order.

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 

https://en.wikipedia.org/wiki/Bubble_sort


Example output:
Please Enter the Total Number of Elements : 5
Please enter the 0 Element : 4
Please enter the 1 Element : 3
Please enter the 2 Element : -1
Please enter the 3 Element : 9
Please enter the 4 Element : 6
The Sorted List in Ascending Order :  [-1, 3, 4, 6, 9]

"""


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all the elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we skip them
        for j in range(0, n - i - 1):
            # Sawp if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


a = []
number = int(input("Please Enter the Total Number of Elements: "))
for i in range(number):
    value = int(input("Please enter the %d Element : " % i))
    a.append(value)

print("The sorted List in Ascending Order : ", bubble_sort(a))
