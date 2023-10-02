try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    exit()

def computepay(hours,rate):
    if hours >= 40:
        extra_hours = hours - 40
        standard_hours_pay =  rate * 40
        extra_hours_pay = rate * extra_hours * 1.5
        salary = standard_hours_pay + extra_hours_pay
        print(salary, "USD")
    else:
        salary = hours * rate
        print(salary, "USD")


computepay(hours,rate)

# ----------------------------------------------------------

try:
    test_score = int(input("Enter your test`s score: "))
except:
    print("Error, please enter numeric input")
    exit()


def get_score(score):
    if score > 100 or score < 0:
        print("Error, please enter numeric input between 0 and 100")
    elif score >= 90:
        print("Grade is A")
    elif score >= 80:
        print("Grade is B")
    elif score >= 70:
        print("Grade is C")
    elif score >= 60:
        print("Grade is D")
    else:
        print("Grade is F")


get_score(test_score)


# -----------------------------------------------------------


def num_divide3(num):
    result = 0            
    for i in range(1, num + 1):
        if i % 3 == 0:
          result = result + 1
    return result

def check_positive(num):
    if num > 0:
        return True
    else:
        return False
    
while True:
    
    num_input = input("Enter a positive integer: ")
    if num_input.lower() == "done":
        print("Bye !")
        break
        
    try:
        num_input = int(num_input)
        
        if not check_positive(num_input):
            print("Please, enter a positive number, not a negative one")
            continue
        
    except ValueError:
        print("Please, enter a number (for example 1,25,32) as an input")
        continue

    final_result = num_divide3(num_input)
    print(f"Numbers divisible by 3 among numbers from 1 to {num_input}: {final_result}")
            



