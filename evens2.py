def even_number_of_evens(numbers):
    if numbers == []:
        return False 
    else:
        evens = 0
        
    for n in numbers:
        if n % 2 == 0:
            evens += 1
    
    return evens %2 == 0        
    
    
assert even_number_of_evens([]) == False, "no numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")