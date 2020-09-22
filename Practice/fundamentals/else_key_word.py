# else in a for loop
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "fautly":
        print("Stopping the production line!")
        all_succesful = False
        break
    print(f"This car is {status}.")
    print("Shipping new acr to customer!")

else:
    print("All cars built succesfully.No faulty cars!")

# for loops to find mathematical numbers / primenumbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")