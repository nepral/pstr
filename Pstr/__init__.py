# -*- coding: UTF-8 -*-

"""
    Usage:
        pss = pcolor.Pss
        pss(TEXT, pr=True)
            TEXT = str or any thing
        	and in str write like this 

        color/background:
            "<!y>Hello <!g>World <!m>!!<!e>"
            "<?y>Hello <?g>World <?m>!!<!e>"
            "<u><r> Hello <r><!g>World"

        emoje:
            "I,m fine <:thumbs_up:>" or
            "I,m fine :thumbs_up:"

        icons:
            "This is python icon <@python>"
            "This is python icon <ico>python</ico>"

        text:
            "This is sub text <sub>python</sub>"
            "This is sup text <sup>python</sup>"
            "This is hr line <hr>python</hr>"

    image about code :

        <!code> = for color
        <?code> = for background color
        <@code> = for print icon
        <u> 	= Underline
        <i>     = Italic
        <r>     = Reversed = select on text
        <s>     = Strike/strikethrough
        <l>     = lamb
        <h>     = hide
        <br>    = bright
        <bo>    = bold
                    
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
        - background = bg
        - color      = co

    example:
        <!y>   = yellow
        <!e>   = use this in end any color or background color
            
    emoje functions :
        emoji terminal output for Python.
        >>> import pstr
        >>> print(pstr.emojize('Python is :thumbsup:', aliase=True))
        Python is 👍
        >> print(pstr.emojize('Python is :thumbs_up:'))
        Python is 👍
        >> pstr.emojize("Python is :thumbs_up:", pr=True, aliase=True)
        Python is 👍

    try:
        help(pstr), or
        dir(pstr)
"""

from pstr.pstr import (
        ## main color
        pcolor, pss,

        ## text
        Write, sup, sub, hr, 
        url, figlet, toilet, 
        postion, slowIndex, 
        slowLine, everStr, box,

        ## reg 
        find, findCo,

        ## files
        file, rtext, config,

        ## prompt/print cli
        passwd, prss, inpss,

        ## emoje fucntions
        emojize, demojize, get_emoji_regexp, emoji_count, emoji_list,

        ## icon functions
        icon, get_icon_regexp, icon_count, icon_list, dicon,

        ## loading functions
        hrLoad, Loading, prog_bar,

        ## other functions
        show_all)

from pstr.text import (
    ## text functions
    black, red, green, yellow, blue, magenta,
    cyan, err, info, que, bad, good, run)

from pstr.icons_files.unicode_codes import (EMOJI_ALIAS_UNICODE,
    EMOJI_UNICODE,
    UNICODE_EMOJI,
    UNICODE_EMOJI_ALIAS)


__version__ = '1.0.3'
__author__ = 'Osama Muhammed AL-zabidi'
__email__ = 'osamanepral@gmail.com'
__source__ = 'https://github.com/nepral/pstr/'
__pip_install__ = 'pip3 install pstr'
__git_install__ = 'git clone https://github.com/nepral/pstr.git && cd pstr && python3 setup.py install'

__infoAboutAuthor__ = """
authorName    : Osama Mohammed Al-zabidi
authorEmail   : osamanepral@gmail.com
authorPhone   : +(967) 717448593
moduleVersion : 1.0.3
StringUnicode : utf-8
"""
__license__ = '''
New BSD License

Copyright (c) 2014-2015, Taehoon Kim and Kevin Wurster
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* The names of its contributors may not be used to endorse or promote products
  derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
