'''
import Package05_3.sound.echo
Package05_3.sound.echo.echo_test()

from Package05_3.sound import echo
echo.echo_test()

from Package05_3.sound.echo import echo_test
echo_test()

import Package05_3
'''
#Package05_3.graphic.render.render_test() #AttributeError: module 'Package05_3' has no attribute 'graphic'
#import Package05_3 can reference only Package05_3/__init__.py

#import Package05_3.sound.echo.echo_test # end of import(without from) item should be package or module. not function

#from Package05_3.sound import *
#echo.echo_test() #without __init__.py __all__, NameError: name 'echo' is not defined

from Package05_3.graphic.render import render_test #main->render->echo chaining import
render_test()