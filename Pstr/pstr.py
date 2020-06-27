# -*- coding: UTF-8 -*-

"""
author        : Osama Mohammed Al-zabidi
email         : osamanepral@gmail.com
phone         : +(967) 717448593
Version       : 1.0.3
coding        : utf-8
"""

from __future__ import print_function, unicode_literals
from sys import stdout, stdin, stderr, version, version_info
from os import remove, path, getcwd
import re
from time import sleep, strftime

# importing for emoje, encode text
try:
    from icons_files import unicode_codes, icons_str, icons_without_codePoint
except ImportError:
    from pstr.icons_files import unicode_codes
    from pstr.icons_files import icons_str
    from pstr.icons_files import icons_without_codePoint



__all__ = [
    'pcolor', 'pss','Write','sup','sub','hr','url',
    'figlet','toilet','postion','slowIndex','slowLine',
    'everStr','box','find','findCo','file','rtext','config',
    'passwd','prss','inpss','emojize','demojize',
    'get_emoji_regexp','emoji_count','emoji_list',
    'icon','get_icon_regexp','icon_count','icon_list',
    'dicon','hrLoad','Loading','prog_bar', 'show_all',

    'black', 'red', 'green', 'yellow', 
    'magenta', 'cyan','err', 'info', 
    'que', 'bad', 'good', 'run', 'blue', 
]

__version__ = "1.0.3"
'''
1 + 1
0 + 3
3 + 3
'''
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

_ICON_REGEXP = None
_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ":"

PY2 = version_info[0] == 2
if version[0] < '3':
    print(" ! This module not Working in Python Version 2.x, Please update Python to 3.x")


def Sum_code(f_v, r_k1, r_k2, var, fme=None):
    for f_k in f_v:
        var = var.replace(r_k1 + f_k + r_k2, f_v[f_k])
        if fme is not None:
            var = var.replace(r_k1 + f_k + r_k2, fme)
    return var

class pcolor:
    """
    Usage:
    pss = pcolor.Pss
    pss(TEXT, pr=True)
        TEXT = str or any thing
     	and in str write like this 

    color/background:
        "<!y>Hello <!g>World <!m>!!<!e>"
        "<?y>Hello <?g>World <?m>!!<!e>"
        "<$u><$r> Hello <$r><!g>World"

    emoje:
        "I,m fine <:thumbs_up:>"
        "I,m fine :thumbs_up:" 
        "I,m fine <&thumbs_up>"

    icons:
        "This is python icon <@python>"
        "This is python icon <ico>python</ico>"

    text:
        "This is sub text <sub>python</sub>"
        "This is sup text <sup>python</sup>"
        "This is hr line <hr>python</hr>"

image about code :
    ------------------------------------
    <!code>  = for color
    <?code>  = for background color
    <@code>  = for print icon
    <&code>  = for print emoje
    <:code:> = for print emoje
    :code:   = for print emoje
    <+code>  = for print sup text
    <-code>  = for print sub text
    <code>   = color or any thing but not alias
    <sup>code</sup>
    <sub>code</sub>
    <ico>code</ico>
    <em>code</em>
    <hr>code</hr>
    -------------------------------------
    <$u> 	 = Underline
    <$i>     = Italic
    <$r>     = Reversed = select on text
    <$s>     = Strike/strikethrough
    <$l>     = lamb
    <$h>     = hide
    <$br>    = bright
    <$bo>    = bold
    -------------------------------------
    
types:
    - no
    - bright
    - bold
    - family
    - underline
    - reverse
    - hide
    - middleline
    - lamb
    - dark
    - light
            
styls:
    - bg = background
    - co = color 

example:
    <!y>   = yellow
    <!e>   = use this in end any color or background color
        
try:
    help(pstr), or
    dir(pstr)
    """
    def show_me(self):
            pss = self.Pss
            # print(pcolor.__doc__)
            # Colors :
            print("\n  print(pcolor.__doc__) for show how to use pstr")
            print('\n  These Color: \n  chose any number for select Color !!\n')
            for i in range(0, 16):
                for j in range(0, 16):
                    code = str(i * 16 + j)
                    # code = str(35)
                    print(u"\u001b[38;5;" + code + "m "+ code.ljust(4),end='')
                    # sys.stdout.write()
                print (u"\u001b[0m")

            # Background :
            print("\n\n\n  These Background Color: \n  chose any number for select Background color !!\n")
            for i in range(0, 16):
                for j in range(0, 16):
                    code = str(i * 16 + j)
                    print(u"\u001b[48;5;" + code + "m " + code.ljust(4),end='')
                    # sys.stdout.write()
                print (u"\u001b[0m")

    # def __init__(self, Type='', Style='bold'):
    #     global Tc, St, Txco

    #     self.Type = Type
    #     self.Style = Style

    #     if self.Type in ("Co", "co", "color",'',' '):
    #         Tc = 30
    #     elif self.Type in ("bg", "background", "BG", "Bg", "bG"):
    #         Tc = 40
    #     else:
    #         print(" [ ✗ ] Oh no this argument not found ...")

    #     ST = {
    #         'no'            : 0,
    #         'bright'        : 2,
    #         'bold'          : 1 ,
    #         'family'        : 3,
    #         'underline'     : 4,
    #         'reverse'       : 7,
    #         'hide'          : 8,
    #         'middleline'    : 9,
    #         'lamb'          : 5,
    #         ''              : 1}
    #     St = ST[Style]
