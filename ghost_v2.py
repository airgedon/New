try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error, please enter numeric input")
    exit()


if hours >= 40:
    extra_hours = hours - 40#(hours)
    standard_hours_pay =  rate * 40#(hours)
    extra_hours_pay = rate * extra_hours * 1.5#(times)
    salary = standard_hours_pay + extra_hours_pay
    print(salary, "USD")
else:
    salary = hours * rate
    print(salary, "USD")

# ----------------------------------------------------------


try:
    score = int(input("Enter score: "))
except:
    print("Error, please enter numeric input")
    exit()
else:
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


# -----------------------------------------------------------
values = []


while True:
	try:
		value = input("Enter a number 'for completing the loop - type * done * '): ")
		if value == "done":
			break
		else:
			value = float(value)
			values.append(value)
	except:
		print("Invalid input. Enter a number")

total = 0
count = 0
for value in values:
	total = total + value
	count = count + 1

average_input = total / count
print("Average of input numbers: ", average_input)





