def count_upper_case(message):
    count = 0
    for rikduijm in message:
        if rikduijm.isupper():
            count += 1
    return count        
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 2, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"

print ("All the test passed")