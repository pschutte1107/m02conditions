for x in range (3, -1, -1):
    print(x)

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    elif number > guess_me:
        print("oops")
        break
    number +=1


guess = 5
for num in range(0, 15):
    if num < guess:
        print("too low")
    elif num == guess:
        print("found it!")
        break
    elif num > guess:
        print("oops")
        break