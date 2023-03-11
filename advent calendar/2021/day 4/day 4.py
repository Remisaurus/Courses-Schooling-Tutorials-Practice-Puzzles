def main():
    print(get_cards(), get_rolls())

def get_rolls(): 
    rolls = []
    with open('input.txt', 'r') as boss:
        for line in boss:
            rolls.append(line)
        return rolls

def get_cards():
    with open('input2.txt', 'r') as boss:
        cards = []
        for line in boss:
            cards.append(line)
        return cards
    
if __name__ == '__main__':
    main()