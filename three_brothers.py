def solution(number):
    answer = 0
   
    for i in range(len(number) -2):
        for j in range(j,len(number)-1):
              for k in range(k,len(number)):
                if number[i]+ number[j] + number[k] == 0:
                    answer+=1
                    
    return answer


