try:
  fileName = input("Enter a file name: ")
  with open(fileName, "r") as f:
    lineNumber = 1
    for line in f:
      print(f"LINE NUMBER : {lineNumber}")
      print(line.upper())
      lineNumber += 1
except FileNotFoundError:
  print("Sorry, there is no such file!")

# -------------------------------------------------

current_file = "mbox.txt"

hosts = set()
with open(current_file, "r") as file:
  for line in file:
    if line.startswith("From:"):
      email_account = line.split()[1]
      hostName = email_account.split("@")[1]
      hosts.add(hostName)
      
for hostName in hosts:
  print(hostName)

print(f"Total {len(hosts)} hosts printed")

# ----------------------------------------------------



try:
    filename = input("Enter a file name: ")
    spam_scores = []

    with open(filename, "r") as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                spam_score = float(line.split(":")[1])
                spam_scores.append(spam_score)

except FileNotFoundError:
    print("Sorry, this file does not exist.")
    exit()

if not spam_scores:
    print("No emails found in file.")
    exit()

average_spam_score = sum(spam_scores) / len(spam_scores)

print(f"Average spam confidence: {average_spam_score}")

