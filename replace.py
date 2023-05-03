
# initializing string
test_str = 'red-blue-orange-white-black'

# printing original string
print("The original string is : " + str(test_str))

# initializing Delimiter
c = "-"

# joining the sorted string after split
a=test_str.split("-")
d=sorted(a, reverse=True)
print(d)
b=c.join(d)
print(b)

'''
res = delim.join(sorted(test_str.split('-')))

# printing result
print("The sorted words : " + str(res))
'''
