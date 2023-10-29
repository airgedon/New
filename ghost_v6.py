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

# -----------------------------------------------------------------------


with open("romeo.txt", "r") as fhand:
    
    my_list = fhand.read().split()
    
    new_word = input("Enter a new word to add to my list: ")
    
    if new_word not in my_list:
        my_list.append(new_word)
        print(sorted(my_list))        
    else:
        print("The word is already in my list")


# ---------------------------------------------------------------------------

with open("mbox.txt", "r") as fhand:
    
    count = 0
    for line in fhand:
        if line.startswith("From:"):
            line = line.replace("From:", "")
            print(line.rstrip())
            count += 1
    print("Total %d lines were printed" %count)

# ---------------------------------------------------------------------------


my_list = []

while True:
    try:
        num_input = input("Please enter an integer(done to quit): ")
        if num_input == "done":
            print("------------------Bye!!---------------------")
            break
        else:
            num_input = int(num_input)
            my_list.append(num_input)
            total = 0
            count = 0
            for num_input in my_list:
                total += num_input
                count += 1
                
            average_num_input = total / count
            print(my_list,", average = ", average_num_input)
    except ValueError:
        print("Please, enter numeric input")
        

        


