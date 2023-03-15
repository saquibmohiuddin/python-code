import random, os, yaml, getpass

directory=os.getcwd()

with open(os.path.join(directory, 'yaml', 'yml_basics_game.yml')) as f:
    config=yaml.safe_load(f)
print(config)


range_min=config['range']['min']

range_max=config['range']['max']

guesses_allowed=config['guesses']

mode=config['mode']

solved=False
if mode=='single':
    number = random.randrange(range_min, range_max)
    
elif mode=='multi':
    number=int(getpass.getpass('Player 2: Please enter the number to guess'))
else:
    print('invalid config')
    exit()
    
for i in range(guesses_allowed):
    guess=int(input('Enter your guess: '))
    
    if guess==number:
        print('You Have guessed the correct number')
        solved=True
        break
        
    elif guess<number:
        print('You are low')
    elif guess>number:
        print('your guess is high')
    