# var 52
# y = f(x) для x<=0 : -(cos(x))^2
# y = f(x) для x>=0 : (cos(x))^2 - 2
# x_min : -pi/2
# x_max : +pi/2
# x0 ^ a : x6

from functools import wraps
from matplotlib import pyplot as plt
import numpy as np
from math import cos, pi, sin, sqrt
from scipy import cbrt

# constants
x_min = -pi/2
x_max = pi/2
# plt.style.use('dark_background')
plt.style.use('seaborn')
# plt.style.use('grayscale')

def plot(path):
	def dec(func):
		@wraps(func)
		def savefig(xx, name, *args):
			fig = plt.figure(name)
			sub = plt.subplot()
			sub.set_xlabel('x-axis')
			sub.set_ylabel('y-axis')
			sub.set_title(name)
			if len(args) > 0:
				xx, yy, xmp, ymp = func(xx, name, *args)
				x_negative = list(filter(lambda x: x < 0, xx))
				x_positive = list(filter(lambda x: x > 0, xx))
				sub.plot(x_negative, yy[:len(x_negative)], zorder=1)
				sub.plot(x_positive, yy[-len(x_positive):], zorder=1)
				sub.scatter(xmp, ymp, marker='x', color='crimson', zorder=2)
			else:
				yy = func(xx, name, *args)
				sub.plot(xx, yy, zorder=1)
				e_x, e_y = [xx[0], xx[-1]], [yy[0], yy[-1]] # межі
				sub.scatter(e_x, e_y, marker='o', color='crimson', zorder=2)
			fig.add_subplot(sub)
			# path = './img/' + name + '.svg'
			fpath = './img/' + path + '.png'
			plt.savefig(fpath, format='png', dpi=400)
			return fig
		return savefig
	return dec

@plot('func')
def f(xx, name):
	yy = []
	for x in xx:
		if x < 0:
			yy.append(-(cos(x))**2)
		elif x > 0:
			yy.append((cos(x))**2 - 2)
		else:
			yy.append(-2)
	return yy

xx = np.linspace(x_min, x_max, 2000)

# 2
@plot('second derivative')
def d2y(xx, name, *args):
	""" 
	dy2/dx2 (second derivative)
	f''(x) = 2*cos(2x)\n
	f''(x) = -2*cos(2x)\n
	"""
	yy = []
	for x in xx:
		if x < 0:
			yy.append(2*cos(2*x))
		elif x > 0:
			yy.append(-2*cos(2*x))
		else: yy.append(0)
	return xx, yy, 0, 0

#3
@plot('abs second derivative')
def d2y_abs(xx, name):
	return list([abs(2*cos(2*x)) for x in xx])

# f(xx, 'f(x)')
# d2y(xx, 'Графік другої похідної d^2y/dx^2', 'sder')
# d2y_abs(xx, 'Графік модулю другої похідної |d^2y/dx^2|')

# 4
# (-pi/2, -pi/4), (0, pi/4) ф-я опукла (f''(x)<0)
# (-pi/4, 0), (pi/4, pi/2) ф-я вгнута (f''(x)>0)
# -pi/4, pi/4, 0 - точки перегину
# 0 - точка розриву першого роду lim2 = 2, lim-2 = -2 -> 2 != -2, 2 != -1

@plot('ilya f(x)')
def iif(xx, name):
	yy = []
	for x in xx:
		if x > 0:
			try:
				yy.append(sqrt(cos(x)) - 2)
			except ValueError:
				yy.append(3)
		elif x < 0:
			try:
				yy.append(-sqrt(cos(x)))
			except ValueError:
				yy.append(3)
		else:
			yy.append(-1)
	return yy

@plot('ilya sder')
def isder(xx, name, *args):
	yy, xc = [], []
	xmp, ymp = 0, 0
	for x in xx:
		if x > 0:
			try:
				yy.append(-sqrt(cos(x))/2.0 - sin(x)**2/4/cos(x)**(3/2.0))
				xc.append(x)
			except ValueError: pass
		elif x < 0:
			try:
				yy.append((cos(2*x) + 3)/8/cos(x)**(3/2.0))
				xc.append(x)
			except ValueError: pass
		else:
			pass
	return xc, yy, xmp, ymp

@plot('ilya abs sder')
def iabsder(xx, name, *args):
	yy, xc = [], []
	xmp, ymp = 0, 0
	for x in xx:
		if x > 0:
			try:
				yy.append(abs(-sqrt(cos(x))/2.0 - sin(x)**2/4/cos(x)**(3/2.0)))
				xc.append(x)
			except ValueError: pass
		elif x < 0:
			try:
				yy.append(abs((cos(2*x) + 3)/8/cos(x)**(3/2.0)))
				xc.append(x)
			except ValueError: pass
		else:
			pass
	return xc, yy, xmp, ymp

xi = np.linspace(-pi/2, pi/2, 2000)
xid = np.linspace(-1.5, 1.5, 2000)
yy = iif(xi, 'f(x)')
isder(xid, 'd2y/dx2', 'sder')
iabsder(xid, '|d2y/dx2|', 'abs')