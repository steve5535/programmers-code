def solution(num_list):
    answer = []
    list_len = len(num_list) - 1
    end_num = num_list[list_len]
    be_num = num_list[list_len - 1]
    num = 0
    if end_num > be_num:
        num = end_num - be_num
    else:
        num = end_num * 2
    num_list.append(num)
    answer = num_list

    return answer