import pymysql
from account import Account
from User import User


class DBHandler:
    def __init__(self, host, user, password, dataBase, port):
        self.host = host
        self.password = password
        self.username = user
        self.dataBase = dataBase
        self.port = port

    def register_User(self, account):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        print("connection Created")
        cursor = connection.cursor()
        try:
            sql = "Insert into user (`username`,`password`) VALUES (%s,%s)"
            args = (account.username, account.password)
            cursor.execute(sql, args)
            connection.commit()
            sql = "Select * from `user` where username=%s"
            args = (account.username)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            sql = "Insert into account (`accBal`,`accType`,`intersetRate`,`noOfTransaction`,`accNo`) VALUES (%s,%s,%s,%s,%s)"
            args = (account.accBal, account.accType,
                    account.intersetRate, account.noOfTransaction, result[0])
            cursor.execute(sql, args)
            connection.commit()

        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()

    def Authentication(self, user):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        print("connection Created")
        cursor = connection.cursor()
        try:
            sql = "Select * from `user`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                if i[1] == user.username and i[2] == user.password:
                    return True

            return False
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()

    def CheckBalance(self, username, password):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:
            sql = "Select * from `user` where username = %s"
            args = (username)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            sql = "select * from `account` where accNo= %s"
            args = (result[0])
            cursor.execute(sql, args)
            result = cursor.fetchone()
            total = int(result[1])+int(result[3])
            print(total)

        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()

    def Deposit(self, amount, username, password):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:
            sql = "Select * from `user` where username = %s"
            args = (username)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            sql = "update `account` set accBal=%s where accNo= %s"
            args = (amount, result[0])
            cursor.execute(sql, args)
            connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()
    def WithDraw(self, amount, username, password):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:
            sql = "Select * from `user` where username = %s"
            args = (username)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            sql = "update `account` set accBal=%s where accNo= %s"
            args = (result[1])-amount, result[0]
            cursor.execute(sql, args)
            connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()
            connection.close()

db = DBHandler('localhost', 'root', 'sbaf1234', 'atm', 3306)
print("***Welcome to Menu***")
print("1.Register Your Account")
print("2.Login to Account")

choice = int(input())

if choice == 1:
    u = input("Enter username")
    p = input("Enter password")
    t = input("Enter account Type")
    acc = Account(u, p, t)
    db.register_User(acc)

    print("Registered Successfully!")

if choice == 2:
    u = input("Enter username")
    p = input("Enter password")

    user = User(u, p)
    if db.Authentication(user):
        print("Authenticated")

        print("1.Check Balance")
        print("2.Deposit Amount")
        print("3.WithDraw Amount")
        print("4.Transfer Amount")

        subChoice = int(input())
        if subChoice == 1:
            db.CheckBalance(u, p)
        elif subChoice == 2:
            amount = input("How many amount you want to enter")
            if int(amount)<=0:
                print("Negative Number Entered")
            else:
                db.Deposit(amount, u, p)
        elif subChoice == 3:
            amount = input("How many amount you want to Withdraw")
            if int(amount)<=0:
                print("Negative Number Entered")
            else:
                db.WithDraw(amount, u, p)
    else:
        print("Authentication failed!")
