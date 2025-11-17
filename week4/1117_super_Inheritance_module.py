import my_first_moudle
import my_area as area
from my_module2 import *
from my_module1 import *
from my_area import PI as pi
from my_area import square_area as square
from my_area import circle_area as circle

import my_module_test2

import random
print(f"램덤 숫자: {random.randrange(0, 10,2)}")

import datetime
date_obj = datetime.date(year, month, day)

set_day = datetime.date(2020, 10, 15)
today = datetime.date.today()
print(set_day-today)
print(set_day)
print(f"{set_day.year} / {set_day.month} / {set_day.day}")


my_module_test2.func(3)

class Bicycle():
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print(f"자전거: 시속 {speed}킬로미터로 전진")

    def turn(self, direction):
        print(f"자전거: {direction}회전")

    def stop(self):
        print(f"자전거({self.wheel_size}, {self.color}): 정지")

class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state): # FoldingBicycle 초기화
        # Bicycle.__init__(self, wheel_size, color) # Bicycle의 초기화 재사용
        super().__init__(wheel_size, color) #super()도 사용 가능
        self.state = state

    def fold(self):
        self.state = 'folding'
        print(f"자전거: 접기, state = {self.state}")

    def unfold(self):
        self.state = 'unfolding'
        print(f"자전거: 펴기, state = {self.state}")

folding_bicycle = FoldingBicycle(30,'white', 'unfolding') # 객체 생성
folding_bicycle.move(20)
folding_bicycle.turn('좌')
folding_bicycle.stop()
folding_bicycle.fold()
folding_bicycle.unfold()
my_first_moudle.my_function()

print(f"pi = {my_area.PI}")
print(f"square area = {my_area.square_area(5)}")
print(f"circle area = {my_area.circle_area(2)}")
print(dir(my_first_moudle))
print(dir(my_area))

print(f"PI: {pi}")
print(f"square_area: {square(5)}")
print(f"circle_area: {circle(2)}")

func1()
func2()
func3()

