def reading():

    with open('22.txt') as open_text:
        text = open_text.read()
        text = text.split('\n')
        list_set = set(text)

        dictionary = dict()
        for _ in list_set:
            dictionary.update(dict([(_,0)]))

        for _ in text:
            if _ in dictionary:
                dictionary[_] += 1

    return dictionary
                
                
        
print(reading())
