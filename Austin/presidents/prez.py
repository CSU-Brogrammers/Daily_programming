import numpy as np
counter = 0
index = [2, 4]

with open('presidents.csv', 'r') as f:
    content = f.read().splitlines()
    a = np.array = []
	b = np.array = []
    for line in content:
        a.append(line)
        counter = counter + 1

for word in a:
    print(word)
print(counter)

new_a  = np.delete(a,index)
print(new_a)
