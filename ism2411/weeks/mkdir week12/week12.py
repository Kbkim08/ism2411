import csv
import os

folder = os.path.dirname(__file__)
csv_file = os.path.join(folder, "data", "sales.csv")

with open(csv_file, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


### Exercise 2
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

### Exercise 3
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    for row in reader:
        print(row)


### Exercise 4

import csv

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} unit x ${price:.2f} = ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")


### Exercise 5
import csv

row_written = 0
total_rows = 0

with open("data/sales.csv" , "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    with open("data/cleaned.csv" , "w" , newline = "") as new_file: 
        writer = csv.writer(new_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows +=1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                rows_written +=1

print(f"Rows written: {rows_written}")
print(f"Original rows: {total_rows}")

### Exercise 6

import csv

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

print(f"Total Revenue: ${total_revenue:.2f}")

# csv.reader uses index like row[0]
# csv.DictReader uses column names. It makes code easier to read.

### Exercise 7

import csv

summary = {}

with open ("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["Price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in summary:
            summary[product] += total
        else:
            summary[product] = total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

### Exercise 8

import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv" , "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_revenue += float(row["price"]) * int(row["quantity"])

    with open("data/run_log.txt" , "a") as log:
        log.write(
            f"{datetime.now()} | Total Revenue = ${total_revenue:.2f}\n"
        )

print("Updated Log")


## Reflection:

# Question 1
# Python and Execl can both be used to analyze data, 
# but python is better for automating repetitive tasks
# while Excel is better for quickly viewing or editing 
# or creating data charts. Python is efficient at this as well
# but it needs to be repeated many times.

#Question 2
# A business could use append mode to track sales reports or
# system activity. 

# Append is useful because it adds new records to end of a file 
# without deleting previous ones.