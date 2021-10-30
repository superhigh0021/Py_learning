from random import randint
from random import sample
import string
def file_write():
    with open('text1.txt', 'w') as f1:
        for i in range(1,randint(1, 100)):
            str=''.join(sample(string.ascii_letters + string.digits,randint(1,10)))
            str += '\n'
            print('NO.{}  {}'.format(i,str),end='')
            f1.write(str)
    f1.close()


def file_read():
    line=open('text1.txt', 'r').readlines()
    return len(line)

file_write()
print(file_read())