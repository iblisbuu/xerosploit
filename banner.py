#!/usr/bin/python
# -*- coding: utf-8 -*-
# Xerosploit banners


#---------------------------------------------------------------------------#
# This file is part of Xerosploit.                                          #
# Xerosploit is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# Xerosploit is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with Xerosploit.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2016 LionSec (www.lionsec.net)                         #
#                                                                           #
#---------------------------------------------------------------------------#


import random

header1 = """  

  _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ 
( M | B | T | E | C | H )
 \_/ \_/ \_/ \_/ \_/ \_/ 
"""

header2 = """

  _   _   _   _   _   _  
/ \ / \ / \ / \ / \ / \ 
( M | B | T | E | C | H )
 \_/ \_/ \_/ \_/ \_/ \_/                                                     
"""

header3 = """

  _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ 
( M | B | T | E | C | H )
 \_/ \_/ \_/ \_/ \_/ \_/ 
 """

header4 = """
____  __                     \033[1;36m________         ______       _____ _____ \033[1;m
__  |/ /_____ ______________ \033[1;36m__  ___/________ ___  /______ ___(_)__  /_\033[1;m
__    / _  _ \__  ___/_  __ \\\033[1;36m_____ \ ___  __ \__  / _  __ \__  / _  __/\033[1;m
_    |  /  __/_  /    / /_/ /\033[1;36m____/ / __  /_/ /_  /  / /_/ /_  /  / /_  \033[1;m
/_/|_|  \___/ /_/     \____/ \033[1;36m/____/  _  .___/ /_/   \____/ /_/   \__/  \033[1;m
                             \033[1;36m        /_/                               \033[1;m     
"""

def xe_header():
    headers = [header1, header2, header3, header4]
    return random.choice(headers)
