def solution(l, r):
    answer = []
    for i in range(l, r+1):
        str_n = str(i)
        set_n = set(str_n)
        if set_n <= {"0", "5"}:
            answer.append(i)
    if answer == []:
        answer.append(-1)
        
    return answer