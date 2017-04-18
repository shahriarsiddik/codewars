def pig_it(text):
    #your code here
    return " ".join(map(str, [i[1:]+i[0]+'ay' if i[0].isalpha() else i[0] for i in text.split()]))

print pig_it('Oay emporatay oay oresmay !') # igPay atinlay siay oolcay