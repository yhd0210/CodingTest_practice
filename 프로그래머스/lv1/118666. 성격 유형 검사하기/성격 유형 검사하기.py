
def solution(survey, choices):
    answer = ''
    dic = {'T':0, 'R':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)) : 
        if choices[i] - 4 < 0: 
            dic[survey[i][0]] += 4 - choices[i]

        elif choices[i] - 4 > 0:
            dic[survey[i][1]] += choices[i] - 4
        
    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += 'C' if dic['C'] >= dic['F'] else 'F'
    answer += 'J' if dic['J'] >= dic['M'] else 'M'
    answer += 'A' if dic['A'] >= dic['N'] else 'N'
                
    return answer