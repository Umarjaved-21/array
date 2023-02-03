# defining and declaring an array 
arr = [10,20,30,40,50]
print(arr)

#Accesing array element
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1]) # Negative Indexing
print(arr[-2]) #Negative indexing

brands = ["coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

# Finding the length of array
num_brands = len(brands)
print(num_brands)

# Adding an element to an array using append()
brands.append("Intel")
print(brands)

# Removing element from an array
colors = ["voilet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
del colors[4]
colors.remove("Blue")
colors.pop(3)
print(colors)
 
# Modifying element of an array using indexing
fruits = ["Apple", "Bnana", "Mango", "Grapes", "Orange"]
print(fruits)
fruits[1] = "Pineapple"
fruits[-1] = "lemon"
print(fruits)

# Concatenating two arrays using the + opperator
concat = [1,2,3]
print(concat)

concat + [4,5,6]
print(concat)

concat = concat + [4,5,6]
print(concat)

# Repeating element in arrays
repeat = ["Umar"]
print(repeat)

repeat = repeat * 5
print(repeat)

# Slicing an array
fruits = ["Apple", "Bnana", "Mango", "Grapes", "Orange"]
print(fruits)
print(fruits[1:4])
print(fruits[ : 3])
print(fruits[-4: ])
print(fruits[-3: -1])

# Declaring and defining multidumensional videos
multd = [[1,2],[3,4],[5,6],[7,8]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])
print(multd[3][0])

