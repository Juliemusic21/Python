#Julie Sakai
#Module 11.2 Assignment

def print_recursive(n):
    if n > 0:
        #Display number from 1 up to n - 1. 
        print_recursive(n - 1)
        #Display the value for n.
        print(n)

def print_non_recursive(n):
    #Display number from 1 up to and including n.
    for i in range(1, n + 1):
        print(i)

#Call the main function. 
if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            #Input a positive number great than 0.
            #This will not allow a nagative or 0 value. 
            print("Please enter a positive integer greater than 0.")
        else:
            #Display the recursive function is being invoked.
            print("Invoking recursive function:")
            print_recursive(num)
            #Display the non-recursive function is being invoked. 
            print("\nInvoking non-recursive function:")
            print_non_recursive(num)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
    