from fuzzywuzzy import fuzz

string1 = "- Massena, New York - 0704"
string2 = "Massena"

ratio = fuzz.ratio(string1, string2)  # Simple ratio
partial_ratio = fuzz.partial_ratio(string1, string2)  # Best matching substring
token_sort_ratio = fuzz.token_sort_ratio(string1, string2) # Ignores word order
token_set_ratio = fuzz.token_set_ratio(string1, string2) # Ignores duplicates

print(f"Ratio: {ratio}") #40
print(f"Partial Ratio: {partial_ratio}") #67
print(f"Token Sort Ratio: {token_sort_ratio}") #56
print(f"Token Set Ratio: {token_set_ratio}") #100

# Example: Check if the similarity is above a threshold
if token_set_ratio > 70:  # Adjust threshold as needed
    print("Strings are likely similar")
else:
    print("Strings are likely different")