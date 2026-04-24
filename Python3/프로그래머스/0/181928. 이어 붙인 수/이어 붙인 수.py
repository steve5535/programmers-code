def solution(num_list):
    answer = 0
    add_even = ""
    add_odd = ""
    for i in num_list:
        if i % 2 == 0:
            add_even += str(i)
        else:
            add_odd += str(i)
    answer = int(add_even) + int(add_odd)
    return answer