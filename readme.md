upprint
=======

This is a modified version of the built-in `pprint` module that is better
able to print Unicode characters. Instead of printing the codepoints,
it prints the actual Unicode characters themselves.

The code for this module is a slightly modified version of an answer written
on Stack Overflow by user Georg: http://stackoverflow.com/a/10883893/3553425

To use:

    from upprint import upprint
    upprint({u'あ': '亜')}


License
-------

MIT licensed.
