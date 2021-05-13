
#Name: Michael Moyo
#Lab: lab assignment 3, sorting it all out
#Purpose: using python to sort out data
#Date: 15/05/2019

def partition(the_list, p, r, compare_func): #partition the list containing cities' information

    i = p - 1

    j = p

    pivot = r #the last index in the list

    while j < r: #loops through the list, comparing and swapping the value at index = pivot with other values in the list. Also, the loops terminates when j == r.

        if compare_func(the_list[j], the_list[pivot]):

            j += 1

        elif compare_func(the_list[pivot], the_list[j]):

            temporal = the_list[i+1]
            the_list[i+1] = the_list[j]
            the_list[j] = temporal
            i += 1
            j += 1

    temporal = the_list[i + 1]
    the_list[i + 1] = the_list[pivot]
    the_list[pivot] = temporal
    return i + 1

def compare_func(x, y): #returns true when x is greater than y

    return x > y


def quick_sort(the_list, p, r, compare_func): #calls the partition function to evaluate index == pivot. Also, recursively calls itself to divide and sort the list

    if p < r:

        pivot = partition(the_list, p, r, compare_func)

        quick_sort(the_list, p, pivot - 1, compare_func)

        quick_sort(the_list, pivot + 1, r , compare_func)


def sort(the_list, compare_func): #calls the quicksort function and gives it the instance variables p = 0 and r = len(the_list) - 1

    quick_sort(the_list, 0, len(the_list) - 1, compare_func)









