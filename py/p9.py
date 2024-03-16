import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of unique lowercase letters in the input string
    str_set = set(c.lower() for c in str1 if c.isalpha())
    
    # Convert the alphabet string to a set
    alphaset = set(alphabet)
    
    # Check if all the letters in the alphabet set are present in the input string set
    return alphaset <= str_set

# Test the function
print(ispangram('The quick brown fox jumps over the lazy dog'))  # Output: True
