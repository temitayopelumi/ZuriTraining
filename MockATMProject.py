#features
# The user should see the current date and time after they log in
from datetime import datetime
allowedUsers =  ['Blessing', 'Temitayo', 'Val']
allowedPassword = ['PasswordBlessing',  "PasswordTemitayo", 'PasswordVal']
currentBalances = [1000, 2000, 3000]

name=str(input("What is your name? \n"))
if name in allowedUsers:
    Password=str(input("Enter Your Password? \n"))
    userId = allowedUsers.index(name)
    if Password == allowedPassword[userId]:
        now = datetime.now().strftime('%Y/%m/%d %I:%M:%S')
        print(now)

        print('Welcome %s' % name)
        print('These are the availiable options:')
        print('1.  Withdrawal')
        print('2.  Deposit')
        print('3.  Compliant')

        selectedOptions=int(input('Please select an option: '))
        if selectedOptions == 1:
            currentBal = currentBalances[userId]
            print(now)
            Amount = int(input('How much would you like to withdraw?'))
            if currentBal >   Amount:
                currentBalances[userId] = currentBal-Amount
                print('Take your Cash')
            else:
                print('Insufficent Funds')
        elif selectedOptions == 2:
            currentBal = currentBalances[userId]
            print(now)
            Amount = int(input('How much would you like to deposit?'))
            currentBalances[userId] = currentBal+Amount
            print(currentBalances[userId])
        elif selectedOptions == 3:
            print(now)
            Amount=int(input('What issue will you like to report?'))
            print('Thank you for contacting us')
        else:
            print('You selected an invalid option. Please try again')
    else:
        print('You entered an incorrect password.  Please try again')
else:
    print('Name not found. Please try again')
