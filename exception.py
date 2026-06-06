while True:
    try:
        x=int(input("Enter a number: "))

    except ValueError:
        print("Enter a integer!!")

    else:
        print(f"x is {x}")
        break
        
