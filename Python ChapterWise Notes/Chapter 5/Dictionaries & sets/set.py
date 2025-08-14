s = {1,3,4,6,"magnetic",12}
print(type(s))

new_set = s.copy()
print(new_set)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union => {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection => {3, 4}
print(a - b)  # Difference => {1, 2}
print(a ^ b)  # Symmetric Difference => {1, 2, 5, 6}
print(a.isdisjoint(b))  # Check if disjoint => False
print(a.issubset(b))  # Check if a is subset of b => False
print(a.issuperset(b))  # Check if a is superset of b => False

