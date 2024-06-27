import pytest

from convertertools.impl import (
    del_dict_set,
    del_dict_tuple,
    pop_dict_set,
    pop_dict_tuple,
)


def test_del_dict_tuple():
    d = {"a": 1, "b": 2, "c": 3}
    del_dict_tuple(d, ("a", "b"))
    assert d == {"c": 3}


def test_pop_dict_tuple():
    d = {"a": 1, "b": 2, "c": 3}
    pop_dict_tuple(d, ("a", "b"))
    assert d == {"c": 3}


def test_del_dict_set():
    d = {"a": 1, "b": 2, "c": 3}
    del_dict_set(d, {"a", "b"})
    assert d == {"c": 3}


def test_pop_dict_set():
    d = {"a": 1, "b": 2, "c": 3}
    pop_dict_set(d, {"a", "b"})
    assert d == {"c": 3}


def test_del_dict_tuple_missing_key():
    d = {"a": 1, "b": 2, "c": 3}
    with pytest.raises(KeyError):
        del_dict_tuple(d, ("a", "b", "d"))
    assert d == {"c": 3}


def test_pop_dict_tuple_missing_key():
    d = {"a": 1, "b": 2, "c": 3}
    pop_dict_tuple(d, ("a", "b", "d"))
    assert d == {"c": 3}


def test_del_dict_set_missing_key():
    d = {"a": 1, "b": 2, "c": 3}
    with pytest.raises(KeyError):
        del_dict_set(d, {"a", "b", "d"})


def test_pop_dict_set_missing_key():
    d = {"a": 1, "b": 2, "c": 3}
    pop_dict_set(d, {"a", "b", "d"})
    assert d == {"c": 3}
