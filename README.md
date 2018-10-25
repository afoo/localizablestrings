# Localizablestrings

A simple reader and writer for Localizable.strings files as used by Xcode projects.

## Installation

`pip install localizablestrings`

## Usage

```python
from localizablestrings import StringsFile, Translation

sf = StringsFile('/path/to/Localizable.strings')

for translation in sf:
    print(f'Key = {translation.key}\nValue = {translation.value}\nComment = {translation.comment}')

if sf.get_translation('spam') is None:
    new_translation = Translation(key='spam', value='eggs', comment='Needs more bacon')
    sf.add_translation(new_translation)

s.write()

```