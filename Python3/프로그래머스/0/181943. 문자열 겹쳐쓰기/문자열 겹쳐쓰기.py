# def solution(my_string, overwrite_string, s):
#     answer = ''
#     answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
#     return answer
def solution(my_string, overwrite_string, s):
    list_string = list(my_string)
    list_string[s:s+len(overwrite_string)] = overwrite_string
    answer = ''.join(list_string)
    return answer