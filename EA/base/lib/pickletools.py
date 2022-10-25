import codecs
class ArgumentDescriptor(object):
    __slots__ = ('name', 'n', 'reader', 'doc')

    def __init__(self, name, n, reader, doc):
        self.name = name
        self.n = n
        self.reader = reader
        self.doc = doc

def read_uint1(f):
    data = f.read(1)
    if data:
        return data[0]
    raise ValueError('not enough data in stream to read uint1')

def read_uint2(f):
    data = f.read(2)
    if len(data) == 2:
        return _unpack('<H', data)[0]
    raise ValueError('not enough data in stream to read uint2')

def read_int4(f):
    data = f.read(4)
    if len(data) == 4:
        return _unpack('<i', data)[0]
    raise ValueError('not enough data in stream to read int4')

def read_uint4(f):
    data = f.read(4)
    if len(data) == 4:
        return _unpack('<I', data)[0]
    raise ValueError('not enough data in stream to read uint4')

def read_uint8(f):
    data = f.read(8)
    if len(data) == 8:
        return _unpack('<Q', data)[0]
    raise ValueError('not enough data in stream to read uint8')

def read_stringnl(f, decode=True, stripquotes=True):
    data = f.readline()
    if not data.endswith(b'\n'):
        raise ValueError('no newline found when trying to read stringnl')
    data = data[:-1]
    if stripquotes:
        for q in (b'"', b"'"):
            if data.startswith(q):
                if not data.endswith(q):
                    raise ValueError('strinq quote %r not found at both ends of %r' % (q, data))
                data = data[1:-1]
                break
        raise ValueError('no string quotes around %r' % data)
    if decode:
        data = codecs.escape_decode(data)[0].decode('ascii')
    return data

def read_stringnl_noescape(f):
    return read_stringnl(f, stripquotes=False)

def read_stringnl_noescape_pair(f):
    return '%s %s' % (read_stringnl_noescape(f), read_stringnl_noescape(f))

def read_string1(f):
    n = read_uint1(f)
    data = f.read(n)
    if len(data) == n:
        return data.decode('latin-1')
    raise ValueError('expected %d bytes in a string1, but only %d remain' % (n, len(data)))

