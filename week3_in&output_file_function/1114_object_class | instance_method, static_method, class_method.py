class Bicycle():

    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.wheel_color = color

    def move(self, speed):
        print(f"자전거: 시속 {speed}km/h로 전진")
        # print(id(my_bicycle))

    def turn(self, direction):
        print(f"자전거: {direction}회전")
        # print(id(my_bicycle))

    def stop(self):
        print(f"자전거({self.wheel_size}, {self.wheel_color})")
        print(id(my_bicycle))

my_bicycle = Bicycle()
my_bicycle.wheel_size = 26
my_bicycle.wheel_color = 'black'
my_bicycle.move(30)
my_bicycle.turn("좌")
my_bicycle.stop()
# print(id(my_bicycle))

your_bicycle = Bicycle()
your_bicycle.wheel_size = 30
your_bicycle.wheel_color = 'red'
your_bicycle.move(50)
your_bicycle.turn("우")
your_bicycle.stop()

객체를 생성할 때 속성값을 지정해서 초기화하는 방법
bicycle = Bicycle(20, 'red')
bicycle.move(50)
bicycle.turn("좌")
bicycle.stop()

class Car():
    instance_count = 0

    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count += 1
        print(f"자동차 객체의 수: {Car.instance_count}")

    def move(self):
        print(f"자동차 ({self.size} & {self.color})가 움직입니다.")

    def change_color(self, color):
        self.color = color
        print(f"색깔이 변경되었습니다.:{self.color}")

    def change_size(self, size):
        self.size = size
        print(f"사이즈가 변경되었습니다.: {self.size}")


car1 = Car('small', 'white')
car2 = Car('big', 'black') # car2는 객체(인스턴스) Car는 클래스, Car 클래스 안에 instance_count는 클래스 변수, car1의 size는 인스턴스 변수

car3 = car1.size('medium', 'red')
car3.move()

car1.change_color('red')
car2.change_size('medium')
car1.move()
car2.move()

print(f"Car 클래스의 총 인스턴스 개수:{Car.instance_count}")
print(f"Car 클래스의 총 인스턴스 개수: {car1.instance_count}")
print(f"Car 클래스의 총 인스턴스 개수: {car2.instance_count}")

car1.move()
car2.move()

class Car2:
    count = 0;
    instance_count = 0

    @classmethod
    def count_instances(cls):
        print(f"자동차 객체의 개수: {cls.instance_count}")

    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기차입니다.")
        elif(10 <= model_code < 20):
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")

    def __init__(self, size, num):
        self.size = size;
        self.count = num;
        Car2.count = Car2.count + 1;
        print(f"자동차 객체의 수: {Car2.count}");
        print(f"인스턴스 변수 초기화: {self.count}");
    def move(self):
        print(f"자동차({self.size} & {self.count})가 움직입니다.");

car1 = Car2('big', 20);
car2 = Car2('small', 30)

Car2.check_type(25)
Car2.check_type(2)