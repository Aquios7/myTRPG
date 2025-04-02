class Char:
    def __init__(self, name='', cclass="Warrior", stats=[1, 50, 5, 5, 0, 'True', 'False', 'False']):
        self.c = cclass
        self.name = name
        self.stats = {'LVL': stats[0],
                      'HP': stats[1],
                      'ATK': stats[2],
                      'DEF': stats[3],
                      'EXP': stats[4],
                      'ALIVE': stats[5],
                      'POISONED': stats[6],
                      'FROZEN': stats[7]}
        self.calc_level()

    def __repr__(self):
        outs = ''
        outs += "Character Name: {0} of class {1}:\n---------------".format(self.name, self.c)
        for k, v in self.stats.items():
            outs += '\n  {0}: {1}'.format(k, v)
        return outs

    def calc_level(self):
        self.stats['LVL'] = int(self.stats['EXP'] ** .5) + 1

    def attack(self, other):
        print("\n{0} furiously attacks {1} with {2} attack. {1} has {3} defense.".format(self.name, other.name,
                                                                                         self.stats['ATK'],
                                                                                         other.stats['DEF']))
        if self.stats['ATK'] >= other.stats['DEF']:
            other.stats['HP'] -= self.stats['ATK']
            print("\nThat was a hit! The HP of {0} is now {1}".format(other.name, other.stats['HP']))
        else:
            print("\nYou missed and only made him angrier!")


def new_char(existing):
    cc = ''
    accept = False
    while not accept:
        n = input("\nPlease input a new name: ")
        accept = True
        for c in existing:
            if n == c.name:
                accept = False
                print("This name is taken, already")
    while not cc in ['w', 't', 'z']:
        cc = input("\nPlease input a class, noble {0}. (W)arrior, (T)ank, Wi(z)ard: ".format(n)).lower()

    cclasses = {'w': 'Warrior', 't': 'Tank', 'z': 'Wizard'}

    newc = Char(n, cclasses[cc])
    print('\nCharacter successfully created:')
    print(newc)
    return newc


def play(chars):
    print("May the games begin. The following characters are present:\n")
    for c in chars:
        print(c)
        print('')

    game_over = False
    turn = 0
    while not game_over:
        print(
            "It's the turn of noble {0} {1}. Please select a player to attack:".format(chars[turn].c, chars[turn].name))
        possible = []
        for i in range(len(chars)):
            if not i == turn:
                possible.append(i)
                print(" - ({0}): {1} named {2}".format(i, chars[i].c, chars[i].name))
        sel = -1
        while not sel in possible:
            s = input('Selection: ')
            try:
                sel = int(s)
            except:
                print("That's not a valid choice")

        chars[turn].attack(chars[sel])
        if chars[sel].stats['HP'] <= 0:
            game_over = True
            print("That was it! {0} has died and the game is over.".format(chars[sel].name))
        turn += 1
        if turn == len(chars): turn = 0


def main():
    chars = []
    entry = ''
    print("Welcome to PSB Battle Game!")
    while not entry.lower() in ['q', 'p']:
        entry = input('\n(N)ew character\n(P)lay game\n(Q)uit\nSelection: ').lower()
        if entry == 'p' and len(chars) < 2:
            print("\nYou can't play with only one character. Create characters first")
            entry = ''  ## You can't play with only one char
        elif entry == 'n':
            chars.append(new_char(chars))
            entry = ''
        elif entry == 'p':
            play(chars)
        elif entry == 'q':
            print("\nOK, good bye")


main()