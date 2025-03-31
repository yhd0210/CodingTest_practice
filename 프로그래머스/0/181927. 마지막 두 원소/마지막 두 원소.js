function solution(num_list) {
    numlen = num_list.length;
    if(num_list[numlen-2] < num_list[numlen-1]) 
        num_list.push(num_list[numlen-1] - num_list[numlen-2])
    else num_list.push(num_list[numlen-1]*2)
    return num_list;
}