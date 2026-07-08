command=""
command=input('>')
while True:

    if command.upper()=="START":
        print("THE CAR IS STARTED")
        break
    elif command.upper()=="STOP":
        print("THE CAR IS STOPPED!")
        break
    elif command.upper()=="RESTART":
        print("THE CAR IS RESTARTED!")
        break
    elif command.upper() == "EXIT":
        print("THE CAR IS EXITED!")
        break
    elif command.upper()=='HELP':
        print("""" START THE CAR WITH START
        STOP THE CAR WITH STOP
        EXIT THE CAR WITH EXIT""")
        print(input(">"))
        break
else:
    print("THE CAR IS NOT STARTED")
    command = input("enter your command")