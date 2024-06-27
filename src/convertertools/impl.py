"""impl.py."""

from __future__ import annotations

from typing import Any


def delete_dict_keys_tuple(d: dict[Any, Any], keys: tuple[Any, ...]) -> None:
    """Delete keys from a dictionary from a tuple."""
    for key in keys:
        del d[key]


def delete_dict_keys_set(d: dict[Any, Any], keys: set[Any]) -> None:
    """Delete keys from a dictionary from a set."""
    for key in keys:
        del d[key]
