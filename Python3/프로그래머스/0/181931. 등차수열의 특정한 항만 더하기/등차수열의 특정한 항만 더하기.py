def solution(a, d, included):
    answer = 0
    num_list = []
    for i in range(len(included)):
        num_list.append(a)
        a += d
    for i, bool in enumerate(included):
        if bool:
            answer += num_list[i]
    return answer