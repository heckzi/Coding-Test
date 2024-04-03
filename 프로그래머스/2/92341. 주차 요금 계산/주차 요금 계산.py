import math
def solution(fees, records):
    answer = []
    car_in = {}  # 차량별 입차 시간 기록
    total_time = {}  # 차량별 총 주차 시간

    for r in records:
        time, car, state = r.split()
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m  # 시간을 분으로 변환
        
        if state == 'IN':
            car_in[car] = minutes
        elif state == 'OUT':
            if car in total_time:
                total_time[car] += minutes - car_in[car]
            else:
                total_time[car] = minutes - car_in[car]
            del car_in[car]  # 해당 차량의 입차 시간 기록 삭제
    for key,value in car_in.items():
        if key in total_time:
            total_time[key]+=(23*60+59)-value
        else:
            total_time[key]=(23*60+59)-value
    
    for car in sorted(total_time.keys()):
        time=total_time[car]
        if time>fees[0]:
            total_fee=fees[1]+math.ceil((time-fees[0])/fees[2])*fees[3]
            answer.append(total_fee)
        else:
            answer.append(fees[1])
        

    return answer