from User import User


class Account(User):
    def __init__(self, name, password, accType):
        super().__init__(name, password)
        self.accBal=100
        self.accType = accType
        self.intersetRate = 0
        if accType=="Saving":
            self.intersetRate = 4
        elif accType=="Fixed Deposit":
            self.intersetRate = 8.26
        self.noOfTransaction = 0