#################################################################

    def Pss(self, Text, pr=False, emoje_aliase=True,
            Type='color', Style='bold', remove=False, 
            End='\n', File=stdout, Sep='', Flush=False):
        

        """
        bl = Black
        r  = Red
        g  = Greend
        y  = Yellow
        b  = Blue
        m  = Magenta
        p  = purple
        c  = Cyan
        w  = White
        o  = Orange
        b  = bright black
        e  = End color
        
        Parameters:
            Text = string or any thing
            pr   = if (False) will return a text
            emoje_aliase = alias for emoje name
            Type   = color or backgrond : co/bg
            Style  = bold, bright, underline, etc...
            End    = end in print function
            Sep    = sep in print function
            File   = file in print function
            Flush  = flush in print function
        """

        if Type in ("Co", "co", "color", "cl"):
            Tc = 30
        elif Type in ("bg", "background", "BG", "Bg", "bG"):
            Tc = 40
        else:
            print(" [ ✗ ] Oh no This argument not found ...")

        ST = {
            'no'       : 0, 'bright'     : 2,
            'bold'     : 1, 'italic'     : 3,
            'underline': 4, 'reverse'    : 7,
            'concealed': 8, 'middleline' : 9,
            'hide'     : 8, 'crossedout' : 9,
            'blinkslow': 5, ''           : 1,
            'dark'     : 0, 'light'      : 1,
            'reset'    : 0, 'blinkrapid' : 6,
            'null'     : 10}

        St = ST[Style]
        NC = Tc
        nt = St
        try:
            NumColor = {
                'bl': NC+0,  'r' : NC+1,
                'g' : NC+2,  'y' : NC+3,
                'b' : NC+4,  'm' : NC+5,
                'c' : NC+6,  'w' : NC+7,
                'no': NC-NC, 'e' : NC-NC, 
                'p' : NC+5,  'bu': NC+4}

            Comm = {
                'u' : 4, 's' : 9,
                'i' : 3, 'r' : 7,
                'h' : 8, 'bs': 5,
                'br': 6, 'c' : 8, 
                'bo': 1, 'br': 2,
                'd' : 0, 'lg': 1,
                'no': 0, 'f' : 2,
                'null' : 10}

            Color_2 = {
				"normal":'\033[0m',
                "end":'\033[0m',
                "e":'\033[0m',
                
                "black" : '\u001b[2m', # black
                "dgrey" : f'\033[1;30m',
                "grey"  : f'\033[{nt};30m', # grey
                "red"   : f'\033[{nt};31m', # red
                "green" : f'\033[{nt};32m', # green
                "yellow": f'\033[{nt};33m', # yellow
                "blue"  : f'\033[{nt};34m', # blue
                "purple": f'\033[{nt};35m', # purple
                "cyan"  : f'\033[{nt};36m', # cyan
                "white" : f'\033[{nt};37m', # white

                'Bl#' : f'\033[{nt};30m',
                'R#'  : f'\033[{nt};31m',
                'G#'  : f'\033[{nt};32m',
                'Y#'  : f'\033[{nt};33m',
                'B#'  : f'\033[{nt};34m',
                'P#'  : f'\033[{nt};35m',
                'C#'  : f'\033[{nt};36m',
                'W#'  : f'\033[{nt};37m',

                "lblack" : f'\033[{nt};30m', # black
                "lgrey"  : f'\033[{nt};30m', # grey
                "lred"   : f'\033[{nt};31m', # red
                "lgreen" : f'\033[{nt};32m', # green
                "lyellow": f'\033[{nt};33m', # yellow
                "lblue"  : f'\033[{nt};34m', # blue
                "lpurple": f'\033[{nt};35m', # purple
                "lcyan"  : f'\033[{nt};36m', # cyan
                "lwhite" : f'\033[{nt};37m', # white

                "reset":'\033[0m',
                "bold":'\033[01m',
                "disable":'\033[02m',
                "underline":'\033[04m',
                "reverse":'\033[07m',
                "strikethrough":'\033[09m',
                "invisible":'\033[08m'}

            ## this for background color
            for bgcolor in NumColor:
                # bgcolor = str(bgcolor)
                if St == 0:
                    nt = ''
                Text = Text.replace("<?" + bgcolor + ">", f"\u001b[{NumColor[bgcolor]+10};{nt}m")

            ## this for text color
            Text = Sum_code(Color_2, "<", ">", Text)

            ## this code for Color way
            for color in NumColor:
                if St == 0:
                    nt = ''
                if color in ('e', 'E', 'end', 'no', 'No', 'End'):
                    Text = Text.replace("<!" + color + ">", f"\u001b[0m")
                Text = Text.replace("<!" + color + ">", f"\u001b[{NumColor[color]};{nt}m")

            ## this color by number
            for i in range(0, 256):
                i = str(i)
                # Css = u"\u001b[38;5;" + i + "m"
                Text = Text.replace("<!" + i + ">", u"\u001b[38;5;" + i + "m")

            ## this background color by number
            for s in range(0,256):
                s = str(s)
                Text = Text.replace("<?" + s + ">", u"\u001b[48;5;" + s + "m")

            ## this for Style commands
            for command in Comm:
                    Text = Text.replace("<$" + command + ">", f"\u001b[{NumColor[color]};{Comm[command]}m")
            ## emojes            
            dict_emoje = unicode_codes.EMOJI_ALIAS_UNICODE if emoje_aliase else unicode_codes.EMOJI_UNICODE
            Text = Sum_code(dict_emoje, "<:", ":>", Text)
            Text = Sum_code(dict_emoje, "<em>", "</em>", Text)
            Text = Sum_code(dict_emoje, ":", ":", Text)
            Text = Sum_code(dict_emoje, "<&", ">", Text)
            
            ## icons
            Text = Sum_code(icons_str.icons_text, "<ico>", "</ico>", Text)
            Text = Sum_code(icons_str.icons_text, "<@", ">", Text)

            ## sub/sup text
            Text = Sum_code(unicode_codes.sub_script_map, "<sub>", "</sub>", Text)
            Text = Sum_code(unicode_codes.sup_script_map, "<sup>", "</sup>", Text)
            Text = Sum_code(unicode_codes.sup_script_map, "<+", ">", Text)
            Text = Sum_code(unicode_codes.sub_script_map, "<-", ">", Text)

            pattern = re.compile(u'(<hr>[a-zA-Z0-9\\+\\-_&.ô’Åéãíç()!#*]+</hr>)')
            matches = pattern.finditer(Text)
            for matche in matches:
                fin = Text.find(matche.group(0))
                # print(fin)
                # print(matche.group(0))
                Text =  Text.replace("<hr>", "").replace("</hr>", "") + '\n' + ' '*fin + '─'*len(matche.group(0).replace("<hr>", "").replace("</hr>", ""))

            if pr:
                print(Text, sep=Sep, file=File, end=End, flush=Flush)
            else:
                return Text

        except KeyError as kerr:
            print(f" ✗ Oh no This color or key not found !, {kerr}")
        
        except AttributeError:
            if pr:
                print(Text, sep=Sep, file=File, end=End, flush=Flush)
            else:
                return Text

