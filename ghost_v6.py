def chop(my_list):
  my_list.remove(my_list[0])
  my_list.pop()
  return None

def middle(my_list):
  new_list = my_list[1:-1]
  return new_list

my_list = [1, 2, 3, 4]

print("my list before call chop function =>", my_list)
chop(my_list)
print("my list after call chop function =>", my_list)

my_list = [1, 2, 3, 4]
print("my list before call middle function =>", my_list)
middle(my_list)
print("my list after call middle function =>", my_list)

new_list = middle(my_list)

print("new list after call middle function =>", new_list)

-----------------------------------------------------------------------
