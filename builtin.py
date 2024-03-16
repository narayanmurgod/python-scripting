import builtins
buildin_names=dir(builtins)
print('first 20 builtins:',buildin_names[:20])

help(builtins.EOFError)