pcolor = pcolor()
pss = pcolor.Pss

### for run pstr helper :
# print(help(pcolor))
# pcolor.examples()

###################### slow write #####################
def Write(text, t=0.1, CLT='g', CUT='w',
         space=0, start=0, end=1,
         animate=False, right=10,
         ever=['lower', ''], pr=True,
         sound=False, sound_path=""):

    from playsound import playsound
    if animate: 
        try:
            text = ' '*start +text.strip("\n")+' '*end
            text = pss(text)
            for i in range(1):#
                for i in range(0, len(text)):
                    if ever[0] in ("lower"):
                        # from lower to upper
                        if ever[1] in ("cap", "upper"):
                            pss(f"<!{CLT}>{text[:i].lower()}<!e>{' '*space}<!{CUT}>{text[i:].upper()}<!e>", End='\r', pr=True)
                            if sound:
                                playsound(sound_path)
                        elif ever[1] in ("no", "normal"):
                            pss(f"{text[:i]}{' '*space}{text[i]}", End='\r', pr=True)
                            if sound:
                                playsound(sound_path)
                        else:
                            pss(f"<!{CLT}>{text[:i].lower()}<!e>{' '*space}<!{CUT}>{text[i].upper()}<!e>", End='\r', pr=True)
                            if sound:
                                playsound(sound_path)
                    elif ever[0] in ("upper"):
                        # from uppder to lower
                        pss(f"<!{CLT}>{text[:i].upper()}<!e>{' '*space}<!{CUT}>{text[i].lower()}<!e>", End='\r', pr=True)                                    
                        if sound:
                            playsound(sound_path)
                    sleep(t)

            print('')
        except KeyboardInterrupt as e:
            print('\n'+ type(e).__name__ + ": Termainated", file=stderr)
            exit(1)
    else:
        Text = pss(text)
        for i in Text:
            try:
                if sound:
                    playsound(sound_path)
                    print(i, flush=True, end='')
                    sleep(t)
                else:
                    print(i, flush=True, end='')
                    sleep(t)
            except KeyboardInterrupt as e:
                print('\n'+ type(e).__name__ + ": Termainated")
                exit(1)
###################### super Script #####################
def sup(text, pr=False):
    """
    >> import pstr
	>> pstr.sup('This pstr module print sup script')
	## output:
	>> ᵀʰᶦˢ ᵖˢᵗʳ ᵐᵒᵈᵘˡᵉ ᵖʳᶦⁿᵗ ˢᵘᵖ ˢᶜʳᶦᵖᵗ

	:param:>
		text 	= str  :  string for translate to sub string
		pr  	= bool :  True=print or False=return
		color 	= str  :  y=yellow, g=green, etc...
		bg 		= str  :  y=yellow, g=green, etc...
    """

    for k, v in unicode_codes.sup_script_map.items():
        text = text.replace(k, unicode_codes.sup_script_map.get(k, k))

    if pr:
        pcolor.Pss(text, pr=True)
    else:
        return text

###################### sub Script #####################
def sub(text, pr=False):
    """
	>> import pstr
	>> pstr.sub('This pstr module print sub script')
	## output:
	>> ₜₕᵢₛ ₚₛₜᵣ ₘₒᑯᵤₗₑ ₚᵣᵢₙₜ ₛᵤₚ ₛ꜀ᵣᵢₚₜ

	:param:>
		text 	= str  :  string for translate to sub string
		pr  	= bool :  True=print or False=return
		color 	= str  :  y=yellow, g=green, etc...
		bg 		= str  :  y=yellow, g=green, etc...
    """
    for k, v in unicode_codes.sub_script_map.items():
        text = text.replace(k, unicode_codes.sub_script_map.get(k, k))
    if pr:
        pcolor.Pss(text, pr=True)
    else:
        return text

def hr(text, pr=False, Type='u'):
    """
    Types:
        n : -
        r : ·
        u : _
        s : ─
    """
    alls = {    
    'n' : '-',
    'r' : '·',
    'u' : '_',
    's' : '─'}
    suffix = alls[Type]
    # print(text+'\n ─'*len(text))
    # print(text+'\n'+'─'*len(text))
    tfn = text.find(text)
    TEXT = text + '\n' + ' '*tfn + f'{suffix}'*len(text)
    if pr:
        pcolor.Pss(TEXT, pr=True)
    else:
        return TEXT

def url(text, pr=False, color="blue"):
    if pr:
        pss(f"<{color}>" + text + "<e>", Style='underline', pr=True)
    else:
        return pss(f'<{color}>{text}<!e>',Style='underline')
        
def findCo(Text, word, color='r', pr=False):
    All_find = f"<!{color}>{word}<!e>"
    FindCo = re.sub(word, All_find, Text)
    if pr:
        pss(FindCo, pr=True)
    else:
        return pss(FindCo)

def find(Text, word, back='', after='',  pr=False):
    Find = re.sub(word, f'{back}{word}{after}', Text)
    if pr:
        pss(Find, pr=True)
    else:
        return pss(Find)

