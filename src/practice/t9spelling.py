'''
Created on May 10, 2011

@author: abdelrahman
'''

'''
Problem

The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. We would like to make it easier to write a message to your friend using a sequence 
of keypresses to indicate the desired characters. The letters are mapped onto the digits as shown below. 
To insert the character B for instance, the program would press 22. In order to insert two characters in sequence from the same key,
 the user must pause before pressing the key a second time. 
The space character ' ' should be printed to indicate a pause. For example, 2 2 indicates AA whereas 22 indicates B.
'''

'''
Input 
 
4
hi
yes
foo  bar
hello world

Output
Case #1: 44 444
Case #2: 999337777
Case #3: 333666 6660 022 2777

'''

info_map = {' ': '0',
 'a': '2',
 'b': '22',
 'c': '222',
 'd': '3',
 'e': '33',
 'f': '333',
 'g': '4',
 'h': '44',
 'i': '444',
 'j': '5',
 'k': '55',
 'l': '555',
 'm': '6',
 'n': '66',
 'o': '666',
 'p': '7',
 'q': '77',
 'r': '777',
 's': '7777',
 't': '8',
 'u': '88',
 'v': '888',
 'w': '9',
 'x': '99',
 'y': '999',
 'z': '9999'}


alphapit = 'abcdefghijklmnopqrstuvwxyz'
#alpha_numeric_map = dict()
#index = 0
#for i in range(2, len(alphapit)):
#    if i == 9:
#        alpha_numeric_map[i] = alphapit[index:]
#        break
#    else:
#        alpha_numeric_map[i] = alphapit[index: index+3]
#    index += 3
#info_map = dict()
#for key, value in alpha_numeric_map.iteritems():
#    info_map[value[0]] = '%s' % key
#    info_map[value[1]] = ('%s' % key) * 2
#    info_map[value[2]] = ('%s' % key) * 3
#    if key == 9:
#        info_map[value[3]] = ('%s' % key) * 4
#        
#info_map[' '] = '0'

def __process_text(text):
#    import pdb
#    pdb.set_trace()
    last_occured_group = None
    output = list()
    for char in text:
        current_group = alphapit.find(char) / 3 if char in alphapit else -1
        if current_group > 7:
            current_group = 7
        if current_group == last_occured_group:
            output.append(' ')
        last_occured_group = current_group
        output.append(info_map[char])
    return output
        
def t9spelling(input_list):
    result = ''
    for index, item in enumerate(input_list):
        result = '%sCase #%s: %s\n' %(result, index + 1, ''.join( __process_text(item)))
    return result