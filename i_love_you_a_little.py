love_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
def how_much_i_love_you(nb_petals):
    return love_list[nb_petals%7] if nb_petals>6 else love_list[nb_petals]

print how_much_i_love_you(4)
