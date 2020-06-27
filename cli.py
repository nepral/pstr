#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pstr
# from optparse import OptionParser

# import sys


# def _parse_args():
#     parser = OptionParser(
#         usage='pstr [options] <text>',
#         description='Simple program for Python pstr Library.',
#         version='pstr 1.0.3'
#     )
        
#     parser.add_option(
#         '-f', '--fg',
#         dest='fgcolor',
#         # type='int',
#         help='set foreground color',
#         # default='w'
#     )
    
#     parser.add_option(
#         '-B', '--base',
#         # type='int',
#         help='expand the other operations',
#         # default=Base.Null.value
#     )
    
#     parser.add_option(
#         '-b', '--bg',
#         dest='bgcolor',
#         # type='int',
#         help='set backround color',
#         default='no'
#     )
    
#     (opts, args) = parser.parse_args()

#     if not args:
#         parser.print_help()
#         exit(1)
        
#     return opts, args[0]
    

# def _colorize(arg, fakedict):
#     opts = fakedict.__dict__
#     color = f"<!{opts['fgcolor']}>{arg}" if len(opts['fgcolor']) <= 3 else f"<{opts['fgcolor']}>{arg}" 
#     background = f"<?{opts['bgcolor']}>{arg}"
#     pstr.pss(color+background, pr=True)
#     # pstr.pss(f"<{opts['fgcolor']}><!{opts['fgcolor']}><?{opts['bgcolor']}>{arg}", pr=True)
#     # cprint(arg, fg=opts['fgcolor'], bg=opts['bgcolor'], base=opts['base'])
    
# def main():
#     (opts, arg) = _parse_args()
#     _colorize(arg, opts)
    
# if __name__ == '__main__':
#     main()