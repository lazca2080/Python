class Car:

    # 생성자
    def __init__(self, brand, color, price):
        self.__brand = brand
        self.__color = color
        self.__price = price
    
    # 기능
    def speedUp(self):
        print('%s 속도 올립니다.' % self.__brand)

    def speedDown(self):
        print('%s 속도 내립니다.' % self.__brand)

    def show(self):
        print('차량명 : ', self.__brand)
        print('차량색 : ', self.__color)
        print('차량가격 : ', self.__price)