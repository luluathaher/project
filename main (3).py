appointments = []  # list to store appointments
while True:
    print("1. Add appointment")
    print("2. Show appointments")
    print("3. Delete appointment")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")
    if choice == "1":
        name = input("Enter patient name: ")
        date = input("Enter date: ")
        time = input("Enter time: ")
        appointments.append(name + " - " + date + " - " + time)
        print("Appointment added!\n")
    elif choice == "2":
        if len(appointments) == 0:
            print("No appointments.\n")
        else:
            print("Appointments list:")
            for i in range(len(appointments)):
                print(i+1, appointments[i])
            print()

    elif choice == "3":
        if len(appointments) == 0:
            print("No appointments to delete.\n")
        else:
            for i in range(len(appointments)):
                print(i+1, appointments[i])
            num = input("Enter number to delete: ")
            if num.isdigit():  
                num = int(num)
                if 1 <= num <= len(appointments):
                    appointments.pop(num-1)
                    print("Appointment deleted!\n")
                else:
                    print("Invalid number.\n")
            else:
                print("Please enter a number.\n")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1-4.\n")
