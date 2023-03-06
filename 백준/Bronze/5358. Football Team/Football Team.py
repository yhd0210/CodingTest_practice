def football_team(name):
    change_word_dict = {"e": "i", "i": "e", "E": "I", "I": "E"}
    
    new_name_list = [change_word_dict[word] if word in change_word_dict else word for word in list(name)]
    
    return "".join(new_name_list)


if __name__ == "__main__":
    while True:
        try:
            name = input()
            print(football_team(name=name))
        except EOFError:
            break