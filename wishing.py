import os
os.system('cls')
# ==================================
# wishing to a teacher 


time = int(input('Enter the time : '))
gender = input('For whom ur wishing ? Sir or Madem :')
if time <= 12:
    print(f'Good Morning {gender}')
elif time <= 15:
    print('Good afternoon {t}'.format(t = gender ))
elif time <= 19:
    print('Good evening %s'%gender)
elif time <= 24 :
    
    print('Good night {t}'.format(t = gender))
else:
    print('wrong time')