import math

def to_minute(timestamp):
    h, m = timestamp.split(":")
    return int(h) * 60 + int(m)
    
    
def solution(fees, records):
    min_time, min_fee, unit_time, unit_fee = fees
    
    def calc_fee(time):
        if time <= min_time:
            return min_fee
        return min_fee + math.ceil((time - min_time) / unit_time) * unit_fee 
    
    in_time = dict()
    total_time = dict()
    
    for record in records:
        timestamp, number, status = record.split()
        current_time = to_minute(timestamp)
        
        if in_time.get(number, -1) < 0:
            in_time[number] = current_time
        else:
            total_time[number] = total_time.get(number, 0) + (current_time - in_time[number])
            in_time.pop(number)
    
    end_time = to_minute("23:59")
    for number in in_time:
        total_time[number] = total_time.get(number, 0) + (end_time - in_time[number])
        
    key_list = sorted(list(total_time.keys()))
    answer = []
    for key in key_list:
        answer.append(calc_fee(total_time[key]))
    return answer