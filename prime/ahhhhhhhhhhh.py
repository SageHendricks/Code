from math import floor
try:
    user_input = int(input ("input a number to check if its prime \n> "))
    user_input = 2**13 - 1
except ValueError:
   print("youre not nice :grumpy face: goodbye.")
else:
    output = "prime"
    for a in range(2, floor(pow(user_input,0.5))) :
        print(f"{a} out of {floor(pow(user_input,0.5))}: {floor(a*100000000/floor(pow(user_input,0.5)))/1000000}%")
        if (user_input % a) == 0:
            output = "not prime " + str(a)
            break
    print (output)