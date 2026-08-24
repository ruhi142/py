#expense tracker project

expenses = [] #list of all expense in form of dictionary
print("welcome to expense tracker : spend less, save more")

while True:   #we can click an option (save/expense) etc again and again
    print("==MENU==")
    print("1. add expense")
    print("2. view all expense")
    print("3. view total expenditure")
    print("4. exit")

    choice = int (input("pls enter your choise : "))

    #1. add expense
    if (choice==1):
        date= input("expend on which date: ")
        category= input("which category?: (food/travel)")
        description= input("details: ")
        amount= float(input("enter the amount: "))

        expense= {              #dictionary key
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense) #1st list name then append then keyname of dictionary which is expense
        print("\n expense is added succesfully")

    #2. view all expense 
    elif (choice==2):
        if( len(expenses) ==0 ):
            print("1st do spend")
        else:
            print(" == this is your all expense== ")
            count = 1
            for eachspending in expenses: #for loop to count all expense, eachspend is a variable which will store each expense in the list
                print(f"spending {count} -> {eachspending["date"]}, {eachspending["category"]}, {eachspending["description"]}, {eachspending["amount"]}")
                count= count+1

    #3. view total expenditure
    elif (choice==3):       
          total = 0 
          for eachsepending in expenses:
              total= total+eachspending["amount"] #how many amount will be spend can be counted by total expenditure

          print("\n total expenditure = ", total)

        
    #4. exit
    elif(choice==4):
        print("thank you for using expense tracker")
        break
    else:
        print("invalid choice, pls try again")