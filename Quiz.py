print('Welcome to my quiz game')
playing = input('Do you want to play? ')
if playing.lower() != "yes"
  quit()
else:
  print('Okay lets Play!')
  
score = 0

answer = input('What does CPU stand for? ')
if answer.lower() == "central processing unit":
  print('Correct')
  score += 1
else:
  print('Incorrect')

answer = input('What does GPU stand for? ')
if answer.lower() == 'graphics processing unit:
  print('yes')
  score += 1
else:
  print('Incorrect')
  

print(f'You got {score} answers correct')
