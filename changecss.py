#convert all px values to rem or other values

import re

def test(a):
    b=float(a[1])*0.062 #multiplies 0.062 by value in group 1
    return str(b)+'rem'


myRe=re.compile(r'(\d{0,4})(px)')
sub=myRe.sub(test, css)
print(sub)

    


    
    
    
    