def read_string4(f):
    n = read_int4(f)
    if n < 0:
        raise ValueError('string4 byte count < 0: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return data.decode('latin-1')
    raise ValueError('expected %d bytes in a string4, but only %d remain' % (n, len(data)))

def read_bytes1(f):
    n = read_uint1(f)
    data = f.read(n)
    if len(data) == n:
        return data
    raise ValueError('expected %d bytes in a bytes1, but only %d remain' % (n, len(data)))

def read_bytes4(f):
    n = read_uint4(f)
    if n > sys.maxsize:
        raise ValueError('bytes4 byte count > sys.maxsize: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return data
    raise ValueError('expected %d bytes in a bytes4, but only %d remain' % (n, len(data)))

def read_bytes8(f):
    n = read_uint8(f)
    if n > sys.maxsize:
        raise ValueError('bytes8 byte count > sys.maxsize: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return data
    raise ValueError('expected %d bytes in a bytes8, but only %d remain' % (n, len(data)))

def read_unicodestringnl(f):
    data = f.readline()
    if not data.endswith(b'\n'):
        raise ValueError('no newline found when trying to read unicodestringnl')
    data = data[:-1]
    return str(data, 'raw-unicode-escape')

def read_unicodestring1(f):
    n = read_uint1(f)
    data = f.read(n)
    if len(data) == n:
        return str(data, 'utf-8', 'surrogatepass')
    raise ValueError('expected %d bytes in a unicodestring1, but only %d remain' % (n, len(data)))

def read_unicodestring4(f):
    n = read_uint4(f)
    if n > sys.maxsize:
        raise ValueError('unicodestring4 byte count > sys.maxsize: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return str(data, 'utf-8', 'surrogatepass')
    raise ValueError('expected %d bytes in a unicodestring4, but only %d remain' % (n, len(data)))

def read_unicodestring8(f):
    n = read_uint8(f)
    if n > sys.maxsize:
        raise ValueError('unicodestring8 byte count > sys.maxsize: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return str(data, 'utf-8', 'surrogatepass')
    raise ValueError('expected %d bytes in a unicodestring8, but only %d remain' % (n, len(data)))

def read_decimalnl_short(f):
    s = read_stringnl(f, decode=False, stripquotes=False)
    if s == b'00':
        return False
    if s == b'01':
        return True
    return int(s)

def read_decimalnl_long(f):
    s = read_stringnl(f, decode=False, stripquotes=False)
    if s[-1:] == b'L':
        s = s[:-1]
    return int(s)

def read_floatnl(f):
    s = read_stringnl(f, decode=False, stripquotes=False)
    return float(s)

def read_float8(f):
    data = f.read(8)
    if len(data) == 8:
        return _unpack('>d', data)[0]
    raise ValueError('not enough data in stream to read float8')

def read_long1(f):
    n = read_uint1(f)
    data = f.read(n)
    if len(data) != n:
        raise ValueError('not enough data in stream to read long1')
    return decode_long(data)

def read_long4(f):
    n = read_int4(f)
    if n < 0:
        raise ValueError('long4 byte count < 0: %d' % n)
    data = f.read(n)
    if len(data) != n:
        raise ValueError('not enough data in stream to read long4')
    return decode_long(data)

class StackObject(object):
    __slots__ = ('name', 'obtype', 'doc')

    def __init__(self, name, obtype, doc):
        self.name = name
        if isinstance(obtype, tuple):
            for contained in obtype:
                pass
        self.obtype = obtype
        self.doc = doc

    def __repr__(self):
        return self.name

class OpcodeInfo(object):
    __slots__ = ('name', 'code', 'arg', 'stack_before', 'stack_after', 'proto', 'doc')

    def __init__(self, name, code, arg, stack_before, stack_after, proto, doc):
        self.name = name
        self.code = code
        self.arg = arg
        for x in stack_before:
            pass
        self.stack_before = stack_before
        for x in stack_after:
            pass
        self.stack_after = stack_after
        self.proto = proto
        self.doc = doc

    if d.name in name2i:
        raise ValueError('repeated name %r at indices %d and %d' % (d.name, name2i[d.name], i))
    if d.code in code2i:
        raise ValueError('repeated code %r at indices %d and %d' % (d.code, code2i[d.code], i))
    name2i[d.name] = i
    code2i[d.code] = i
    code2op[d.code] = d
def assure_pickle_consistency(verbose=False):
    copy = code2op.copy()
    for name in pickle.__all__:
        if not re.match('[A-Z][A-Z0-9_]+$', name):
            if verbose:
                print("skipping %r: it doesn't look like an opcode name" % name)
                picklecode = getattr(pickle, name)
                if isinstance(picklecode, bytes) and len(picklecode) != 1:
                    if verbose:
                        print("skipping %r: value %r doesn't look like a pickle code" % (name, picklecode))
                        picklecode = picklecode.decode('latin-1')
                        if picklecode in copy:
                            if verbose:
                                print('checking name %r w/ code %r for consistency' % (name, picklecode))
                            d = copy[picklecode]
                            if d.name != name:
                                raise ValueError("for pickle code %r, pickle.py uses name %r but we're using name %r" % (picklecode, name, d.name))
                            del copy[picklecode]
                        else:
                            raise ValueError("pickle.py appears to have a pickle opcode with name %r and code %r, but we don't" % (name, picklecode))
                else:
                    picklecode = picklecode.decode('latin-1')
                    if picklecode in copy:
                        if verbose:
                            print('checking name %r w/ code %r for consistency' % (name, picklecode))
                        d = copy[picklecode]
                        if d.name != name:
                            raise ValueError("for pickle code %r, pickle.py uses name %r but we're using name %r" % (picklecode, name, d.name))
                        del copy[picklecode]
                    else:
                        raise ValueError("pickle.py appears to have a pickle opcode with name %r and code %r, but we don't" % (name, picklecode))
        else:
            picklecode = getattr(pickle, name)
            if isinstance(picklecode, bytes) and len(picklecode) != 1:
                if verbose:
                    print("skipping %r: value %r doesn't look like a pickle code" % (name, picklecode))
                    picklecode = picklecode.decode('latin-1')
                    if picklecode in copy:
                        if verbose:
                            print('checking name %r w/ code %r for consistency' % (name, picklecode))
                        d = copy[picklecode]
                        if d.name != name:
                            raise ValueError("for pickle code %r, pickle.py uses name %r but we're using name %r" % (picklecode, name, d.name))
                        del copy[picklecode]
                    else:
                        raise ValueError("pickle.py appears to have a pickle opcode with name %r and code %r, but we don't" % (name, picklecode))
            else:
                picklecode = picklecode.decode('latin-1')
                if picklecode in copy:
                    if verbose:
                        print('checking name %r w/ code %r for consistency' % (name, picklecode))
                    d = copy[picklecode]
                    if d.name != name:
                        raise ValueError("for pickle code %r, pickle.py uses name %r but we're using name %r" % (picklecode, name, d.name))
                    del copy[picklecode]
                else:
                    raise ValueError("pickle.py appears to have a pickle opcode with name %r and code %r, but we don't" % (name, picklecode))
    if copy:
        msg = ["we appear to have pickle opcodes that pickle.py doesn't have:"]
        for (code, d) in copy.items():
            msg.append('    name %r with code %r' % (d.name, code))
        raise ValueError('\n'.join(msg))

def _genops(data, yield_end_pos=False):
    data = io.BytesIO(data)
    if isinstance(data, bytes_types) and hasattr(data, 'tell'):
        getpos = data.tell
    else:
        getpos = lambda : None
    while True:
        pos = getpos()
        code = data.read(1)
        opcode = code2op.get(code.decode('latin-1'))
        if opcode is None:
            if code == b'':
                raise ValueError('pickle exhausted before seeing STOP')
            else:
                raise ValueError('at position %s, opcode %r unknown' % ('<unknown>' if pos is None else pos, code))
        if opcode.arg is None:
            arg = None
        else:
            arg = opcode.arg.reader(data)
        if yield_end_pos:
            yield (opcode, arg, pos, getpos())
        else:
            yield (opcode, arg, pos)
        if code == b'.':
            break

def genops(pickle):
    return _genops(pickle)

def optimize(p):
    put = 'PUT'
    get = 'GET'
    oldids = set()
    newids = {}
    opcodes = []
    proto = 0
    protoheader = b''
    for (opcode, arg, pos, end_pos) in _genops(p, yield_end_pos=True):
        if 'PUT' in opcode.name:
            oldids.add(arg)
            opcodes.append((put, arg))
        elif opcode.name == 'MEMOIZE':
            idx = len(oldids)
            oldids.add(idx)
            opcodes.append((put, idx))
        elif 'FRAME' in opcode.name:
            pass
        elif 'GET' in opcode.name:
            if opcode.proto > proto:
                proto = opcode.proto
            newids[arg] = None
            opcodes.append((get, arg))
        elif opcode.name == 'PROTO':
            if arg > proto:
                proto = arg
            if pos == 0:
                protoheader = p[pos:end_pos]
            else:
                opcodes.append((pos, end_pos))
        else:
            opcodes.append((pos, end_pos))
    del oldids
    out = io.BytesIO()
    out.write(protoheader)
    pickler = pickle._Pickler(out, proto)
    if proto >= 4:
        pickler.framer.start_framing()
    idx = 0
    for (op, arg) in opcodes:
        frameless = False
        if op is put:
            if arg not in newids:
                pass
            else:
                data = pickler.put(idx)
                newids[arg] = idx
                idx += 1
                pickler.framer.commit_frame(force=frameless)
                if frameless:
                    pickler.framer.file_write(data)
                else:
                    pickler.write(data)
        elif op is get:
            data = pickler.get(newids[arg])
        else:
            data = p[op:arg]
            frameless = len(data) > pickler.framer._FRAME_SIZE_TARGET
        pickler.framer.commit_frame(force=frameless)
        if frameless:
            pickler.framer.file_write(data)
        else:
            pickler.write(data)
    pickler.framer.end_framing()
    return out.getvalue()

def dis(pickle, out=None, memo=None, indentlevel=4, annotate=0):
    stack = []
    if memo is None:
        memo = {}
    maxproto = -1
    markstack = []
    indentchunk = ' '*indentlevel
    errormsg = None
    annocol = annotate
    for (opcode, arg, pos) in genops(pickle):
        if pos is not None:
            print('%5d:' % pos, end=' ', file=out)
        line = '%-4s %s%s' % (repr(opcode.code)[1:-1], indentchunk*len(markstack), opcode.name)
        maxproto = max(maxproto, opcode.proto)
        before = opcode.stack_before
        after = opcode.stack_after
        numtopop = len(before)
        markmsg = None
        if stack[-1] is markobject:
            if markstack:
                markpos = markstack.pop()
                if markpos is None:
                    markmsg = '(MARK at unknown opcode offset)'
                else:
                    markmsg = '(MARK at %d)' % markpos
                while stack[-1] is not markobject:
                    stack.pop()
                stack.pop()
                try:
                    numtopop = before.index(markobject)
                except ValueError:
                    numtopop = 0
            else:
                errormsg = markmsg = 'no MARK exists on stack'
        if (markobject in before or opcode.name == 'POP') and stack and opcode.name in ('PUT', 'BINPUT', 'LONG_BINPUT', 'MEMOIZE'):
            if opcode.name == 'MEMOIZE':
                memo_idx = len(memo)
                markmsg = '(as %d)' % memo_idx
            else:
                memo_idx = arg
            if memo_idx in memo:
                errormsg = 'memo key %r already defined' % arg
            elif not stack:
                errormsg = "stack is empty -- can't store into memo"
            elif stack[-1] is markobject:
                errormsg = "can't store markobject in the memo"
            else:
                memo[memo_idx] = stack[-1]
        elif opcode.name in ('GET', 'BINGET', 'LONG_BINGET'):
            if arg in memo:
                after = [memo[arg]]
            else:
                errormsg = 'memo key %r has never been stored into' % arg
        if arg is not None or markmsg:
            line += ' '*(10 - len(opcode.name))
            if arg is not None:
                line += ' ' + repr(arg)
            if markmsg:
                line += ' ' + markmsg
        if annotate:
            line += ' '*(annocol - len(line))
            annocol = len(line)
            if annocol > 50:
                annocol = annotate
            line += ' ' + opcode.doc.split('\n', 1)[0]
        print(line, file=out)
        if errormsg:
            raise ValueError(errormsg)
        if len(stack) < numtopop:
            raise ValueError('tries to pop %d items from stack with only %d items' % (numtopop, len(stack)))
        if numtopop:
            del stack[-numtopop:]
        if markobject in after:
            markstack.append(pos)
        stack.extend(after)
    print('highest protocol among opcodes =', maxproto, file=out)
    if stack:
        raise ValueError('stack not empty after STOP: %r' % stack)

class _Example:

    def __init__(self, value):
        self.value = value

def _test():
    import doctest
    return doctest.testmod()

    import argparse
    parser = argparse.ArgumentParser(description='disassemble one or more pickle files')
    parser.add_argument('pickle_file', type=argparse.FileType('br'), nargs='*', help='the pickle file')
    parser.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), help='the file where the output should be written')
    parser.add_argument('-m', '--memo', action='store_true', help='preserve memo between disassemblies')
    parser.add_argument('-l', '--indentlevel', default=4, type=int, help='the number of blanks by which to indent a new MARK level')
    parser.add_argument('-a', '--annotate', action='store_true', help='annotate each line with a short opcode description')
    parser.add_argument('-p', '--preamble', default='==> {name} <==', help='if more than one pickle file is specified, print this before each disassembly')
    parser.add_argument('-t', '--test', action='store_true', help='run self-test suite')
    parser.add_argument('-v', action='store_true', help='run verbosely; only affects self-test run')
    args = parser.parse_args()
    if args.test:
        _test()
    else:
        annotate = 30 if args.annotate else 0
        if not args.pickle_file:
            parser.print_help()
        elif len(args.pickle_file) == 1:
            dis(args.pickle_file[0], args.output, None, args.indentlevel, annotate)
        else:
            memo = {} if args.memo else None
            for f in args.pickle_file:
                preamble = args.preamble.format(name=f.name)
                args.output.write(preamble + '\n')
                dis(f, args.output, memo, args.indentlevel, annotate)