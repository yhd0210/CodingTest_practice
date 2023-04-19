def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        print(move)
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break
    print(stack)
    return answer