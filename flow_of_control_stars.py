#pattern print
'''
                   *
                   * *
                   * * *
                   * * * *
                   * * * * * 
'''
print('\n\n\n')
for row in range(5):
    for col in range(row+1):
        print('$',end = ' ')
    print('\n')
print('\n\n\n')

# for any n
n = int(input('enter any number n : \n'))
print('\n\n\n')
for row in range(n):
    for col in range(row+1):
        print('$BHUWAN', end = ' ')
    print('\n')
print('\n\n\n')

