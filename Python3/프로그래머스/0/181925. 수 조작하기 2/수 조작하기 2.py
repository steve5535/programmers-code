def solution(numLog):
    answer = ''
    n = numLog[0]
    for i in range(1, len(numLog)):
        if numLog[i] == n + 1:
            answer += "w"
            n += 1
        elif numLog[i] == n - 1:
            answer += "s"
            n -= 1
        elif numLog[i] == n + 10:
            answer += "d"
            n += 10
        else:
            answer += "a"
            n -= 10
    return answer