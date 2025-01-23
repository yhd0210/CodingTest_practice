function solution(n) {
    var answer = [];
    for(let i = 0; i < n.toString().length; i++) {
        answer.push(Number(n.toString().charAt(i)));
    }
    return answer.reverse();
}