command=input('enter your command')
command=('START STOP QUIT')
i=command
while command!='STOP QUIT':
    command.upper()=="START"
    print("THE CAR IS STARTED!")
    if command.upper()=="STOP":
        print("THE CAR IS STOPPED!")
    elif command.upper()=="Quit":
        print("THE CAR IS QUIT!")

else:
    print("THE CAR IS NOT STARTED!")