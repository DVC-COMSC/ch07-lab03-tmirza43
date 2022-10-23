
# ******************************
# Make your Code
# ******************************

numbers = []
for i in range(5):
  numbers.append(int(input("Enter num: ")))

for n in range(5):
  if numbers[n] > (sum(numbers)/5):
    print(numbers[n], end = ' ')
