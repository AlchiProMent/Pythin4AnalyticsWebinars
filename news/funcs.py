from const import _ATTENT, _NORM, _TXT, _CLEAR

def err_msg(msg, margins=True):
    s = f'{_ATTENT}{msg}{_CLEAR}'
    if margins:
        s = f'\n{s}\n'
    print(s)

def msg(msg):
    s = f'{_NORM}{msg}{_CLEAR}'
    print(s)

def prntxt(txt):
    s = f'{_TXT}{txt}{_CLEAR}'
    print(s)


