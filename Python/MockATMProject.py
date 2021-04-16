#features
# The user should see the current date and time after they log in
import pickle
from datetime import datetime
from random import randint




def loadDatabase(filename):
    with open(filename, 'rb') as filehandle:
    # read the data as binary data stream
        return pickle.load(filehandle)


def dumpDatabase(filename, listname):
    with open(filename, 'wb') as filehandle:
    # store the data as binary data stream
        pickle.dump(listname, filehandle)

def Register():
    username  = loadDatabase('Username.data')
    allowedPassword = loadDatabase('Password.data')
    Firstname = loadDatabase('Firstname.data')
    Lastname = loadDatabase('Lastname.data')
    currentBalances = loadDatabase('balance.data')
    #accountno = loadDatabase('accountno.data')
    Fname=str(input('Enter your First name:'))
    Lname=str(input('Enter your Last name:'))
    Username=str(input('Enter your unique Username:'))
    if Username in username:
        return 'Username must be unique, try another combination'
    Password=str(input('Enter Password:'))
    Confirmedpassword=str(input('Confirm Password: '))
    if Password == Confirmedpassword:
        username.append(Username)
        allowedPassword.append(Password)
        Firstname.append(Fname)
        Lastname.append(Lname)
        currentBalances.append(0)
        accountno.append(randint(10**(9), (10**10)-1))
        dumpDatabase('Password.data', allowedPassword)
        dumpDatabase('Firstname.data', Firstname)
        dumpDatabase('Lastname.data', Lastname)
        dumpDatabase('Username.data', username)
        dumpDatabase('balance.data', currentBalances)
        dumpDatabase('accountno.data', accountno)
        return True
    else:
        return 'Password mismatch'


def Login():
    Lusername  = loadDatabase('Username.data')
    Lpassword = loadDatabase('Password.data')
    Username = str(input('Enter your username: '))
    if Username in Lusername:
        Password = str(input('Enter your password: '))
        userId = Lusername.index(Username)
        if Password == Lpassword[userId]:
            return (True,userId)
        else:
            return 'You entered an incorrect password.  Please try again'
    else:
        return ('Name not found. Please try again') 


def Dashboard(userId):
    now = datetime.now().strftime('%Y/%m/%d %I:%M:%S')
    Lusername  = loadDatabase('Username.data')
    Lbalance = loadDatabase('Balance.data')
    Username = Lusername[userId]
    accountno = loadDatabase('accountno.data')
    #balance = Lbalance[userId]
    print(now)
    print(accountno)
    print(Lbalance)
    print(Lusername)
    print('Welcome %s' % Username)
    print('These are the availiable options:')
    print('1.  Withdrawal')
    print('2.  Deposit')
    print('3.  Check Balance')
    print('4.  Retrive account no')
    print('.  Compliant')


    selectedOptions=int(input('Please select an option: '))
    if selectedOptions == 1:
        currentBal = Lbalance[userId]
        print(now)
        Amount = int(input('How much would you like to withdraw?'))
        if currentBal >   Amount:
            Lbalance[userId] = currentBal-Amount
            dumpDatabase('balance.data', Lbalance)
            print('Take your Cash')
        else:
            print('Insufficent Funds')
    elif selectedOptions == 2:
        currentBal = Lbalance[userId]
        print(now)
        Amount = int(input('How much would you like to deposit?'))
        Lbalance[userId] = currentBal+Amount
        dumpDatabase('balance.data', Lbalance)
        print('You have $' ,Lbalance[userId], 'now')
    elif selectedOptions == 3:
        currentBal = Lbalance[userId]
        print(now)
        print('Your current bal is : $',currentBal)
    elif selectedOptions == 4:
        print('Your account number is : ', accountno[userId])
    elif selectedOptions == 5:
        print(now)
        issue=str(input('What issue will you like to report?'))
        print('Thank you for contacting us, We will get back to you')
    else:
        print('You selected an invalid option. Please try again')



def LandingPage():
    print('Hello Guest, ')
    print('Do you want to register or Login: ')
    print('1.   Register')
    print('2.   Login')
    selected = int(input('Please select an option: '))
    if selected == 1:
        registmes = Register()
        if registmes == True:
            print('Successful Registration!, Do you want to Login?')
           
            print('1. Login')
            print('2. Cancel')
            selected2 = int(input('Please select an option: '))
            if selected2 == 1:
                loginmes = Login()
                if loginmes[0] == True:
                    Dashboard(loginmes[1])
                else:
                    print(loginmes)   
            else: 
                print('Bye Guest')
        else:
            print(registmes)
    elif selected == 2:
        loginmes=Login()
        if loginmes[0] == True:
            Dashboard(loginmes[1])
        else:
            print(loginmes)  
        
    else:
        print('Please select a valid option')

if __name__ == '__main__':
    LandingPage()

        

        
