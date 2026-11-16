
total = 0
count = 0

while True:
    price = float(input("Price (0 to stop): "))

    if price == 0:
        break

    total += price
    count += 1

if count > 0:
    average = total / count
else:
    average = 0

print("Items:", count)
print("Total:", format(total, ".2f"))
print("Average:", format(average, ".2f"))
