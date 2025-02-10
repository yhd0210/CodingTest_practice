def solution(my_string):
    answer = []
    for i in my_string.split(" "):
        if i != "":
            answer.append(i)
    return answer