def file(file, line=0, color='no', before_num='│',
        grep='', grep_color='r', grep_set='',
        show_num=False, color_num='no', suffix='',
        suffix_color='', show_space=True,
        End='', Type='color', Style='bold',
        pr=True, Unicode=False, effect=["none", 0.01]):

        """
        :param effect = ws, wa, w
            ws = write with sound
            wa = write with animate
            w  = write 
        """
        animate_ = False if effect[0] in ("w", "write") else True
        with open(file, 'r', encoding='utf-8') as FSa: #'utf-8'
                if line in ("*", "all", "end"):
                    FI = FSa.readlines()[0:]
                else:
                    FI = FSa.readlines()[0:int(line)]
                    
                for fil in enumerate(FI):
                    if grep:
                    	ali = findCo(Text=fil[1], word=grep, color=grep_color)
                    else:
                    	ali = fil[1]

                    if show_space == False:
                        ali = fil[1].lstrip()
                        end = '\n'

                    if show_num:
                       num = fil[0]+1

                    else:
                        num = ''

                    if effect[0] in ("w", "write", "wa", "write animate"):
                        Write(f"{before_num}<!{color_num}>{num}<!e>{suffix_color}{suffix}<!{color}>{ali}<!e>", pr=True, animate=animate_, t=effect[1])
                    
                    elif Unicode:
                        pss(f"{before_num}<!{color_num}>{num}<!e>{suffix_color}{suffix}<!{color}>{ali}<!e>".encode('utf-8'), Type=Type, Style=Style, End=End, pr=pr)
                    else:
                        pss(f"{before_num}<!{color_num}>{num}<!e>{suffix_color}{suffix}<!{color}>{ali}<!e>", Type=Type, Style=Style, End=End, pr=pr)
                FSa.close()
                exit(0)

def rtext(File, word=[], rep=''):
    """
    if file not exsits will created new file

    File = file path
    word = words for replace
    rep  = word replace
    """
    infile = File
    outfile = File

    fin = open(infile)
    remove(File)

    fout = open(outfile, "w+")
    for line in fin:
        for Word in word:
            if re.search(f"({Word})", line):
                line = line.replace(Word, rep)
                print(word)
        fout.write(line)
    fin.close()
    fout.close()



# def _rep(text: str, rep_list: str, new_rep=""):
#   for i in rep_list.split(" "):
#       text = str(text).replace(f"{i}", new_rep)
#   return str(text)
# def char(text: str):
#   text = str(text).replace("\\t", " "*4).replace("\\n", "\n").replace("\\", "")
#   return text


def rep(text: str, rep_list: str, new_rep=""):
		for i in rep_list.split(" "):
			text = str(text).replace(f"{i}", new_rep)
		return str(text)

def char(text: str):
	text = str(text).replace("\\t", " "*4).replace("\\n", "\n")
	return text

############ configuare class for python #################3
class config:
    def __init__(self, file, path): # complit path
        self.file = file
        self.path = path.replace(".", getcwd()+"/")

    def creat(self, message):
    	with open(self.path+self.file, "a") as file:
	    	len_str = 50 if int(len(message)) < 40 else int(len(message))

	    	message_ = f"""\
##{'#'*len_str}###
# {message}

// @NOTE: use (_) for one space don't use space way
// @NOTE: you can use: (\\t \\n) for tab/new line
// @NOTE: you can use: (// or #) for comment line
##{'#'*len_str}###"""
	    	file.write(message_)
	    	file.close()

    def unique(self, key, suffix="=", hide_space=True, err_message=False, pr=False):
        with open(str(self.path+self.file), "r") as file:
            pattern = re.compile(r"\W*{}*\s*{}\s*\S*\d*".format(key, suffix))
            als = pattern.findall(file.read())
            return_ = char(rep(str(als).split("=")[0], f"' \" ] [", ""))
            return_ = return_.strip() if hide_space else return_
            ret_str = "ok" if return_ == key else "no"
            if pr: print(ret_str)            	
            else: return ret_str
            file.close()

    def set(self, key, value, suffix="=", 
    		comment=False, comment_message=None, set_type="str"):

        with open(str(self.path+self.file), "a") as file:
        	if self.unique(key) == "ok":
        		print("this key is alerady usage")
        	else:
        		com = "# " if comment else ""
        		comm_mes = "" if comment_message == None else f"\n## {comment_message}"
        		set_value = value.replace(" ", "_")
        		if   set_type.lower() == "str":   set_text = f""""{set_value}" """
	        	elif set_type.lower() == "int":   set_text = f"""{int(set_value)}"""
	        	elif set_type.lower() == "list":  set_text = f"""{set_value.split()}"""
	        	elif set_type.lower() == "tuple": set_text = f"""{tuple(set_value.split())}"""
	        	elif set_type.lower() == "set":   set_text = f"""{set(set_value.split())}"""
	        	elif set_type.lower() == "float": set_text = f"""{float(set_value)}"""
	        	elif set_type.lower() == "time":  set_text = f"""{strftime(set_value)}"""
	        	else: set_text = set_value
        		text = f"{comm_mes}\n{com}{key}{suffix}{set_text}"
	        	file.write(text)
	        	file.close()
	    
    def get(self, cfg: str, suffix="=", return_type="default", chars=False,
            comments=("#", "//"), hide_space=True, err_message=False, pr=False):
      """
      @NOTE: Don't use a space in last value (text/int)

      if chars is True will use char from default like this
          @List: arg1,arg2,arg3,...etc
          will split text use: (,)

	  @NOTE: use thsi (_) for on space
      return_type:
      	- int
      	- str
      	- list
      	- tuple
      	- set
      	- float
      	- time
      	- def/default
      """
      with open(str(self.path+self.file), "r") as file:
          try:
              ## this search about key and value
              pattern = re.compile(r"\W*{}*\s*{}\s*\S*\d*".format(cfg, suffix))
              sp = " " if hide_space else ""
              als = pattern.findall(file.read().replace(sp, ""))
              return_ = char(rep(str(als).split("=")[1], f"' \" [ ]", "")).replace("_", " ").replace(" ", "")
              
              ## this for return default value from config file without any change
              return_def = char(str(als).split("=")[1][0:-1]).replace("_", " ").replace(" ", "")
              
              ## this code for get comment 
              comment_ = rep("\n"+str(als).split(suffix)[0], f"' \" [ \\t \\n \\r \\v \\s", "\n")
              
              if comment_.startswith(comments): text = None # return None

              ## this for change return value
              elif return_type.lower() in ("default", "def") : text = return_def[0:return_def.find("#")]
              elif return_type.lower() == "str":   text = str(return_) 
              elif return_type.lower() == "int":   text = int(return_)
              elif return_type.lower() == "float": text = float(return_)
              elif return_type.lower() == "list":  text = list(return_.split(","))
              elif return_type.lower() == "tuple": text = tuple(return_.split(","))
              elif return_type.lower() == "set":   text = set(return_.split(","))
              elif return_type.lower() == "time":  text = strftime(return_)
              elif hide_space: text = return_.strip()
              elif chars: text = return_.split(",")
              else: text = return_

              ## this end get function
              # exec("ret_")
              if pr: print(text)               
              else: return text

              file.close()
          except IndexError as krr:
              if err_message: prss("<!y>>> <!r>None Type.<!e>")
              else: return None

