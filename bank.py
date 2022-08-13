from datetime import datetime

#Default Account with Account Balance with a list
#[HKD_availability, USD_availability. SGD_availability, HKD_amount,USD_amount,SGD_amount]
accountBalance = {"OSL_FEE":[0,0,0]}

#Transaction Information with [Date, Currency, Operation,Amount,timestamp]
transactionStatement = {}

#Action 1
def accountCreation():
    userName = askuserName()
    Currency = input("Please enter currency account that you want to create(HKD/USD/SGD): ")
    if(validateCurrency(Currency)):
        if(userName in accountBalance):
            if((Currency.upper() == "HKD")):
                accountBalance[userName][0] = True
                print("You created a HKD currency account successfully👍")
            if((Currency.upper() == "USD")):
                accountBalance[userName][1] = True
                print("You created a USD currency account successfully👍")
            if((Currency.upper() == "SGD")):
                accountBalance[userName][2] = True
                print("You created a SGD currency account successfully👍")
        if(userName not in accountBalance):
            if((Currency.upper() == "HKD")):
                accountBalance[userName] = [True, False, False,0,0,0]
                print("You created a HKD currency account successfully👍")
            if((Currency.upper() == "USD")):
                accountBalance[userName] = [False, True, False,0,0,0]
                print("You created a USD currency account successfully👍")
            if((Currency.upper() == "SGD")):
                accountBalance[userName] = [False, False, True,0,0,0]
                print("You created a SGD currency account successfully👍")
    else:
            print("Please enter correct currency❗️")

#Action 2
def deposit():
    userName = askuserName()
    if(userName not in accountBalance):
        print("Can't find this user name please try again❗️")
    else:
        Currency = askCurrencyType()
        if(validateCurrencyAndAccount(Currency,userName)):
            try:
                Amount = int(input("Enter amount you want to deposit:"))
            except:
                print("Please enter correct information❗️")
            increaseAmount(userName,Currency,Amount)
            addTransactionHistory(userName,Currency,"Deposit",Amount)
            print("Deposit Successfully👍")
        else:
            print("You don't have this account type, please try again❗️")

#Action 3
def withdrawal():
    userName = input("Enter User Name: ")
    Currency = askCurrencyType()
    if(validateCurrencyAndAccount(Currency,userName)):
        WithdrawalAmount = int(input("Please input the amount you want to withdrawal"))
        #If more than 5 times withdrawal
        if(countOperation(userName,transactionStatement,"Withdrawal") >= 5):
            if(checkTimeDifferences(userName,transactionStatement)):
                if(validateBalance(Currency,userName,WithdrawalAmount)):
                    withdrawalAction(userName,Currency,WithdrawalAmount)
                else:
                    print("Please validate you have enough balance in this currency account❗")
            else:
                print("You can't withdrwal since recach withdrwal limit within 5 minutes❗")
        elif(validateBalance(Currency,userName,WithdrawalAmount)):
            withdrawalAction(userName,Currency,WithdrawalAmount)
        else:
            print("Please validate you have enough balance in this currency account❗")
    else:
        print("Please enter correct currency or use correct account❗")

def withdrawalAction(userName,Currency,WithdrawalAmount):
    decreaseAmount(userName,Currency,WithdrawalAmount)
    addTransactionHistory(userName,Currency,"Withdrawal",WithdrawalAmount)
    payFee(userName,Currency,WithdrawalAmount)
    addTransactionHistory(userName,Currency,"Withdrawal Fee",WithdrawalAmount * 0.01)
    print("Withdrawal Successfully👍")

#Action 4
def transfer():
    senderUserName = input("Enter Sender User Name: ")
    receiverUserName = input("Enter Receiver User Name: ")
    Currency = askCurrencyType()
    if(validateCurrency(Currency)):
        if(validateUser(senderUserName) and validateUser(receiverUserName)):
            TransferAmount = int(input("Please input the amount you want to transfer"))
            if(validateBalance(Currency,senderUserName,TransferAmount)):
                transferAction(senderUserName,receiverUserName,Currency,TransferAmount)
            else:
                print("Please validate you have enough balance in this currency account❗")
        else:
            print("Can't find sender or receiver user name❗")
    else:
        print("Please enter correct currency❗")

def transferAction(senderUserName,receiverUserName,Currency,TransferAmount):
    #Transfer Out
    decreaseAmount(senderUserName,Currency,TransferAmount)
    addTransactionHistory(senderUserName,Currency,"Transfer Out",TransferAmount)
    #Pay Transfer Fee
    payFee(senderUserName,Currency,TransferAmount)
    addTransactionHistory(senderUserName,Currency,"Transfer Fee",TransferAmount * 0.01)
    #Receiver receives amount of transfer
    increaseAmount(receiverUserName,Currency,TransferAmount)
    addTransactionHistory(receiverUserName,Currency,"Transfer In",TransferAmount)
    print("Transfer Successfully👍")


#Action 5
def listAccountBalance():
    userName = input("Please enter user name to check account balance: ")
    if(userName in accountBalance):
        if(userName == "OSL_FEE"):
            print(userName + " Account Balance is "
                  + " HKD: " + str(accountBalance[userName][0])
                  + "| USD: " + str(accountBalance[userName][1])
                  + "| SGD: " + str(accountBalance[userName][2]))
        else:
            print(userName + " Account Balance is "
              + " HKD: " + str(accountBalance[userName][3])
              + "| USD: " + str(accountBalance[userName][4])
              + "| SGD: " + str(accountBalance[userName][5]))
    else:
        print("This user doesn't exist❗")

