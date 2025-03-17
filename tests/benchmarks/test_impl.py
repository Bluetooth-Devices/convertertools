from pytest_codspeed import BenchmarkFixture

from convertertools.impl import (
    pop_dict_set,
    pop_dict_set_if_none,
    pop_dict_tuple,
)


def test_pop_dict_set_if_none(benchmark: BenchmarkFixture) -> None:
    d = {"a": 1, "b": None, "c": 3}
    benchmark(pop_dict_set_if_none, d, {"a", "b", "d"})
    assert d == {"a": 1, "c": 3}


def test_pop_dict_tuple(benchmark: BenchmarkFixture) -> None:
    d = {"a": 1, "b": 2, "c": 3}
    benchmark(pop_dict_tuple, d, ("a", "b"))
    assert d == {"c": 3}


def test_pop_dict_set(benchmark: BenchmarkFixture) -> None:
    d = {"a": 1, "b": 2, "c": 3}
    benchmark(pop_dict_set, d, {"a", "b"})
    assert d == {"c": 3}


def test_pop_dict_tuple_missing_key(benchmark: BenchmarkFixture) -> None:
    d = {"a": 1, "b": 2, "c": 3}
    benchmark(pop_dict_tuple, d, ("a", "b", "d"))
    assert d == {"c": 3}


def test_pop_dict_set_missing_key(benchmark: BenchmarkFixture) -> None:
    d = {"a": 1, "b": 2, "c": 3}
    benchmark(pop_dict_set, d, {"a", "b", "d"})
    assert d == {"c": 3}
