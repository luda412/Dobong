"""
성적 관리 프로그램 V2
====================
V1 (mngscore.py) 대비 주요 변경점:
1. 함수 기반 → 클래스 기반 구조로 리팩토링
2. Private 메서드/속성 사용 (__ 접두사) - 캡슐화
3. 예외 처리 추가 (FileNotFoundError, Exception)
4. join() 함수 사용으로 코드 간결화
5. 입력 로직 개선 (이름 입력 및 파일 저장을 함수 내부로 이동)
6. 파일명 파라미터화 (생성자에서 받을 수 있도록 변경)
7. run() 메서드로 메인 루프 캡슐화
"""

import json

# V2 변경점: 함수 기반 구조에서 클래스 기반 구조로 리팩토링
# - 코드 재사용성 및 유지보수성 향상
# - 캡슐화를 통한 데이터 보호
class ScoreManager:
    def __init__(self, file_name="scores.json", score_names=["국어", "영어", "수학", "과학"]):
        # V2 변경점: Private 속성 사용 (__ 접두사) - 캡슐화
        # V2 변경점: 파일명을 생성자 파라미터로 받아 유연성 향상
        self.__file_name = file_name
        self.__score_names = score_names
        self.__scores_data = {}
    def __write_scores_file(self):
        """성적 데이터를 JSON 파일에 저장하는 함수"""
        with open(self.__file_name, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__scores_data))

    def __read_scores_file(self):
        """JSON 파일에서 성적 데이터를 읽어오는 함수"""
        # V2 변경점: 예외 처리 추가 - FileNotFoundError 및 기타 예외 처리
        # 파일이 없거나 손상된 경우에도 프로그램이 중단되지 않도록 개선
        try:
            with open(self.__file_name, "r", encoding="utf-8") as f:
                s1 = f.read()
                # 빈 파일인 경우 빈 딕셔너리 반환
                if s1 == "":
                    return {}
                return json.loads(s1)
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다: {e}")
            return {}
        except Exception as e:
            print(f"예상치 못한 오류: {e}")
            return {}

    def __input_scores(self, i, scores={}):
        """
        사용자로부터 각 과목의 점수를 입력받는 재귀 함수

        Args:
            i: 현재 입력할 과목의 인덱스
            scores: 입력받은 점수를 저장할 딕셔너리

        Returns:
            모든 과목 점수와 평균이 포함된 딕셔너리
        """
        # V2 변경점: 이름 입력 로직을 함수 내부로 이동하여 캡슐화
        # V2 변경점: 파일 저장 로직을 함수 내부로 이동 (63-64번 줄)
        if not scores:
            name = input("이름을 입력하세요.\n")
            # 학생 이름을 키로 하여 성적 데이터 추가
            self.__scores_data.update({name: scores})

        if i < len(self.__score_names):
            # 현재 과목의 점수 입력 요청
            score = input(f"{self.__score_names[i]} 점수를 입력하세요.\n")
            if score.isdigit():
                # 점수가 0~100 범위인지 확인
                if 0 <= int(score) <= 100:
                    scores[self.__score_names[i]] = int(score)
                    i += 1
                    # 다음 과목 입력으로 재귀 호출
                else:
                    print("0~100 사이의 숫자를 입력하세요.")
                    # 같은 과목 다시 입력
            else:
                print("숫자를 입력하세요.")
                # 같은 과목 다시 입력
            self.__input_scores(i, scores)
        else:
            # 모든 과목 입력 완료 시 평균 계산
            scores.update({"평균" : sum(scores.values()) / len(scores.values())})
            # V2 변경점: 파일 저장 및 완료 메시지를 함수 내부에서 처리
            # 파일에 저장
            self.__write_scores_file()
            print("성적이 입력되었습니다.")

    def __print_scores(self):
        """모든 학생의 전체 성적을 표 형식으로 출력하는 함수"""
        # V2 변경점: join() 함수 사용으로 코드 간결화 및 가독성 향상
        # 하드코딩된 헤더 대신 동적으로 과목명을 연결
        print(f"이름\t{'\t'.join(self.__score_names)}\t평균")
        for name, scores in self.__scores_data.items():
            print(name, end="\t")
            # 각 과목 점수 출력
            for score_name in self.__score_names:
                print(scores[score_name], end="\t")
            # 평균 점수 출력
            print(scores["평균"])

    def __print_average_scores(self):
        """모든 학생의 평균 점수만 출력하는 함수"""
        print("이름\t평균")
        for name, scores in self.__scores_data.items():
            print(name, end="\t")
            print(scores["평균"])

    def __print_max_min_scores(self):
        """
        각 과목별 최대 점수와 최소 점수를 출력하는 함수
        리스트 컴프리헨션을 사용하여 각 과목의 점수 리스트를 생성한 후 max/min 함수 적용
        """
        print("과목\t최대\t최소")
        scores = self.__scores_data.values()
        for score_name in self.__score_names:
            print(score_name, end="\t")
            # 리스트 컴프리헨션: 각 학생의 해당 과목 점수를 리스트로 추출
            score_list = [score[score_name] for score in scores]
            # 최대 점수 출력
            print(max(score_list), end="\t")
            # 최소 점수 출력
            print(min(score_list))
            # 람다 함수를 사용한 방법 (주석 처리됨)
            # print(max(scores, key=lambda x: x[score_name])[score_name], end="\t")
            # print(min(scores, key=lambda x: x[score_name])[score_name])

    def __delete_scores(self):
        """성적 삭제 함수"""
        name = input("삭제할 이름을 입력하세요.\n")
        if self.__scores_data.get(name):
            del self.__scores_data[name]
            self.__write_scores_file()
            print("성적이 삭제되었습니다.")
        else:
            print("해당 이름의 성적이 없습니다.")

    # V2 변경점: 메인 프로그램 루프를 run() 메서드로 캡슐화
    # 클래스 인스턴스를 생성하고 run()을 호출하는 방식으로 사용
    def run(self):
        # 프로그램 시작 시 파일에서 성적 데이터 로드
        self.__scores_data = self.__read_scores_file()

        # 메인 프로그램 루프
        while True:
            i1 = input("서비스를 선택하세요. 1. 성적 입력 2. 성적 조회 3. 학생별 평균 4. 과목별 최대/최소 점수 5. 성적 삭제 0. 종료\n")
            if i1 == "1":
                # V2 변경점: 이름 입력 및 파일 저장 로직이 __input_scores() 내부로 이동
                # 성적 입력 기능
                self.__input_scores(0, {})
            elif i1 == "2":
                # 전체 성적 조회
                self.__print_scores()
            elif i1 == "3":
                # 학생별 평균 조회
                self.__print_average_scores()
            elif i1 == "4":
                # 과목별 최대/최소 점수 조회
                self.__print_max_min_scores()
            elif i1 == "5":
                # 성적 삭제
                self.__delete_scores()
            elif i1 == "0":
                # 프로그램 종료
                print("종료")
                break
            else:
                # 잘못된 입력 처리
                print("잘못된 입력")