#Action 6
def displayTransaction():
    userName = input("Please enter user name to check transaction statement: ")
    if(userName in transactionStatement):
        print("Client Name: " + userName)
        print("Date                " + " Currency " + " Operation " + " Amount ")
        for record in transactionStatement[userName]:
            print(record[0:4])
    else:
        print("This user doesn't exist or doesn't have any transaction history❗")

def increaseAmount(userName,Currency,Amount):
    if(Currency.upper() =="HKD"):
        accountBalance[userName][3] += Amount
    elif(Currency.upper() =="USD"):
        accountBalance[userName][4] += Amount
    else:
        accountBalance[userName][5] += Amount

def decreaseAmount(userName,Currency,Amount):
    increaseAmount(userName,Currency,Amount * -1)

def payFee(userName,Currency,Amount):
    if(Currency.upper() =="HKD"):
        accountBalance[userName][3] -= Amount * 0.01
        accountBalance["OSL_FEE"][0] += Amount * 0.01
    elif(Currency.upper() =="USD"):
        accountBalance[userName][4] -= Amount * 0.01
        accountBalance["OSL_FEE"][1] += Amount * 0.01
    else:
        accountBalance[userName][5] -= Amount * 0.01
        accountBalance["OSL_FEE"][2] += Amount * 0.01

#count Operation for withdrawal
def countOperation(userName,transactionStatement,ops):
    count = 0
    for record in transactionStatement[userName]:
        if record[2] == ops:
            count += 1
    return count

def checkTimeDifferences(userName,transactionStatement):
    withdrawalTimeList = []
    for record in transactionStatement[userName]:
        if record[2] =="Withdrawal":
            withdrawalTimeList.append(record[4])
    if(len(withdrawalTimeList) >=5):
        print((datetime.now() - withdrawalTimeList[-5]).total_seconds())
        if((datetime.now() - withdrawalTimeList[-5]).total_seconds()/60 >=5):  #check larger than 5 minutes or not
            return True
    else:
        return False
    
def askuserName():
    result = input("Enter User Name:")
    return result

def askCurrencyType():
    result = input("Enter Currency Account(HKD/USD/SGD)")
    return result

def timestampTransform():
    currentTime = datetime.now()
    currentTimeTransform = currentTime.strftime("%d/%b/%Y, %H:%M:%S")
    return currentTimeTransform

#Validate User Input Currency and Account existence.
def validateCurrencyAndAccount(Currency,userName):
    validCurrency = validateCurrency(Currency)
    validAccount = False
    if(Currency.upper() =="HKD" and accountBalance[userName][0] == True):
        validAccount = True
    elif(Currency.upper() =="USD" and accountBalance[userName][1] == True):
        validAccount = True
    elif(Currency.upper() =="SGD" and accountBalance[userName][2] == True):
        validAccount = True
    result = validCurrency and validAccount
    return result

def validateCurrency(Currency):
    return Currency.upper() =="HKD" or Currency.upper() =="USD" or Currency.upper() =="SGD"

def validateUser(userName):
    return userName in accountBalance

def validateBalance(Currency,userName,Amount):
    CurrencyAccountExist = validateCurrencyAndAccount(Currency,userName)
    if(CurrencyAccountExist):
        if(Currency.upper() =="HKD" and(accountBalance[userName][3] > Amount * 1.01)):
            return True
        elif(Currency.upper() =="USD" and(accountBalance[userName][4] > Amount * 1.01)):
            return True
        elif(Currency.upper() =="SGD" and(accountBalance[userName][5] > Amount * 1.01)):
            return True
    else:
        return False

def addTransactionHistory(userName,Currency,Operation,Amount):
    if(userName in transactionStatement):
        transactionStatement[userName].append([timestampTransform(),Currency,Operation,Amount,datetime.now()])
    else:
        transactionStatement[userName] = [[timestampTransform(),Currency,Operation,Amount,datetime.now()]]

def displayMenu():
    print("----------------------------------Menu----------------------------------")
    print("0. Exist")
    print("1. Account Creation")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transfer")
    print("5. List Bank Account Balance")
    print("6. Display Transaction Statement")
    print("7. Show All Account Info(Test Only)")
    print("8. Show All Transaction Info(Test Only)")
    print("----------------------------------End----------------------------------")

def exit():
    print("Exist!")

def showAllAccountInfo():
    print(accountBalance)

def showAllTransactionInfo():
    print(transactionStatement)

if __name__ == "__main__":
    modeNum = 100
    while(modeNum > 0):
        displayMenu()
        modeNum = int(input("Enter a number for operation:"))
        if(modeNum == 1):
            accountCreation()
        if(modeNum == 2):
            deposit()
        if(modeNum == 3):
            withdrawal()
        if(modeNum == 4):
            transfer()
        if(modeNum == 5):
            listAccountBalance()
        if(modeNum == 6):
            displayTransaction()
        if(modeNum == 7):
            showAllAccountInfo()
        if(modeNum == 8):
            showAllTransactionInfo()
        if(modeNum == 0):
            exit()
