"""impl.py."""

from __future__ import annotations

from typing import Any


def del_dict_tuple(d: dict[Any, Any], keys: tuple[Any, ...]) -> None:
    """Delete keys from a dictionary from a tuple."""
    for key in keys:
        del d[key]


def del_dict_set(d: dict[Any, Any], keys: set[Any]) -> None:
    """Delete keys from a dictionary from a set."""
    for key in keys:
        del d[key]


def pop_dict_tuple(d: dict[Any, Any], keys: tuple[Any, ...]) -> None:
    """Pop keys from a dictionary from a tuple if present."""
    for key in keys:
        if key in d:
            del d[key]


def pop_dict_set(d: dict[Any, Any], keys: set[Any]) -> None:
    """Pop keys from a dictionary from a set if present."""
    for key in keys:
        if key in d:
            del d[key]


def pop_dict_set_if_none(d: dict[Any, Any], keys: set[Any]) -> None:
    """Pop keys from a dictionary from a set if present and none."""
    for key in keys:
        if key in d and d[key] is None:
            del d[key]
