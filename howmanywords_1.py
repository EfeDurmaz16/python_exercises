#Cisco online assessment practice 

def howManyWords(sentence):
    words = sentence.split()
    count = 1

    for word in words:
        if word.isalpha():
            count += 1

    return count


# Test cases
print(howManyWords("This is a test."))  # 4
print(howManyWords("This   is   a       test. 123 4 5  6 !!! ! ! "))  # 4
print(howManyWords("This is a test. 123!"))  # 4
print(howManyWords("This is a test. 123!@"))  # 4

# Output