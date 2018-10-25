import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='localizablestrings',
    version='1.0',
    author='Jan Hülsbergen',
    author_email='jan@afoo.de',
    description='Localizable.strings reader and writer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/afoo/localizablestrings',
    py_modules=['localizablestrings'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License'
    ]
)
