for nombre in range (1,101):
    fizz = not nombre % 3
    buzz = not nombre % 5
 
    if fizz and buzz :
        print ("FizzBuzz")
    elif fizz:
        print ("Fizz")
    elif buzz:
        print ("Buzz")
    else:
        print (nombre)