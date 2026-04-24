def solution(num_list):
    answer = 0
    mult_num = 1
    sum_num = sum(num_list)**2
    for i in range(len(num_list)):
        mult_num *= num_list[i]
    if mult_num < sum_num:
        answer = 1
    else:
        answer = 0
    
    return answer