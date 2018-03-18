from matplotlib import pyplot as plt
from functools import wraps

def plot(name='default'):
    def dec(func):
        @wraps(func)
        def savefig(*args, **kwargs):
            plt.style.use('seaborn')
            fig = plt.figure(name)
            sub = plt.subplot()
            sub.set_xlabel('x-axis')
            sub.set_ylabel('y-axis')
            if name != 'default': sub.set_title(name) 
            sub.plot(*args, **kwargs)
            fig.add_subplot(sub)
            path = func(*args, **kwargs)
            plt.savefig(path)
        return savefig
    return dec

@plot('x^2')
def x_squared(xx, yy):
    return './img.png'

@plot('x*sin(x)')
def x_sin_x(xx, yy):
    return './xsinx.png'

@plot('x*sin(x) - 0.3*cos^2(x)')
def pot(xx, yy):
    return './pot.png'

from numpy import linspace as ls
xx = ls(0, 100, 400)
x_squared(xx, list(map(lambda x: x**2, xx)))

from math import sin, cos
x_sin_x(xx, list([x*sin(x) for x in xx]))

pot(xx, list([x*sin(x) - 0.3 * x * (cos(x))**2 for x in xx]))