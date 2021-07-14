import sys

empty_list = []
light_dict = {
    0: '0,0,1,0',
    1: '0,1,0,0',
    2: '1,0,0,0',
    3: '0,0,0,1',
    4: '0,0,0,0',
}
color_dict = {}
value_dict = {
}
#                    inputs          green,   yellow,   red,    green_left,   no_light
transition_table = {'start' :      ['green', 'yellow', 'red',  'green_left', 'no_light'],
                    'green':       ['green', 'yellow1','nope', 'nope',       'no_light1'],
                    'yellow':      ['green', 'yellow', 'red',  'green_left', 'nope'],
                    'red':         ['nope',  'yellow2','red',  'nope',       'nope'],
                    'green_left':  ['green', 'nope',   'nope', 'green_left', 'no_light2'],
                    'no_light':    ['green', 'yellow', 'nope', 'green_left', 'no_light'],
                    'no_light1':   ['green', 'yellow', 'nope', 'nope',       'no_light1'],
                    'no_light2':   ['green', 'nope',   'nope', 'green_left', 'no_light2'],
                    'yellow1':     ['nope',  'yellow1','red',  'nope',       'nope'],
                    'yellow2':     ['green', 'yellow2','nope', 'green_left', 'nope'],
                    'nope':        ['nope',  'nope',   'nope', 'nope',       'nope' ],
                    }
# filename = sys.argv[1]                                      # command line input
filename = input('Input filename with .txt extension: ')      # user input
def open_file(filename):
        file = open(f'{filename}', 'r')
        for x in file:
            empty_list.append(x[0:-1])                        # removing the newline(\n) symbol
# print(empty_list)


def get_key(val):
    for key, value in light_dict.items():
         if val == value:
             return key


def create_dict():                                           # creating a nested dictionary
    index = 0                                                # giving every input an index
    for value in empty_list:
        value_dict[index] = {}  
        value_dict[index]['color'] = get_key(value) 
        value_dict[index]['value'] = value
        index += 1
# create_dict()

def validate():
    state = 'start'
    for i in value_dict:
        print('----')
        print(f'step: {i}')
        print('color indexas: ',value_dict[i]['color'])
        print(f'current state: {state}')
        print('color: ', transition_table[state][value_dict[i]['color']])
        state = transition_table[state][value_dict[i]['color']]
        if (state == 'nope'):
            print('invalid light sequence')
            break
    if (state != 'nope'):
        print('sequence is valid!')
# validate()


try:
    open_file(filename)
except FileNotFoundError:
    print('No such file')
except Exception as e:
    print(e)
else:
    create_dict()
    validate()
