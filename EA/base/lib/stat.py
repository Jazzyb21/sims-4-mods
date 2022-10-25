ST_MODE = 0
def S_IMODE(mode):
    return mode & 4095

def S_IFMT(mode):
    return mode & 61440

def S_ISDIR(mode):
    return S_IFMT(mode) == S_IFDIR

def S_ISCHR(mode):
    return S_IFMT(mode) == S_IFCHR

def S_ISBLK(mode):
    return S_IFMT(mode) == S_IFBLK

def S_ISREG(mode):
    return S_IFMT(mode) == S_IFREG

def S_ISFIFO(mode):
    return S_IFMT(mode) == S_IFIFO

def S_ISLNK(mode):
    return S_IFMT(mode) == S_IFLNK

def S_ISSOCK(mode):
    return S_IFMT(mode) == S_IFSOCK

def filemode(mode):
    perm = []
    for table in _filemode_table:
        for (bit, char) in table:
            if mode & bit == bit:
                perm.append(char)
                break
        perm.append('-')
    return ''.join(perm)

    from _stat import *
except ImportError:
    pass