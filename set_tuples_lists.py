#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana","coconut" ]
# print(dir(fruits))#gives options on what you can do with the list
# print(help(fruits))#helpful information about the function
# print(len(fruits)) #length of the list


# print(fruits[::2])  #every second fruit
# print(fruits[::-1]) #makes the list reversed


for fruit in fruits:
    print(fruit) 

print("apple" in fruits) 

# fruits[0] = "pineapple" #Changes the value in () to the word in the ""
fruits.append("pineapple") # Appends/Adds the word to the end of the list
fruits.remove("apple")#Removes said word from the list
fruits.insert(0,"pineapple") #Inserts it into that position, moving everything over by one
fruits.sort#Puts everything in alphabetical order
fruits.reverse() #reverses list

for fruit in fruits:
    print(fruit)    #prints the entire list one over the other