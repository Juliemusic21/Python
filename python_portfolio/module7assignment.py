#Julie Sakai
#07/23/2024
#Module 7.2 Assignment

def get_user_initials(full_name):
    # Split the full name into each own parts. 
    names = full_name.split()

    #Take the first letter of each part. 
    initials = [name[0].upper() for name in names]

    #Add a period after each initials.
    formatted_initials = '. '.join(initials)

    return formatted_initials

def main():
    #Get the user first, middle, and last name. 
    user_input = input("Enter your full name: ")
    print("Initials:", get_user_initials(user_input))

#Call the main function.
if __name__ == "__main__":
    main()