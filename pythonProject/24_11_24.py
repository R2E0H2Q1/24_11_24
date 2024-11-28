# create a new list
# input names from the user until 'done' is entered
# append each name to a list with a timestamp as tuple
# danny
#    0                        ,  1
# [ (datetime.now(), 'danny') , ( )]
# print all the time+name and index
# for key, value ...
#  0: danny 18:55  1: sharon 18:56

from datetime import datetime

time_name: list[tuple] = []

while True:
    t_m = input('Enter your name(Type done to exit): ')
    if t_m == 'done':
        break
    time_name.append((datetime.now(), t_m))
print('GAME OVER')


for index, (time, name) in enumerate(time_name):
    print(f'{index}: {name} {time.strftime('%H:%M:%S')}')








