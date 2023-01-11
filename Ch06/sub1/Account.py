class Account:


    def __init__(self, bank, id, name, balance):
        self.__bank = bank
        self.__id = id
        self.__name = name
        self._balance = balance

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        self._balance -= money

    def show(self):
        print('은행명 : ', self.__bank)
        print('계좌번호 : ', self.__id)
        print('입금주 : ', self.__name)
        print('현재잔액 : ', self._balance)