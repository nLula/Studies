from itertools import chain
import random
import sys
from sys import exit

# lst = [1,2,3,'back2future','badboys','toys',234]

# for i in range (len(lst)):
    
    # smth = lst[i]
    # if type(smth) == str:
        # lst[i] = smth + 'and'
        
# print lst


# lst = list(range(20,-1,-2))

# print (lst)
# count = 0
# for i in range(len(lst)):
    
    # count = count + lst[i]
    # print (count)
# print 'nr sum is: ', count


# a1 = range (10, 0 , -2)
# a2 = range (50, 20, - 2)
# a3 = range (90, 60 , -2)

# final = chain(a1,a2,a3)

# print (final)

# print (list(final))


qstn = raw_input('Ask you question, fellow traveller and I will try to answer it: ')

if qstn == '':
    exit()
else:
    answr = random.randint(0,7)

    lst = ['It is certain', 'Outlook good', 'You may rely on it', 'Ask again later', 'By the will of Poseidon', 'Everything is possible', 'I feel it is a NO', 'My sources say YES']

    output = lst.pop(answr)

    print output