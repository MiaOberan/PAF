def deriv(funkc,x,h):
    return(funkc(x+h)-funkc(x-h))/(2*h)