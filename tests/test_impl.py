from convertertools.impl import del_dict_set, del_dict_tuple


def test_del_dict_tuple():
    d = {"a": 1, "b": 2, "c": 3}
    del_dict_tuple(d, ("a", "b"))
    assert d == {"c": 3}


def test_del_dict_set():
    d = {"a": 1, "b": 2, "c": 3}
    del_dict_set(d, {"a", "b"})
    assert d == {"c": 3}
