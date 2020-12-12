class Budget:

    def __init__(self):
        self.amount = 0

    def validity():
        print("Enter a valid option.")
        return


class functions(Budget):
    def Income(self):
        print("Enter the income: ")
        income = input()
        self.amount = self.amount + income

    def Expense(self):
        print("Enter the amount spend: ")
        spend = input()
        self.amount = self.amount - spend

    def Balance(self):
        print(self.amount)

    def Decide_Reset(self):
        print("This command will erase all data. Do you want to continue ?")
        print("\nPress 0 to return\nPress 1 to reset data")
        reset = input()
        if(reset == 0):
            return
        elif(reset == 1):
            self.amount = 0
        else:
            print("Enter a valid option")

    def Exit(self):
        print("Are you sure you want to quit ?")
        print("\nPress 0 to return to menu\nPress 1 to quit")
        exit = input()
        if(exit == 1):
            exit(0)
        else:
            return

    def Menu(self):
        print("Select an Option: \n1.Income\n2.Expenditure")
        print("3.Balance\n4.Reset Data\n5.Exit\n")

var = 0
object_1 = functions()
object_1.Menu()
option = int(input())
while(option > 0):
    if(var == 1):
        object_1.Menu()
        option = int(input())
    var = 1
    if(option == 1):
        object_1.Income()
        print("Press any key")
        input()
        continue
    elif(option == 2):
        object_1.Expense()
        print("Press any key")
        input()
        continue
    elif(option == 3):
        object_1.Balance()
        print("Press any key")
        input()
        continue
    elif(option == 4):
        object_1.Decide_Reset()
        print("Press any key")
        input()
        continue
    elif(option == 5):
        object_1.Exit()
    else:
        object_1.validity()
        print("Press any key")
        input()
