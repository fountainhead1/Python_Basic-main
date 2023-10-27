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
            car_num = input(">>입고 : ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG : 입고 불가")
    elif select_num == 2:  # 출고
        # 1. 출고해야하는 차량번호 입력
        car_num = input(">>출고 : ")
        # 2. 입고된 차량번호인지 조회
        if car_num in tower:
            for i, car in enumerate(tower):
                if car == car_num:  # 출고
                   tower[i] = ""  # tower에서 차량 제거
                   car_cnt -= 1  # 현재 주차대수 동기화
                   break
        else:  # 차량이 없음
            print("MSG : 해당 번호로 입고 된 차량이 없습니다.")

        #  2-1 : 차 없음(메시지 출력 : 입고된 차량이 아님)
        #  2-2 : 출고(tower에서 해당 차량 제거), (car_cnt - 1)
        pass
    elif select_num == 3:  # 조회
        print("== 주차 타워 현황 ==")
        for i in range(len(tower)-1, -1, -1):  # 5층이 가장 위, 1층이 가장 아래로 가도록
            print(f"> {i+1}층 {tower[i]}")
    elif select_num == 4:  # 종료
        print("MSG : 프로그램을 종료합니다.")
        exit()