import random
num_twos =0
num_threes =0
num_fours =0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights =0
num_nines =0
num_tens =0
num_elevens = 0
num_twelves =0
total_rolls = 0
num_rolls = int(input('Enter number of rolls, -1 to quit:\n'))
while num_rolls >=1 and num_rolls <= 10:
    if num_rolls >= 1:
        for i in range(num_rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            roll_total = die1 + die2
            
            #Count number of twos to twelses
            if roll_total == 2:
                num_twos = num_twos + 1
            if roll_total == 3:
                num_threes = num_threes + 1
            if roll_total == 4:
                num_fours = num_fours + 1
            if roll_total == 5:
                num_fives = num_fives + 1
            if roll_total == 6:
                num_sixes = num_sixes + 1
            if roll_total == 7:
                num_sevens = num_sevens + 1
            if roll_total == 8:
                num_eights = num_eights + 1
            if roll_total == 9:
                num_nines = num_nines + 1
            if roll_total == 10:
                num_tens = num_tens + 1
            if roll_total == 11:
                num_elevens = num_elevens + 1
            if roll_total == 12:
                num_twelves = num_twelves + 1
            print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))
            num_rolls -= 1
        print('\nDice roll statistics:')
        print('2s:', num_twos)
        print('3s:', num_threes)
        print('4s:', num_fours)
        print('5s:', num_fives)
        print('6s:', num_sixes)
        print('7s:', num_sevens)
        print('8s:', num_eights)
        print('9s:', num_nines)
        print('10s:', num_tens)
        print('11s:', num_elevens)
        print('12s:', num_twelves)
        # Print histogram
        print('\nDice roll histogram:')
        print('2s:  ' + '*' * num_twos)
        print('3s:  ' + '*' * num_threes)
        print('4s:  ' + '*' * num_fours)
        print('5s:  ' + '*' * num_fives)
        print('6s:  ' + '*' * num_sixes)
        print('7s:  ' + '*' * num_sevens)
        print('8s:  ' + '*' * num_eights)
        print('9s:  ' + '*' * num_nines)
        print('10s: ' + '*' * num_tens)
        print('11s: ' + '*' * num_elevens)
        print('12s: ' + '*' * num_twelves)
       
        total_rolls +=1
        print('TOTAL TURNS TAKEN',total_rolls)    
        num_rolls = int(input('Enter number of rolls -1 to quit:\n'))
    else:
        print('Invalid number of rolls. Try again.')
print("You can not roll it more then 10 times")