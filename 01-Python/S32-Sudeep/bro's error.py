while True:
    try:
        a=float(input("What's x? "))
    except ValueError:
        print("Please enter a number")
    else:
        break
while True:
    try:
        b=float(input("What's y? "))
    except ValueError:
        print("Please enter a number")
    else:
        break
while True:
    c=input("x _ y ")
    if c == "+" or "-" or "*" or "/":   
        if c==("+"):
            print(a+b)
        if c==("-"):
            print(a-b)
        if c==("*"):
            print(a*b)
        if c==("/"):
            print(a/b)
    
    if c=="stop":
        break


