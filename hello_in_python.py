print ('Hello World \n')
import time

def hello():
    a = input("Enter a string to print: ")
    print(a)

ask = input("Do you want to print a statement? (Y or N): ")
if ask.lower() == "y":
    start_time = time.time()
    hello()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

    ask2 = input("Do you want to print more? (Y or N): ")
    if ask2.lower() == "y":
        start_time = time.time()
        hello()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
    else:
        print("Thank you!")

    ask3 = input("Do you want to print more? (Y or N): ")
    if ask3.lower() == "y":
        start_time = time.time()
        hello()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
    else:
        print("Thank you!")
else:
    print("Thank you!")

