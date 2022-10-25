import re
@_extend_docstrings
class EmailPolicy(Policy):
    message_factory = EmailMessage
    utf8 = False
    refold_source = 'long'
    header_factory = HeaderRegistry()
    content_manager = raw_data_manager

    def __init__(self, **kw):
        if 'header_factory' not in kw:
            object.__setattr__(self, 'header_factory', HeaderRegistry())
        super().__init__(**kw)

    def header_max_count(self, name):
        return self.header_factory[name].max_count

    def header_source_parse(self, sourcelines):
        (name, value) = sourcelines[0].split(':', 1)
        value = value.lstrip(' \t') + ''.join(sourcelines[1:])
        return (name, value.rstrip('\r\n'))

    def header_store_parse(self, name, value):
        if hasattr(value, 'name') and value.name.lower() == name.lower():
            return (name, value)
        if isinstance(value, str) and len(value.splitlines()) > 1:
            raise ValueError('Header values may not contain linefeed or carriage return characters')
        return (name, self.header_factory(name, value))

    def header_fetch_parse(self, name, value):
        if hasattr(value, 'name'):
            return value
        value = ''.join(linesep_splitter.split(value))
        return self.header_factory(name, value)

    def fold(self, name, value):
        return self._fold(name, value, refold_binary=True)

    def fold_binary(self, name, value):
        folded = self._fold(name, value, refold_binary=self.cte_type == '7bit')
        charset = 'utf8' if self.utf8 else 'ascii'
        return folded.encode(charset, 'surrogateescape')

    def _fold(self, name, value, refold_binary=False):
        if hasattr(value, 'name'):
            return value.fold(policy=self)
        maxlen = self.max_line_length if self.max_line_length else float('inf')
        lines = value.splitlines()
        refold = self.refold_source == 'all' or self.refold_source == 'long' and any(len(x) > maxlen for x in lines[1:])
        if refold or refold_binary and _has_surrogates(value):
            return self.header_factory(name, ''.join(lines)).fold(policy=self)
        return name + ': ' + self.linesep.join(lines) + self.linesep
