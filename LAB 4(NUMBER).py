def check_number(num):
    if num == 0:
        print("The number is Zero.")
    elif num % 2 == 0:
        print (f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
        
while True:
        num = int(input("Ente your number."))
        check_number(num)