# module name can't be named with postfix"-01"
import module1_05 as mod1
print(mod1.add(3,4))
print(mod1.sub(10,4))

from module1_05 import add,sub
print(add(5,10))
print(__name__) # in main process, __name__ return __main__


#import module from another directory..1
import sys
# in path, use / or \. But sometimes '\\' should be used
sys.path.append("C:/SamsungU/JumpToPython/Modules05")

#import module from another directory..2
'''
from cmd, PYTHONPATH = C:\SamsungU\JumpToPython\Modules05
python
>>> import module2_05
'''

import module2_05 as mod2
a = mod2.Math()
print("{0}, PI:{1}, solv:{2}".format(mod2.add(1,1), mod2.PI, a.solv(2)))
#There is no mod2.Math.PI