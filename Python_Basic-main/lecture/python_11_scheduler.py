#  스케줄러(Scheduler)
#   - 정해진 일정에 맞춰서 프로그램을 동작시킴
#  ex) 12시간에 한번씩 / 5분마다 / 특정일에만(e.g 크리스마스)

#  스케줄러 + 프로그램 → 완성 → 서버(동작)

#  apscheduler 사용
#   1. Blocking
#    - 스케줄러 + 프로그램만 동작
#   2. Background
#    - 동작은 하되 뒤에서 조용히

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def print_today():
    print(datetime.now())   # 현재 시간을 출력해주는 함수

#  1. 스케줄러 생성
scheduler = BlockingScheduler()

scheduler.add_job(print_today, "interval", seconds=5)
scheduler.start()
