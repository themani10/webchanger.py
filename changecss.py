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

def convert_rem_to_px(css_code):
    # Define the regex pattern
    pattern = r'(\d+(?:\.\d+)?rem)'
    
    # Function to convert rem to px
    def convert(match):
        rem_value = float(match.group()[:-3])  # Remove 'rem' and convert to float
        px_value = rem_value * 16
        return f"{px_value:.1f}px"
    
    # Use re.sub to replace all occurrences
    converted_code = re.sub(pattern, convert, css_code)
    
    return converted_code
print(convert_rem_to_px(css_code))

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
    


    
    
    
    