while True:
    i1 = input("1. 중간고사 2. 기말고사 0. 종료\n")
    if i1 == "1":
        score_manager = ScoreManager("scores_midterm.json", ["국어", "영어", "수학", "과학", "사회"])
        score_manager.run()
    elif i1 == "2":
        score_manager = ScoreManager("scores_final.json", ["국어", "영어", "수학", "과학", "사회", "체육"])
        score_manager.run()
    elif i1 == "0":
        print("종료")
        break
    else:
        print("잘못된 입력")



h_list = []
d_list = []

with open("coffeeShopSales.txt", encoding="utf-8") as f:
    h_list = (f.readline().split())
    h_list.append("평균")
    h_list.append("합계")
    sum_list = []
    avg_list = []
    for line in f:
        temp_list = [int(data) for data in line.split() if data.isdigit()]
        temp_sum = sum(temp_list)
        temp_avg = temp_sum / len(temp_list)
        temp_list.append(temp_avg)
        temp_list.append(temp_sum)
        for i in range(len(temp_list)):
            if len(sum_list) == i:
                sum_list.append(0)
            sum_list[i] += temp_list[i]
        d_list.append([line.split()[0], *temp_list])
    avg_list = [sum_data / len(d_list) for sum_data in sum_list]
    d_list.append(["평균", *avg_list])
    d_list.append(["합계", *sum_list])
d_list.insert(0, h_list)
for row in d_list:
    print("\t".join([f"{str(data):<8}" for data in row]))

with open("coffeeShopSalesResult.txt", "w", encoding="utf-8") as f:
    for row in d_list:
        f.write("\t".join([f"{str(data):<8}" for data in row]) + "\n")