"""Build optional cython modules."""

import contextlib
import os
from distutils.command.build_ext import build_ext
from typing import Any


class BuildExt(build_ext):
    """Build extension modules."""

    def build_extensions(self) -> None:
        """Build the extension modules."""
        with contextlib.suppress(Exception):
            super().build_extensions()


def build(setup_kwargs: Any) -> None:
    """Build the extension modules."""
    if os.environ.get("SKIP_CYTHON", False):
        return
    try:
        from Cython.Build import cythonize

        setup_kwargs.update(
            {
                "ext_modules": cythonize(
                    [
                        "src/convertertools/impl.py",
                    ],
                    compiler_directives={"language_level": "3"},  # Python 3
                ),
                "cmdclass": {"build_ext": BuildExt},
            }
        )
        setup_kwargs["exclude_package_data"] = {
            pkg: ["*.c"] for pkg in setup_kwargs["packages"]
        }
    except Exception:
        if os.environ.get("REQUIRE_CYTHON"):
            raise
        pass
