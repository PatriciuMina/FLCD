separators = ['[', ']', '(', ')', ';', ' ',  ':', ',' ,'~' ,'"']
operators = ['+', '-', '*', '/', '%', '<', '<=', '=', '>=', '>',
             '>>', '<<', '==', '&&', '||', '!', '!=', '&', '~',
             '|', '^', '++', '--', ',']
reservedWords = ['define', 'number', 'boolean', 'character', 'string', 'if',
                 'then', 'else', 'for', 'read', 'write', 'do', 'while',
                 'start', 'end', 'and', 'or', 'not']

everything = separators + operators + reservedWords
codification = dict([(everything[i], i + 2) for i in range(len(everything))])
codification['identifier'] = 0
codification['constant'] = 1

