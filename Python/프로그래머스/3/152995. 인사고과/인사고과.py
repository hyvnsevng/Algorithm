MAX = 200001    

def solution(scores):
    wonho = scores[0]
    scores_sorted_by_a = sorted(scores, reverse=True)   # 근태 점수 기준 내림차순으로 정렬
    
    # [현재 점수보다 높은 근태 점수 중 최소, 그 중 최대 동료 평가 점수]
    lower_bound = [MAX, 0]
    
    # [현재 점수와 같은 근태 점수, 그 중 최대 동료 평가 점수]
    upper_bound = [scores_sorted_by_a[0][0], scores_sorted_by_a[0][1]]
    
    # 인센티브 대상자의 점수 배열
    scores_with_incentive = []
    
    for a, b in scores_sorted_by_a:
        # 더 낮은 근태 점수 등장
        if upper_bound[0] > a:
            lower_bound[0], lower_bound[1] = upper_bound[0], max(lower_bound[1], upper_bound[1])
            upper_bound = [a, b]
        
        # 인센티브 제외 조건
        if b < lower_bound[1]:
            continue
            
        scores_with_incentive.append((a, b))
    
    scores_sorted_by_sum = sorted(scores_with_incentive, key=lambda x: x[0] + x[1], reverse=True)
    
    answer = 0
    n = len(scores_with_incentive)
    
    last_score_sum = MAX    # 이전 순서의 점수 합
    
    for i in range(n):
        score = scores_sorted_by_sum[i]
        sum_score = sum(score)
        
        # 점수 합이 다른 경우(동석차 아님)
        if last_score_sum > sum_score:
            answer = i + 1
            last_score_sum = sum_score
        
        # 원호의 점수인 경우
        if score[0] == wonho[0] and score[1] == wonho[1]:
            return answer
        
    return -1
