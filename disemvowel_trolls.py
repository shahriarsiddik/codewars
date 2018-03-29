def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return reduce(lambda a,b:a.replace(b,''),vowels,string)

print(disemvowel("This website is for losers LOL!"))