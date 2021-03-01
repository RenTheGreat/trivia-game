print('Hello peasant, welcome to trivia!')

ans = input('Are you ready to play (yeah/nah): ')
score = 0
total_q = 4

if ans.startswith('n'):
    print('ok. bye now.')

if ans.startswith('y'):

    ans = input('1. Who is the richest person in the world? ')
    if ans.lower() == 'jeff bezos':
        score += 1
        print ('noice!')
    else:
        print ('sorry, thats wrong')

    ans = input('2. How old is Jeff Bezos? ')
    if ans == '57':
        score += 1
        print('noice!')
    else:
        print('just google it next time...')

    ans = input('3. What country is Jeff Bezos from? ')
    if ans.lower() == 'usa' or ans.lower() == 'united states':
        score += 1
        print('noice!')
    else:
        print('do you live under a cave?')

    ans = input('4. What company is Jeff Bezos most known for? ')
    if ans.lower() == 'amazon':
        score += 1
        print('Fantastic!')
    else:
        print('how did you get this wrong? You impulse buy from here all the time.')

    print('Thanks for playing! You got', score,'questions correct.')
    mark = (score/total_q) * 100

    print('Mark:', mark,'%')
    print('bye')

