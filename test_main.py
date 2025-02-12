from main import *


def test_simple_work():
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(16, 2, 2) == 80
	assert simple_work_calc(8, 3, 2) == 65
	assert simple_work_calc(4, 2, 2) == 12


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(16, 2, 2, lambda n: n) == 80
	assert work_calc(8, 3, 2, lambda n: n * n) == 175
	assert work_calc(4, 2, 2, lambda n: 1) == 7

def test_compare_work():
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: n**0.5)       # c < log_b(a)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n**1)         # c = log_b(a)
	work_fn3 = lambda n: work_calc(n, 2, 2, lambda n: n**2)         # c > log_b(a)

	sizes = [10, 20, 50, 100, 1000, 5000, 10000]
	res = compare_work(work_fn1, work_fn2, work_fn3, sizes)
	print_results(res)


def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: n)
	span_fn2 = lambda n: span_calc(n, 3, 2, lambda n: 1)
	res = compare_span(span_fn1, span_fn2)
	print_results(res)
