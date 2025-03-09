# Question number 1 - how to flatten the deep nested list
def flatten(lst):
    
    return sum(([e] if not isinstance(e, list) else flatten(e) for e in lst), [])

nested_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

print(flatten(nested_list))

# Question number 2 - how to reverse a nested list

list = [[1, 2], [3, 4], [5, 6, 7]]

reversed_list = []

for i in reversed(list):
    reversed_list.append(i[::-1])
    
print (reversed_list)