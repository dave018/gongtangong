#from Package05_3.sound.echo import echo_test
from ..sound.echo import echo_test #relative import
def render_test():
    print("render")
    echo_test()