def find_template(string, template):
    num_of_matches = 0

    magic_symbols_cnt = 0
    while template[magic_symbols_cnt] == "@":
        if magic_symbols_cnt < len(template) - 1:
            magic_symbols_cnt += 1
        else:
            break

    for i in range(len(string)):

        if num_of_matches == len(template):
            return i - num_of_matches

        if string[i] == template[num_of_matches] or template[num_of_matches] == "@":
            num_of_matches += 1
        else:
            num_of_matches = magic_symbols_cnt

    if num_of_matches == len(template):
        return len(string) - num_of_matches

    return -1


string = input()
template = input()
print(find_template(string, template))
