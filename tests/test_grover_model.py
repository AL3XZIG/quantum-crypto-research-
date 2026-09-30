from experiments.grover.grover_model import classical_work, grover_work


def test_grover_scaling():
    n = 2**20
    assert classical_work(n) == n
    assert grover_work(n) == 2**10


def test_grover_is_quadratic_speedup():
    n = 2**32
    assert classical_work(n) / grover_work(n) == 2**16
