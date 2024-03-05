#BinarySearch
import random

def BinarySearch(list_to_search, value_to_search, list_has_only_unique_values):
    value_idx = -1
    min_idx = 0
    max_idx = len(list_to_search) - 1
    
    while min_idx <= max_idx:
        half_idx = (min_idx + max_idx) // 2
        
        if value_to_search == list_to_search[half_idx]:
            if list_has_only_unique_values:
                return half_idx
            else:
                value_idx = half_idx
                max_idx = half_idx - 1
        elif value_to_search < list_to_search[half_idx]:
            max_idx = half_idx - 1
        else:
            min_idx = half_idx + 1
            
    return value_idx
    
min_value = 0
max_value = 0

input_values = int(input("Do you wish to input the values or generate random ones? (type 1 to input, or type 0 to generate random values) ")) > 0

if not input_values:
    min_value = int(input("Type the minimum value you want to be randomly generated: "))
    max_value = int(input("Type the maximum value you want to be randomly generated: "))

list_size = int(input("How many values do you want on the list? "))
values_list = []

if input_values:
    print("\nDigite os valores:")
    for i in range(list_size):
        values_list.append(int(input(f"{i+1}: ")))
else:
    for i in range(list_size):
        values_list.append(random.randint(min_value, max_value))
        
values_list.sort()

print()

for idx, value in enumerate(values_list):
    print(f"Value {idx+1} (Idx: {idx}): {value}")
    
unique_values = int(input("\nAre the values in the list unique? (1 - Yes; 0 - No) ")) > 0
search = int(input("\nType a value to search in the list (-1 to exit): "))
while search > -1:
    searched_value_idx = BinarySearch(values_list, search, unique_values)
    
    if searched_value_idx > -1:
        print(f"Value {search} found at idx: {searched_value_idx}")
    else:
        print("Value not found")
    
    search = int(input("\nType a value to search in the list (-1 to exit): "))
        
print("\nProgram finished")
