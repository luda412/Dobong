class CoffeeSystem:

    def __init__(self, file_name='coffeeShopSales.txt'):
        # 파일명 및 데이터 구조 초기화
        self.file_name = file_name
        self.header = []
        self.espresso = []
        self.americano = []
        self.cafe_latte = []
        self.capuccino = []
        self.date = []

    def file_read(self):
        with open(self.file_name, 'r') as f:
            for line in f:
                print(line, end='')

    def header_processing(self):
        with open(self.file_name, 'r') as f:
            self.header = f.readline().split()
            # print(self.header)

    def menu_processing(self):
        with open(self.file_name, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                data_list = line.split()
                self.date.append(data_list[0])
                self.espresso.append(int(data_list[1]))
                self.americano.append(int(data_list[2]))
                self.cafe_latte.append(int(data_list[3]))
                self.capuccino.append(int(data_list[4]))
            # print(f'{self.espresso} {self.americano} {self.cafe_latte}')
    def calculate_total_sales(self):

        total_espresso = sum(self.espresso)
        # self.espresso.append(total_espresso)
        print(f"{self.date[0]}부터, {self.date[len(self.date)-1]}까지 {len(self.date)}일간 {self.header[1]} 판매 수: {total_espresso}")
        print(f"{self.header[1]} 평균 판매량: {total_espresso/len(self.espresso)}")

        total_americano = sum(self.americano)
        print(f"{self.date[0]}부터, {self.date[len(self.date)-1]}까지 {len(self.date)}일간 {self.header[2]} 판매 수: {total_americano}")
        print(f"{self.header[2]} 평균 판매량: {total_americano/len(self.americano)}")

        total_cafe_latte = sum(self.cafe_latte)
        print(f"{self.date[0]}부터, {self.date[len(self.date)-1]}까지 {len(self.date)}일간 {self.header[3]} 판매 수: {total_cafe_latte}")
        print(f"{self.header[3]} 평균 판매량: {total_cafe_latte/len(self.cafe_latte)}")

        total_capuccino = sum(self.capuccino)
        print(f"{self.date[0]}부터, {self.date[len(self.date)-1]}까지 {len(self.date)}일간 {self.header[4]} 판매 수: {total_capuccino}")
        print(f"{self.header[4]} 평균 판매량: {total_capuccino/len(self.capuccino)}")

        print("=====================================")

        for i in range(1,len(self.header)):
            print(f"{self.date[0]}부터, {self.date[len(self.date)-1]}까지 {len(self.date)}일간 {self.header[i]} 판매 수: {total_espresso}")
            print(f"{self.header[i]} 평균 판매량: {total_espresso/len(self.espresso)}")

coffee_system = CoffeeSystem()

coffee_system.header_processing()

coffee_system.menu_processing()

coffee_system.calculate_total_sales()
