genres = ["romcom", "action", "drama", "anime"]
#list data type, shown above, is a collection of items
#list is a mutable data type, meaning it can be changed
#list is an ordered collection of items, meaning the order of the items is preserved
#lists are defined using square brackets [], with items separated by commas
#list can contain any data type, including strings, integers, floats, booleans, and even other lists
#list can contain duplicate items
#lists can be empty

#lists can be indexed and sliced the same way as strings

genres_revised = []
genres_revised.append("western")
genres_revised.append("kung fu")

genres_revised.insert(1, "zombie")

genres_revised.append("musical")
genres_revised.insert(2, "scifi")

genres_revised.insert(-1, "biopic")


del genres_revised[3]
print(genres_revised)

genres_revised.remove("scifi")
print(genres_revised)

genres_revised.remove("western")

del_genres_revised = genres_revised.pop(1)
print(f"We deleted {del_genres_revised}s.")
print(genres_revised)

#note that the remove() method removes only the first occurrence of the item
#to remove all occurrences of an item, use a loop

#pop() method removes the last item in the list and returns it
#pop() method can also be used to remove an item at a specific index
#pop() method is useful when you want to remove an item from a list and use it later
#when no index is specified, pop() removes the last item in the list
#pop() method raises an IndexError if the list is empty