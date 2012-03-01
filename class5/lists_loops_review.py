"""
loops_lists_review.py

1. Create a list of numbers
2. Append a number to that list of numbers
3. Get the length of the list
4. Loop through the list and return the number minus 1
"""
a = range(10)
a.append(12)
b = len(a)
print b
print len(a)
for c in a:
	print c - 1