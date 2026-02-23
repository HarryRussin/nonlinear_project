import numpy as np
# Runge-Kutta 4th order method for solving ODEs

def RK4(x,y,f,h):
    
    k1 = f(x,y)
    k2 = f(x+h/2,y+h*k1/2)
    k3 = f(x+h/2,y+h*k2/2)
    k4 = f(x+h,y+h*k3)
    return y + h*(k1+2*k2+2*k3+k4)/6
