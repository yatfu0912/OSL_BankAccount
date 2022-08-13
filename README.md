# OSL_BankAccount
## Bank Account System

### Program
- **Python: 3.10**

### Variables
- accountBalance : Dictionary stores all user's account balance include default account.
- transactionStatement :**Dictionary stores stores all transaction record.

### Function
- accountCreation : Create account with user name and account type(HKD,USD,SGD)
- deposit :Deposit money with user name and account type(HKD,USD,SGD)
- withdrawal :Withdrawal money with user name and account type(HKD,USD,SGD)
- withdrawalAction :** Remove money from account and pay fee to OSL_FEE account.
- transfer : Transfer money with user name(sender,receiver) and account type(HKD,USD,SGD).
- transferAction :Transfer money from sender to receiver and pay fee to OSL_FEE account.
- listAccountBalance : List account balance for a specific user.
- displayTransaction :Display Transaction record for a specific user.
- increaseAmount : Increase money for a specific user.
- decreaseAmount :Decrease money for a specific user.
- payFee :Pay fee to OSL_FEE account.
- countOperation : Count withdrawal times.
- checkTimeDifferences  :Check differences between 1st withdrawal and 5th withdrawal.
- askuserName  :Ask user input for user name.
- askCurrencyType  :Ask user input for currency type.
- timestampTransform   :Transform time format. eg "13/Aug/2022, 18:15:26"
- validateCurrencyAndAccount  :Validate currency is correct and currency account is exist.
- validateCurrency  :Validate currency is correct.
- validateUser  :Validate user is exist.
- validateBalance  :Validate balance is enough to transfer or withdrawal.
- addTransactionHistory  :Add transaction record with format [Date,Currency,Operation,Amount]
- displayMenu  :Display Menu for selecting action.
- exit  :Exit console.
