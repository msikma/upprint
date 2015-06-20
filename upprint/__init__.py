# coding=utf8
#
# (C) 2015, MIT License

'''
A Unicode version of pprint that is able to display non-Latin characters
in its output. It does this by overriding the default usage of repr()
to display Unicode instances.

Slightly modified version of the original by user georg on Stack Overflow:
<http://stackoverflow.com/a/10883893/3553425>

To use:

    from upprint import upprint
    upprint({u'あ': '亜')}

It's identical in usage to pprint except for the way it outputs Unicode
characters.
'''
import pprint


class upprinter(pprint.PrettyPrinter):
    def __call__(self, *args, **kwargs):
        return self.pprint(*args, **kwargs)

    def format(self, obj, context, maxlvls, lvl):
        if isinstance(obj, unicode):
            return '\'' + obj.encode('utf8') + '\'', True, False
        return pprint.PrettyPrinter.format(self, obj, context, maxlvls, lvl)

# Return object instead of the class.
upprint = upprinter()
