#convert all px values to rem or other values

import re
css = """ """
def test(a):
    b=float(a[1])*0.062 #multiplies 0.062 by value in group 1
    return str(b)+'rem'


myRe=re.compile(r'(\d{0,4})(px)')
sub=myRe.sub(test, css)
print(sub)

#convert all rem values to px or other values

import re
css = """ """
def test(a):
    b=float(a[1])/0.062 #divides 0.062 by value in group 1
    return str(b)+'px'


myRe=re.compile(r'(\d{0,4})(px)')
sub=myRe.sub(test, css)
print(sub)

#introduce 'logical properties'
def test(a):
    if a.group(0) == '-left:':
        return '-inline-start:'
    if a.group(0) == '-right:':
        return '-inline-end:'
    if a.group(0) == '-top:':
        return '-block-start:'
    if a.group(0) == '-bottom:':
        return '-block-end:'
    if a.group(0) == ' top:':
        return 'inset-block-start:'
    if a.group(0) == ' bottom:':
        return 'inset-block-end:'
        
     


myRe=re.compile(r'-left:|-right:|-bottom:|-top:|\stop:|\sbottom:')
sub=myRe.sub(test, css)
#sub = myRe.findall(css)
print(sub)
    


    
    
    
    