def run(code):
    exec(f"{code}")

def passwd(text, pr=False, color='no', bg='no',
          STR=False, INT=False, default='',
          suffix=':', while_close="Closing...",
          left='', right='',lenght=1000,
          lenerr='the lenght is not equal to:--> ',
          stream=stdout):
    """
    this prombt for cli :

    type        = Str, Int
    text        = any Text
    color       = back to pss for color
    default     = [text]
    suffix      = :
    right       = right from text
    left        = left from text

    while_close = KeyboardInterrupt

    you can also use any color in text
    example:
        while_close="<!r>Closeing<!e>"
        suffix="<!bu>:<!e>"
    """

    from getpass import getpass
    try:
        right = ''
        left = ''
        if default:
            default = f"[{default}]"
        pss = pcolor.Pss
        password = getpass(pss(f"{left}<!{color}><?{bg}>{text}{default}{right}{suffix}<!e> "), stream=stream)
        if len(password) > lenght:
            # print(pss(f"{lenerr} {lenght}"), file=sys.stderr)
            pss((False, password), pr=True)

        if STR and not password.isalpha():
        	return False #str(password)

        elif INT and not password.isdigit():
        	return False #int(password)
        else:
            if pr:
        	    pss(password, pr=pr)
            else:
                return password
    except (KeyboardInterrupt):
        print(pss(f"{while_close}"))


def prss(*text, pr=True, fstr='', lstr='', Type='color',
         end='\n', flush=False, file=stdout, Style='bold'): 
         # end='\n', sep='', file='', flush=False
    # txt_sp = text[0:]
    # for i in txt_sp:
    #     pss(i, End='', pr=True)

    text = pss("{}{}{}".format(fstr, *text, lstr), Style=Style, Type=Type)
    if pr:
        pss(text, End=end, Flush=flush, File=file, pr=True)
    else:
        return text

def inpss(text, pr=False, hide=False, while_close='Closing...',
    	 suffix='', fstr='', lstr='', end='', STR=False, INT=False, 
         stream=stdout, Style='bold', Type='color'):

    if not hide:
        prss(text, Style=Style, Type=Type, fstr=fstr, lstr=lstr, file=stream, pr=True, end=end) #text=text, suffix=suffix, stream=stream, while_close=while_close, left=fend, right=lend)
        try:
            IN = input()
            if STR and not IN.isalpha():
                return False
            elif INT and not IN.isdigit():
                return False
            else:
                if pr:
                    pss(IN, pr=True)
                else:
                    return IN
        except KeyboardInterrupt:
            pss(while_close, pr=True)
            exit(1)
    elif hide:
        if pr:
            passwd(text=text.strip(), suffix=suffix, stream=stream, pr=True,
                   while_close=while_close, left=fstr, right=lstr, STR=STR, INT=INT)
        else:
            return passwd(text=text.strip(), suffix=suffix, stream=stream,
                    while_close=while_close, left=fstr, right=lstr, STR=STR, INT=INT)
######################## -- this code for emoje output -- #################################

def emojize(text, aliase=True, pr=False):

    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliase.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
        >>> import pstr
        >>> print(pstr.emojize("thumbsup", aliase=True))
        Python is fun 👍
        >>> print(pstr.emojize("thumbs_up"))
        Python is fun 👍
    """
    dict_emoje = unicode_codes.EMOJI_ALIAS_UNICODE if aliase else unicode_codes.EMOJI_UNICODE
    text = Sum_code(dict_emoje, '', '', text)

    EM = dict_emoje
    for em in EM:
        text = text.replace(em, EM[em])
    if pr:
        pss(text, pr=True)
    else:
        return text

def demojize(string, aliase=False, pr=False, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.
    :param string: String contains unicode characters. MUST BE UNICODE.
    :param use_aliases: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) User delimiters other than _DEFAULT_DELIMITER
        >>> import pstr
        >>> print(pstr.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(pstr.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up:
        >>> print(pstr.demojize(u"Unicode is tricky 😯", delimiters=(" __", "__ ")))
        Unicode is tricky :hushed_face:
    """

    def replace(match):
        codes_dict = unicode_codes.UNICODE_EMOJI_ALIAS if aliase else unicode_codes.UNICODE_EMOJI
        val = codes_dict.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    if pr:
        pss(re.sub(u'\ufe0f','',(get_emoji_regexp().sub(replace, string))), pr=True)
    else:
        return re.sub(u'\ufe0f','',(get_emoji_regexp().sub(replace, string)))

