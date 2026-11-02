low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    guess = (low + high) // 2

    print("My guess is:", guess)
    feedback = input("Enter (H)igher, (L)ower or (C)orrect: ").lower()

    if feedback == 'c':
        print("Number guessed successfully!")
        break
    elif feedback == 'h':
        low = guess + 1
    elif feedback == 'l':
        high = guess - 1
    else:
        print("Invalid input! Try again.")

else:
    print("Invalid feedback or inconsistent answers.")