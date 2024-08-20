words = input().split()
odd_occurrences = {}

for element in words:
    word_lower = element.lower()
    if word_lower not in odd_occurrences:
        odd_occurrences[word_lower] = 0
    odd_occurrences[word_lower] += 1
for key,value in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=' ')