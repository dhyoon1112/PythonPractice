def reading(x):

    with open(x) as text:
        text = text.read()
        text = text.split('\n')
        print(len(text))
    return text
                
                
happynumbers = reading('23.happynumbers.txt')
primenumbers = reading('23.primenumbers.txt')
            

overlapping = [i for i in happynumbers for ii in primenumbers if i == ii]
print(overlapping)

