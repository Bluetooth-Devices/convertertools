from convertertools.impl import delete_dict_keys_set, delete_dict_keys_tuple


def test_delete_dict_keys_tuple():
    d = {"a": 1, "b": 2, "c": 3}
    delete_dict_keys_tuple(d, ("a", "b"))
    assert d == {"c": 3}


def test_delete_dict_keys_set():
    d = {"a": 1, "b": 2, "c": 3}
    delete_dict_keys_set(d, {"a", "b"})
    assert d == {"c": 3}
