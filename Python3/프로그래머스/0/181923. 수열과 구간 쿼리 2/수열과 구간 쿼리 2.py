def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]
        list = arr[s:e+1]
        k_big_list = []
        for j in list:
            if j > k:
                k_big_list.append(j)
        if k_big_list == []:
            answer.append(-1)
        else:
            answer.append(min(k_big_list))
            
        
        
    return answer