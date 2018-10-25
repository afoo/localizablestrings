import shlex


class Translation:
    def __init__(self, comment=None, key=None, value=None):
        self.comment = comment
        self.key = key
        self.value = value

    def __repr__(self):
        return 'Translation(key={!r}, value={!r}, comment={!r})'.format(
            self.key, self.value, self.comment)

    def __str__(self):
        return self.key


class StringsFile:
    def __init__(self, path=None, encoding='utf-16'):
        self.path = path
        self.encoding = encoding
        self.translations = []
        if self.path is not None:
            self._parse()

    def __iter__(self):
        return iter(self.translations)

    def add_translation(self, translation):
        self.translations.append(translation)

    def get_translation(self, key):
        for translation in self.translations:
            if translation.key == key:
                return translation

    def write(self, path=None):
        if path is None:
            path = self.path
        with open(path, mode='w+', encoding='utf-16') as fh:
            for trans in self.translations:
                fh.write('{}\n"{}" = "{}";\n\n'.format(
                    '/* {} */'.format(trans.comment) if trans.comment else '',
                    trans.key,
                    trans.value))

    def _parse(self):
        with open(self.path, encoding=self.encoding) as fh:
            cur_trans = Translation()
            in_comment = False
            cur_comment = ''
            for line in fh:
                line = line.strip().rstrip(';')
                if not line:
                    continue
                if line.startswith('//'):
                    continue
                if line.startswith('/*'):
                    in_comment = True
                    cur_comment = ''
                    line = line.replace('/*', '').strip()
                if in_comment:
                    if line.endswith('*/'):
                        in_comment = False
                        cur_comment += line.replace('*/', '').strip()
                        cur_trans.comment = cur_comment
                    else:
                        cur_comment += line + '\n'
                    continue
                tokens = shlex.split(line)
                cur_trans.key = tokens[0]
                cur_trans.value = tokens[2]
                self.translations.append(cur_trans)
                cur_trans = Translation()
