def single_root_words(root_word,*other_words):
    same_words = []
    lol = [s.lower() for s in other_words]
    pop = root_word.lower()
    for i in lol:
        if  pop in i:
            same_words.append(i)
        if i in pop:
            same_words.append(i)
    same_words.pop(0)
    return print(same_words)

single_root_words("eroor","EROOR","Eroo","er","Олег","ааааeroor")
