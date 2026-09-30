from experiments.signatures.benchmark import measure_ms


def test_measure_ms_runs_callable():
    value = measure_ms(lambda: None, repetitions=3, warmup=1)
    assert value >= 0


def test_measure_ms_rejects_zero_repetitions():
    try:
        measure_ms(lambda: None, repetitions=0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
