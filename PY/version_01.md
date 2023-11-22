```python
list = [1,3,4,53,32]
print(list[3:4])
del list[3:4] 
print(list)
list_02 = [32,434,243,213213]

print(sum(list))
print(list)

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")

print(x)


print(list[1:4])
print(list[2:])
print(list[:4])

print(3 in list) # False

list[0] = 3
print(list)

fruits = ['apple','pear','pineapple']

for i in fruits:
    print(i)

numbers = [34,23,123,3432,45,33,231]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

print(len(numbers))

test = ['demi',2,[1,2,3],['d','f','g','r']]

print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[3][-4])
print(test[2][1])
print(test[3][2])
print(test[3][3])

def func(x):
    return x % 3

list = [3,4,5,6,9,10]
print("Normal sort: ", sorted(list) )
print("Sort by key: ", sorted(list, key=func))

def func(x):
    return x % 7

my_list = [15, 3, 11, 7]
print("Normal Sort : ", sorted(my_list))
print("Sort by key: ", sorted(my_list, key=func)) 
```


```py
students = {}
print(students)
students['name'] = 'steve'
print(students)
s_list = [('name', 'steve'), ('age', '32')]
s_dict = dict(s_list)
print(s_dict)
```

```py
my_dict = {'name': 'Steve', 'age':34 }

print(len(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
```

```py
my_dict = {'name': 'Steve', 'age':34,'id': '2832'}
print('name' in my_dict)
del my_dict['name']

print(my_dict)

if 'name' in my_dict:
    del my_dict['name']
else:
    print("name is not in dic")
```

```py
my_dict = {'banana': 2, 'apple': 3, 'pear': 1}

sorted_dict = sorted(my_dict)
print(sorted_dict) # ['apple', 'banana', 'pear']

sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict) # {'apple': 3, 'banana': 2, 'pear': 1}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict) # {'pear': 1, 'banana': 2, 'apple': 3}
```

```py
m_string = "bravo bravo my life"
c_dict= dict()
for i in m_string:
    if i == " ":
        continue
    if i not in c_dict:
        c_dict[i] = 1
    else:
        c_dict[i] = c_dict[i]+1

print(c_dict) # {'b': 2, 'r': 2, 'a': 2, 'v': 2, 'o': 2, 'm': 1, 'y': 1, 'l': 1, 'i': 1, 'f': 1, 'e': 1}
```

```py
fhand = open("doremi3.txt")
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1

print(counts)

s_counts = sorted(counts.items())
print(dict(s_counts))
```

```py
s_dict = {'name': 'steve', 'age': 18, 'id': '2354'}

for i in s_dict:
    print(i, ":", s_dict[i])
```
