#This file summaries the study data
outcomes = ["s", "h", "h", "s", "h"]

num_people = len(outcomes)
print(f"There are {num_people} patients.")
#len() returns the number of elements in a list
#len() is a built-in function

num_sick = outcomes.count("s")
print(f"{num_sick} people are sick.")
#count() returns the number of times a value appears in a list
#count() is a method of the list class

ages = [34, 61, 34, 29, 40, 19]
ages.count(29)
print(f"29 appears {ages.count(29)} times in the ages list.")
print(f"There are {len(ages)} patients.")


list1 = ["a", "b"]
print(list1)
list2 = list1.copy()
print(list2)
list1[0] = "c"
print(list1)

outcomes_old = outcomes.copy()

outcomes[3] = "h"

print(outcomes_old)
print(outcomes)

patients = ["davis", "lee", "jones", "bell", "garcia"]

sorted(patients)
#sorted() is a function that returns a new sorted list from the elements within the variable
#sorted() does not modify the original list

print(f"First subject: \n{sorted(patients)[0].title()}")
#this will print the first subject in the sorted list in title case with a line break separating it from the rest of the text

#there are also other reordering methods such as sort() and reverse(); however, these methods modify the original list


parameters = (300, "daily", "chewable")
#this is a tuple
#tuples are used to store multiple items in a single variable
#a tuple is a data structure that is similar to a list, but it is immutable (cannot be changed)
#tuples are created using parentheses instead of square brackets
#tuples can be indexed and sliced like lists
#only tuples contain commas and parentheses
#if you know how many elements you need to store and you know their types, you can use a tuple (instead of a list) to store them
#if you have a tuple and you want to convert it to a list, you can use the list() function
#for example, you can convert a tuple to a list like this:
parameters_list = list(parameters)
#this will create a new list with the same elements as the tuple
#this will not modify the original tuple
#you can also convert a list to a tuple like this:
parameters_tuple = tuple(parameters_list)
#this will create a new tuple with the same elements as the list
#this will not modify the original list
#you can also use the tuple() function to create a tuple from a list
#for example, you can create a tuple from a list like this:
parameters_tuple = tuple([300, "daily", "chewable"])
#this will create a new tuple with the same elements as the list