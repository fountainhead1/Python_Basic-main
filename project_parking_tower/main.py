# 주차 타워 구현
# 조건 : 1층 to 5층, 층별로 1대만 주차
# 차량번호 : 숫자 4자리라고 가정
# 기능 : 1. 차량 입고 2. 차량 출고 3. 차량 조회 4. 프로그램 종료

#  설정
max_car = 5  # 타워 주차 최대 용량(최대 5대까지)
car_cnt = 0

# 주차 타워 생성
# list comprehension
tower = ["" for i in range(max_car)]  # 결과 : ["", "", "", "", ""]

# for + list.append()
# tower = []
# for i in range(max_car):
#    tower.append("")  # 결과 : ["", "", "", "", ""]

while True:
    print("=" * 50)
    print("== 주차 타워 시스템 ver 1.1 ==")
    print("=" * 50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    print("=" * 50)

    while True:
        select_num = int(input("번호 : "))
        if 1 <= select_num <= 4:
            break
        else:
            print("MSG : 올바른 번호를 입력하세요.")

    if select_num == 1:  # 입고
        # 입고 1. 주차타워 공간 확인
        if car_cnt < max_car:
            car_num = input("입고 : ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG : 입고 불가")
    elif select_num == 2:  # 출고
        # 1. 차량번호 입력
        # 2. 차량번호 체크
        #  2-1 : 차 없음
        #  2-2 : 출고(tower에 있는 값 -> " "), (car_cnt - 1)
        pass
    elif select_num == 3:  # 조회
        pass
    elif select_num == 4:  # 종료
        print("MSG : 프로그램을 종료합니다.")
        exit()