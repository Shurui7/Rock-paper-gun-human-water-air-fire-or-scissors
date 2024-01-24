# Made by MorinMax and Shurui7_, MIT liscensed

import random

user_input = input('Rock, paper, gun, human, water, air, fire or scissors: ')

rpc_options = ['rock','paper','scissors','fire','gun','human','water','sponge','air']

def checkstatus():
  if user_input == terminal_response:
    print('We tied')
  elif terminal_response in defeats[user_input]:
    print('You win')
  else:
    print('You lose')


if user_input not in rpc_options: 
  print(f'\nYour answer is incorrect; it should be in this list: {rpc_options}\nYour answer is: {user_input}, do you see the error? Lets try again')
else:
  defeats = {
    'air' : ['fire', 'rock', 'water', 'gun'],
    'gun' : ['rock', 'fire', 'scissors', 'human'],
    'paper' : ['air', 'rock', 'water', 'gun'],
    'rock' : ['scissors', 'sponge', 'fire', 'human'],
    'scissors' : ['air', 'paper', 'human', 'sponge'],
    'fire' : ['sponge', 'paper', 'human', 'scissors'],
    'water' : ['rock', 'fire', 'scissors', 'gun'],
    'sponge' : ['water', 'paper', 'gun', 'air'],
    'human' : ['sponge', 'paper', 'air', 'water'],
    }

  terminal_response = random.choice(rpc_options)
  
  print(f'\nYou choose {user_input}, I choose {terminal_response}')

  checkstatus()
