hours= int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

salary = hours * rate

print("Salary: ", salary)

# ----------------------------------------------

celsius = int(input("Enter Celsius Temperature: "))

print("Fahrenheit Temperature :", celsius * 9 / 5 + 32)

# -------------------------------------------------

sec_input = int(input('Enter seconds: '))

hour = sec_input // 3600 
minute = (sec_input % 3600) // 60
second = (sec_input % 3600) % 60

print( sec_input, "second(s) is", hour , "hour(s)", minute, "minute(s)",second, "second(s)\n" )
