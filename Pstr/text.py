#!/usr/bin/python3

# -*- coding: UTF-8 -*-

## 
from pstr import pss
## 

def _all(Text, Message, Icon, Color, Txtco, TType, SStyle, Interrupt=True, space=''):
    
    if Interrupt:
       return pss(f"{Color}{space}{Icon}{Message}\033[0m <!{Txtco}>{Text} \033[0m", Type=TType, Style=SStyle)
    else:
       return pss(f"{Color}{Text}<!e>")

def err(text, message=" Error:", color='w', interrupt=True, Type='color', Style='bold', icon='[x]', space='', pr=False):
    if pr:
        print(_all(text, message, icon, '<!196>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!196>', color, Type, Style, interrupt, space)

def info(text, message=" Info:", color='w', interrupt=True, Type='color', Style='bold', icon='[!]', space='', pr=False):
    if pr:
        print(_all(text, message, icon, '<!11>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!11>', color, Type, Style, interrupt, space)

def que(text, message=" Question:", color='w', interrupt=True, Type='color', Style='bold', icon='[?]', space='', pr=False):
    if pr:
        print(_all(text, message, icon, '<!32>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!32>', color, Type, Style, interrupt, space)

def bad(text, message=" Bad:", color='w', interrupt=True, Type='color', Style='bold', icon='[-]', space='', pr=False):
    if pr:
        print(_all(text, message, icon, '<!196>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!196>', color, Type, Style, interrupt, space)

def good(text, message=" Good:", color='w', interrupt=True, Type='color', Style='bold', icon='[+]', space='', pr=False):
    if pr:
        print(_all(text, message, icon, '<!35>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!35>', color, Type, Style, interrupt, space)

def run(text, message=" Run:", color='w', interrupt=True, Type='color', Style='bold', icon='[~]', space='', pr=False):
    if pr:
         print(_all(text, message, icon, '<!231>', color, Type, Style, interrupt, space))
    else:
        return _all(text, message, icon, '<!231>', color, Type, Style, interrupt, space)


def black(text , pr=True, Style='bold', Type='color'):
    	
    if pr:
    	pss(f"<!bl>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def red(text , pr=True, Style='bold', Type='color'):

    if pr:
        pss(f"<!r>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def green(text , pr=True, Style='bold', Type='color'):

    if pr:
    	pss(f"<!g>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def yellow(text , pr=True, Style='bold', Type='color'):

    if pr:
    	pss(f"<!y>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def blue(text , pr=True, Style='bold', Type='color'):

    if pr:
   		pss(f"<!bu>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def magenta(text , pr=True, Style='bold', Type='color'):

    if pr:
    	pss(f"<!m>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)

def cyan(text , pr=True, Style='bold', Type='color'):

    if pr:
    	pss(f"<!c>{text}<!e>", pr=True, Style=Style, Type=Type)
    else:
    	return pss(text)