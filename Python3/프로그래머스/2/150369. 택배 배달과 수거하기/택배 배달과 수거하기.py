def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        
        if not deliveries and not pickups:
            break
        
        delivered, pickedup = cap, cap
        answer += 2 * max(len(deliveries), len(pickups))
        
        while deliveries and delivered:
            cnt = deliveries[-1]
            if cnt > delivered:
                deliveries[-1] -= delivered
                delivered = 0
            else:
                delivered -= cnt
                deliveries.pop()
                
        while pickups and pickedup:
            
            cnt = pickups[-1]
            if cnt > pickedup:
                pickups[-1] -= pickedup
                pickedup = 0
            else:
                pickedup -= cnt
                pickups.pop()
        
    return answer
