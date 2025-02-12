import tabulate
import time


def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence W(n) = aW(n/b) + n"""
	if n == 1:
		return 1
	else:
		return a * simple_work_calc(n // b, a, b) + n


def work_calc(n, a, b, f):
	"""Compute the value of the recurrence W(n) = aW(n/b) + f(n)"""
	if n == 1:
		return f(1)
	else:
		return a * work_calc(n // b, a, b, f) + f(n)


def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence W(n) = max(W(n/b)) + f(n)"""
	if n == 1:
			return f(1)
	else:
			return max(span_calc(n // b, a, b, f) for _ in range(a)) + f(n)


def compare_work(*work_fns, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	result = []
	for n in sizes:
			row = [n] + [fn(n) for fn in work_fns if callable(fn)]
			result.append(tuple(row))
	return result

def print_results(results):
	"""Prints the comparison results."""
	headers = ['n'] + [f'W(f=func_{i+1})' for i in range(len(results[0]) - 1)]
	print(tabulate.tabulate(results,
													headers=headers,
													floatfmt=".3f",
													tablefmt="github"))

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""Compare the span values for given input sizes."""
	result = []
	for n in sizes:
			result.append((n, span_fn1(n), span_fn2(n)))
	return result