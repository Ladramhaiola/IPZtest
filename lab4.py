# x^3 - 2*x^2 + x + 1 = 0

f = lambda x: x**3 - 2*x**2 + x + 1
der = lambda x: 3*x**2 - 4*x + 1
sder = lambda x: 6*x - 4

newton = lambda b: b - f(b)/der(b)
sectant = lambda a, b: a - (f(a)*(b - a))/(f(b) - f(a))

def solve(a, b, eps):
	if f(b)*f(a) > 0: return 0, "edges have same signs", []
	k = 0; iter_values = []
	while abs(b - a) > eps:
		x = (b + a)/2.0
		if der(x)*sder(x) < 0:
			a, b = b, a
		a = sectant(a, b); b = newton(b)
		k += 1; iter_values.append((a + b)/2.0)
	x = (b + a)/2.0
	return x, k, iter_values

if __name__ == '__main__':
	a = -1
	b = 0.0001
	epsilon = 1
	res, k, iv = solve(a, b, 1.0e-34)
	print(res, k)
	print(f(res))
	print(iv)