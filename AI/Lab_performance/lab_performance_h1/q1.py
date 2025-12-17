def count_vowels_consonants(text):
    vowels_count = 0
    consonants_count = 0
    
    
    vowels = "aeiou"
    
    for char in text:
        if char.isalpha():  
            if char.lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
                
    return vowels_count, consonants_count


user_input = input("Enter a string: ")
v, c = count_vowels_consonants(user_input)

print("-" * 20)
print(f"Vowels: {v}")
print(f"Consonants: {c}")