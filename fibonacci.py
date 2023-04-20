import time
#fibonacci sequence
def fibonacci(y):
    start = time.time()
    #print(start)
    x = y + 1
    my_dict = {1: 0, 2:1}
    for i in range(3, x):
        my_dict[i] = my_dict[i-2] + my_dict[i-1]
    fibonacci_list = list(my_dict.values())
    print("\n")
    print(fibonacci_list)
    end = time.time()
    total_time = end - start
    print("\n"+ str(total_time))

#code
while True:
    r_extreme = int(input("Enter lenght of Fibonacci series\n"))
    if r_extreme <= 100:
        fibonacci(r_extreme) 
        break   
    else:
        print("\nyour input is too high! Try again")
        choice = input("\nContinue?y/n")
        if choice == "y":
            continue
        else: 
            break

