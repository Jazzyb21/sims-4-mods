from os import PathLike
def what(file, h=None):
    f = None
    try:
        if h is None:
            if isinstance(file, (str, PathLike)):
                f = open(file, 'rb')
                h = f.read(32)
            else:
                location = file.tell()
                h = file.read(32)
                file.seek(location)
        for tf in tests:
            res = tf(h, f)
            if res:
                return res
    finally:
        if f:
            f.close()

def test_jpeg(h, f):
    if h[6:10] in (b'JFIF', b'Exif'):
        return 'jpeg'

def test_png(h, f):
    if h.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'

def test_gif(h, f):
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'

def test_tiff(h, f):
    if h[:2] in (b'MM', b'II'):
        return 'tiff'

def test_rgb(h, f):
    if h.startswith(b'\x01\xda'):
        return 'rgb'

def test_pbm(h, f):
    if len(h) >= 3 and (h[0] == ord(b'P') and h[1] in b'14') and h[2] in b' \t\n\r':
        return 'pbm'

def test_pgm(h, f):
    if len(h) >= 3 and (h[0] == ord(b'P') and h[1] in b'25') and h[2] in b' \t\n\r':
        return 'pgm'

def test_ppm(h, f):
    if len(h) >= 3 and (h[0] == ord(b'P') and h[1] in b'36') and h[2] in b' \t\n\r':
        return 'ppm'

def test_rast(h, f):
    if h.startswith(b'Y\xa6j\x95'):
        return 'rast'

def test_xbm(h, f):
    if h.startswith(b'#define '):
        return 'xbm'

def test_bmp(h, f):
    if h.startswith(b'BM'):
        return 'bmp'

def test_webp(h, f):
    if h.startswith(b'RIFF') and h[8:12] == b'WEBP':
        return 'webp'

def test_exr(h, f):
    if h.startswith(b'v/1\x01'):
        return 'exr'

def test():
    import sys
    recursive = 0
    if sys.argv[1] == '-r':
        del sys.argv[1:2]
        recursive = 1
    try:
        if sys.argv[1:]:
            testall(sys.argv[1:], recursive, 1)
        else:
            testall(['.'], recursive, 1)
    except KeyboardInterrupt:
        sys.stderr.write('\n[Interrupted]\n')
        sys.exit(1)

def testall(list, recursive, toplevel):
    import sys
    import os
    for filename in list:
        if os.path.isdir(filename):
            print(filename + '/:', end=' ')
            if recursive or toplevel:
                print('recursing down:')
                import glob
                names = glob.glob(os.path.join(filename, '*'))
                testall(names, recursive, 0)
            else:
                print('*** directory (use -r) ***')
                print(filename + ':', end=' ')
                sys.stdout.flush()
                try:
                    print(what(filename))
                except OSError:
                    print('*** not found ***')
        else:
            print(filename + ':', end=' ')
            sys.stdout.flush()
            try:
                print(what(filename))
            except OSError:
                print('*** not found ***')

    test()