def get_emoji_regexp(pr=False):

    """Returns compiled regular expression that matches emojis defined in
    ``pstr.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(unicode_codes.EMOJI_UNICODE.values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)

    if pr:
        pss(_EMOJI_REGEXP, pr=True)
    else:
        return _EMOJI_REGEXP

def emoji_count(string, pr=False):
   """Returns the count of emojis in a string"""
   c = 0
   for i in string:
     if i in unicode_codes.UNICODE_EMOJI:
          c = c+1
   if pr:
      pss(c, pr=True)
   else:
       return c

def emoji_list(string, pr=False):
    """Return the location and emoji in list of dic format
    >>>pstr.emoji_list("Hi, I am fine. 😁")
    >>>[{'location': 15, 'emoje_count': 1, emoje: '😁'}]
    """
    _entities = []
    for pos,c in enumerate(string):
        if c in unicode_codes.UNICODE_EMOJI:
            _entities.append({
                "location": pos,
                "emoji": c,
                "emoje_count": emoji_count(string)
                })
    if pr:
        pss(_entities, pr=True)
    else:
        return



######################## -- this code for icon output -- #################################

def show_all(suffix=' :==> ', icons=True, emoje=True, char=True):
    from pstr.unicode_codes import EMOJI_UNICODE
    if char:
        Icons = open(BASE_DIR+'/pstr/icons_files/Icon.txt', "r")
        pss(Icons.read(), pr=True)
    if emoje:
        for ii, ss in EMOJI_UNICODE.items():
            print(ii+'  '+ss)
    if icons:
        IC = icons_str.icons_text
        for kico, vico in IC.items():
            print(kico+f"{suffix}", vico)

def icon(text, pr=False, icon_code_point=True):

    if icon_code_point:
        text = Sum_code(icons_str.icons_text, '', '', text)
    else:
        text = Sum_code(icons_without_codePoint.IconsWithoutCodePoint, '', '', text)

    IC = icons_str.icons_text
    for ico in IC:
        text = text.replace(ico, IC[ico])
    
    if pr:
        pss(text, pr=True)
    else:
        return text

def get_icon_regexp(pr=False):
    
    """Returns compiled regular expression that matches icon defined in
    ``pstr.icons_str.icons_text``. The regular expression is only compiled once.
    """

    global _ICON_REGEXP
    # Build icon regexp once
    if _ICON_REGEXP is None:
        # Sort icon by length to make sure multi-character icon are
        # matched first
        icon = sorted(icons_str.icons_text.values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in icon) + u')'
        _ICON_REGEXP = re.compile(pattern)

    if pr:
        pss(_ICON_REGEXP, pr=True)
    else:
        return _ICON_REGEXP

def icon_count(string, pr=False):
   """Returns the count of emojis in a string"""
   c = 0
   for i in string:
     if i in icons_str.icons_text:
          c = c+1
   if pr:
      pss(c, pr=True)
   else:
      return c

def icon_list(string, pr=False):
    """Return the location and icon in list of dic format
    >>>pstr.icon_list("Hi, I am Python. ")
    >>>[{'location': 17, 'icon_count': 1, icon: ''}]
    """
    _entities = []
    for pos, c in enumerate(string):
        if c in unicode_codes.UNICODE_EMOJI:
            _entities.append({
                "location":pos,
                "icon": c,
                "icon_count": icon_count(string)
                })
    if pr:
        pss(_entities, pr=True)
    else:
        return _entities

def dicon(string, pr=False):
    
    """Replace unicode icon in a string with icon shortcodes. Useful for storage.
    :param string: String contains unicode characters. MUST BE UNICODE.
    :param pr: if False will return string
        >>> import pstr
        >>> print(pstr.icon("Python is fun <@python>"))
        Python is fun 
        >>> print(pstr.dicon(u"Python is fun "))
        Python is fun <@python>
        >>> print(pstr.dicon(u"Unicode is tricky "))
        Unicode is tricky <@python>
    """

    def replace(match):
        codes_dict = icons_str.icons_text
        val = codes_dict.get(match.group(0), match.group(0))
        icon_val = "<@" + val[1:-1] + ">"
        return icon_val
    if pr:
        pss(re.sub(u'\ufe0f', '', (get_icon_regexp().sub(replace, string))), pr=True)
    else:
        return re.sub(u'\ufe0f', '', (get_icon_regexp().sub(replace, string)))

######################## -- this code for array output -- #################################

# figlet ...
def figlet(text, font='standard', color=':', **kwargs):
    """
    @NOTE: these all fonts in pyfiglet

    #  1943____       chunky        fbr12___     letterw3            rev           ticks
    #  3-d            clb6x10       fbr1____     letter_w           'ripper!_'     ticksslant
    #  3x5            clb8x10       fbr2____     lexible_            road_rai      tiles
    #  4x4_offr       clb8x8        fbr_stri     linux               rockbox_      times
    #  5lineoblique   cli8x8        fbr_tilt     lockergnome         rok_____      timesofl
    #  5x7            clr4x6        fender       lower.flc               roman         tinker-toy
    #  5x8            clr5x10       finalass     mad_nurs            roman___      ti_pan__
    #  64f1____       clr5x6        fireing_     madrid              rot13.flc         t__of_ap
    #  6x10           clr5x8        flyn_sh      magic_ma            rot13         tomahawk
    #  6x9            clr6x10       fourtops     marquee             rounded       tombstone
    #  acrobatic      clr6x6        fp1_____     master_o            rowancap      top_duck
    #  advenger       clr6x8        fp2_____     maxfour             rozzo         trashman
    #  alligator2     clr7x10       fraktur      mayhem_d            runic         trek
    #  alligator      clr7x8        funky_dr     mcg_____            runyc         triad_st
    #  alphabet       clr8x10       future_1     mig_ally            sansb         ts1_____
    #  aquaplan       clr8x8        future_2     mike                sansbi        tsalagi
    #  arrows         coil_cop      future_3     mini                sans          tsm_____
    #  asc_____       coinstak      future_4     mirror              sansi         tsn_base
    #  ascii___       colossal      future_5     mnemonic            sblood        ttyb
    #  assalt_m       computer      future_6     modern__            sbookb        tty
    #  asslt__m       com_sen_      future_7     morse               sbookbi       tubular
    #  atc_____       contessa      future_8     moscow              sbook         twin_cob
    #  atc_gran       contrast      fuzzy        mshebrew210         sbooki        twopoint
    #  avatar         convoy__      gauntlet     nancyj-fancy        script        type_set
    #  a_zooloo       cosmic        ghost_bo     nancyj              script__      ucf_fan_
    #  banner3-D      cosmike       goofy        nancyj-underlined   serifcap      ugalympi
    #  banner3        courb         gothic       new_asci            shadow        unarmed_
    #  banner4        courbi        gothic__     nfi1____            shimrod       univers
    #  banner         cour          graceful     nipples             short         upper.flc
    #  barbwire       couri         gradient     notie_ca            skateord      usaflag
    #  basic          crawford      graffiti     npn_____            skateroc      usa_____
    #  battle_s       cricket       grand_pr     ntgreek             skate_ro      usa_pq__
    #  battlesh       cursive       greek        null.flc                sketch_s      utopiab
    #  baz__bil       cyberlarge    green_be     nvscript            slant         utopiabi
    #  beer_pub       cybermedium   hades___     o8                  slide         utopia
    #  bell           cybersmall    heavy_me     octal               slscript      utopiai
    #  bigchief       dcs_bfmo      helvb        odel_lak            small         vortron_
    #  big            d_dragon      helvbi       ogre                sm______      war_of_w
    #  binary         decimal       helv         ok_beer_            smisome1      wavy
    #  block          deep_str      helvi        os2                 smkeyboard    weird
    #  b_m__200       defleppard    heroboti     outrun__            smscript      whimsy
    #  briteb         demo_1__      hex          pacos_pe            smshadow      xbriteb
    #  britebi        demo_2__      high_noo     panther_            smslant       xbritebi
    #  brite          demo_m__      hills___     pawn_ins            smtengwar     xbrite
    #  britei         devilish      hollywood    pawp                space_op      xbritei
    #  broadway       diamond       home_pak     peaks               spc_demo      xchartr
    #  bubble_b       digital       house_of     pebbles             speed         xchartri
    #  bubble         doh           hypa_bal     pepper              stacey        xcourb
    #  bubble__       doom          hyper___     phonix__            stampatello   xcourbi
    #  bulbhead       dotmatrix     inc_raw_     platoon2            standard      xcour
    #  c1______       double         platoon_    star_war            xcouri
    #  c2______       drpepper      invita       pod_____            starwars      xhelvb
    #  calgphy2       druid___      isometric1   poison              stealth_      xhelvbi
    #  caligraphy     dwhistled     isometric2   p_s_h_m_            stellar       xhelv
    #  c_ascii_       ebbs_1__      isometric3   p_skateb            stencil1      xhelvi
    #  catwalk        ebbs_2__      isometric4   puffy               stencil2      xsansb
    #  caus_in_       eca_____      italic       __pycache__          stop         xsansbi
    #  c_consen       e__fist_      italics_     pyramid             straight      xsans
    #  char1___       eftichess     ivrit        r2-d2___            street_s      xsansi
    #  char2___       eftifont      jazmine      rad_____            subteran      xsbookb
    #  char3___       eftipiti      jerusalem    radical_            super_te      xsbookbi
    #  char4___       eftirobot     joust___     rad_phan            tanja         xsbook
    #  charact1       eftitalic     katakana     rainbow_            tav1____      xsbooki
    #  charact2       eftiwall      kban         rally_s2            taxi____      xtimes
    #  charact3       eftiwater     kgames_i     rally_sp            tec1____      xttyb
    #  charact4       epic          kik_star     rampage_            tec_7000      xtty
    #  charact5       etcrvs__      krak_out     rastan__            tecrvs__      yie-ar__
    #  charact6       f15_____      larry3d      raw_recu            tengwar       yie_ar_k
    #  characte       faces_of      lazy_jon     rci_____            term          zig_zag_
    #  charset_       fairligh      lcd          rectangles          thick         zone7___
    #  chartr         fair_mea      lean         relief2             thin          z-pilot_
    #  chartri        fantasy_      letters      relief              threepoint
    """
    from pyfiglet import print_figlet
    if color.islower():
        color = color.upper()
    print_figlet(text, font, color, **kwargs)

        # text = os.popen('figlet "%s"'%text).read()
        # _text = ''
        # for i in text.split('\n')[0:-2]:
        #     _text += i+'\n'
        # return _text[0:-1]

# toilet ...
def toilet(text, pr=False):
        text = os.popen('toilet -f mono12 "%s"'%text).read()
        _text = ''
        for i in text.split('\n')[2:-3]:
            _text += i+'\n'

        if pr:
            pss(_text[0:-1], pr=True)
        else:
            return _text[0:-1]

# Change text location ...
def postion(text, top=0, right=0, down=0, pr=False):
        """
    text postion in cli

    :param text  = string
    :param top   = int
    :param right = int
    :param down  = int
    :param pr    = print or return if False
        """
        style = ''
        text = text.split('\n')
        # spaces top
        style = style + ('\n'*top)
        # spaces right
        for i in text:
            style = style + (' ' * right) + i + '\n'
        # spaces down
        style = style + '\n'*(down)
        if pr:
            pss(style[0:], pr=True, End='')
        else:
            return style[0:]

# to write text by line(Index) as slow motion
def slowIndex(text, pr=False, t=0.01):
        for i in range(0,len(text)):
            sleep(t)
        if pr:
            pss(text[i], End='', pr=True)
        else:
            return text[1]
        print('')

# to write text by Line as slow motion
def slowLine(text, pr=False, t=0.5):
        for i in text.split('\n'):
            sleep(t)
            if pr:
                pss(i, pr=True)
            else:
                return

def hrLoad(text, ln=10, CLT='g', 
          CUT='w', repeat=2, t=0.1, 
          start=1, title='', end=1):
    """
    # hr    : '-'
    # hr2   : '·'
    # hr3   : '_'
    # hr4   : '─'
    # hr5   : '+'
    """
    text = text*ln
    text = ' '*start +text+ ' '*end
    space = 0
    pss(f"<!w>{title}<!{CLT}>{text}", End='\r', pr=True)
    # pss(f"{CLT}{text}<!e>", End='\r', pr=True)
    for i in range(repeat):#
        for i in range(0, len(text)):
            pss(f"<!{CLT}>{text[:i]}<!e>{' '*space}<!{CUT}>{text[i]}<!e>", End='\r', pr=True)                
            sleep(t)

# python for ever...-
def everStr(text, CLT='g', CUT="w", t=0.3, repeat=2, 
          ever='lower', space=0, title='', right=1,
          alias_color=True, Type='', start=1, end=1):#text='C#tB#eG#xP#t',
        
        clt = f'<{CLT}>'
        cut = f'<{CUT}>'
        text=' '*start +text+' '*end
        # text = Color.reader(str(text))
        # text = pss(text)
        if ever in ("upper", 'u', 'up'):
            text = text.upper()
        elif ever in ("lower", 'l', 'lo'):
            text = text.lower()
        pss(f"<!w>{title}{' '*right}<!{CLT.split()[0]}>{text}", End='\r', pr=True)
    
        for i in range(repeat):#
            for i in range(0, len(text)):
                if alias_color:
                    clt = f'<!{CLT}>'
                    cut = f'<!{CUT}>'
                if ever in ("lower", 'l', 'lo'):
                    # from lower to upper
                    if Type in ("cap", "upper"):
                        pss(f"{title}{' '*right}{clt}{text[:i].lower()}<!e>{' '*space}{cut}{text[i:].upper()}<!e>", End='\r', pr=True)                
                    
                    pss(f"{title}{' '*right}{clt}{text[:i].lower()}<!e>{' '*space}{cut}{text[i].upper()}<!e>", End='\r', pr=True)
                elif ever in ("upper", 'u', 'up'):
                    # from uppder to lower
                    text = text.upper()
                    pss(f"{title}{' '*right}{clt}{text[:i].upper()}<!e>{' '*space}{cut}{text[i].lower()}<!e>", End='\r', pr=True)                                    
                sleep(t)
        print('')


# Loading animation...
def Loading(AT=['|','/','-','\\'], text='text...', t=0.2, repeat=10):

        """
        '', ''
        """
        AT_2 = ['', '']
        text = pss(text)
        W = pss()
        for i in range(repeat):
            for i in range(0, len(AT)):
                ASA = pss(AT[i])
                pss('<!w>' + text + ASA, End='\r', pr=True)
                sleep(t)
        print('')

# Downloading animation...
# Animation should be list
def prog_bar(text='<!r>Loading', t=0.2, width=25, AT=['<!bu>│','<!g>█','<!c>▒','<!bu>│']):
        text = pss(str(text))
        AT = [pss(i) for i in AT]
        y = width+1
        for i in range(width+1):
            pss('\r' + "<!w>" + text +AT[3] + (i*AT[1]) + (AT[2]*(y-1)) +AT[3] + ' ', End='', pr=True)
            sleep(t)
            y -= 1
        print('')

def box(text, color='e', top=0, 
          right=0, down=0, at_type='br', 
          horizontal=True, vertical=False, 
          at=["┌","│","└","─","┘","┐"]):
        
    # b = '\b'
    # pattern = re.compile(u'(<![a-zA-Z0-9\\+\\-_&.ô’Åéãíç()!#*]+>)')
    # matches = pattern.finditer(text)
    # for matche in matches:
    #     fin = text.find(matche.group(0))
    #     # print(fin)
    #     print(matche.group(0))
        # print(matche.group(1))
        # color = int(len(matche.group(0)))
    # text = text.replace(matche.group(0), f"{at[0]}{at[3]*int(len(text))}{b*len(matche.group(0))}{at[5]}")

    """
    @ box for text:
    :param: str : text       = string
    :param: bool: pr         = print or return 
    :param: int : top        = top space box
    :param: int : right      = right space in box
    :param: int : down       = down space in box
    :param: bool: horizontal = horizontal type for box
    :param: bool: vertical   = vertical type for box
    @ example:
    >> import pstr
    >> pstr.box("This Python Language", pr=True)
    ┌────────────────────┐
    │This Python Language│    
    └────────────────────┘

    @ You can add any color, emoje, icon and background color:
    >> import pstr
    >> pstr.box("<!r>This <!y>Python <!g>Language<!e>", pr=True)

    @ don't use color in vertical type
    >> import pstr
    >> pstr.box("<!r>This <!y>Python <!g>Language<!e>", pr=True, at=["<!c>┌","<!g>│<!e>","<!c>└","<!m>─","<!c>┘","<!c>┐"])
    """
    nl = f"{at[1]}{' '*len(text)}{at[1]}\n"
    nd = f"\n{at[1]}{' '*len(text)}{at[1]}"

    if at_type in ("BOLD", "bold", "Bold", 'bo'):
        at=['╔','║','╚','═','╝','╗']
    elif at_type in ("bright", "Light", "BRIGHT", 'br'):
        at=["┌", "│", "└", "─", "┘", "┐"]
    elif at_type in ("color"):
        at=["<!c>┌", f"<!g>│<!{color}>", "<!c>└", "<!m>─", "<!c>┘", "<!c>┐"]

    ## vertical line
    if vertical:
        text = f"{' '*top}{text}{' '*down}"
        pss(f"{at[0]}{at[3]*right+at[3]}{at[5]}", pr=True)
        for i in text:
            # print(f"{at[0]}{at[3]*len(text)}{at[5]}", end='')
            pss(f"{at[1]}{' '*right}{i}{at[1]}", pr=True)
        pss(f"{at[2]}{at[3]*right+at[3]}{at[4]}", pr=True)
        
    ## horizontal
    elif horizontal:
        text = f"{' '*right}{text}"
        pss(f"{at[0]}{at[3]*int(len(text))}{at[5]}", pr=True)

        pss(f"""\
{nl*top}\
{at[1]}{text}{at[1]}\
{nd*down}\
    """, pr=True)
        # {' '*right}
        pss(f"{at[2]}{at[3]*int(len(text))}{at[4]}", pr=True)
