# convertertools

<p align="center">
  <a href="https://github.com/bluetooth-devices/convertertools/actions/workflows/ci.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/bluetooth-devices/convertertools/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >
  </a>
  <a href="https://convertertools.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/convertertools.svg?logo=read-the-docs&logoColor=fff&style=flat-square" alt="Documentation Status">
  </a>
  <a href="https://codecov.io/gh/bluetooth-devices/convertertools">
    <img src="https://img.shields.io/codecov/c/github/bluetooth-devices/convertertools.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
</p>
<p align="center">
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
  <a href="https://github.com/pre-commit/pre-commit">
    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">
  </a>
</p>
<p align="center">
  <a href="https://pypi.org/project/convertertools/">
    <img src="https://img.shields.io/pypi/v/convertertools.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/pypi/pyversions/convertertools.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">
  <img src="https://img.shields.io/pypi/l/convertertools.svg?style=flat-square" alt="License">
</p>

---

**Documentation**: <a href="https://convertertools.readthedocs.io" target="_blank">https://convertertools.readthedocs.io </a>

**Source Code**: <a href="https://github.com/bluetooth-devices/convertertools" target="_blank">https://github.com/bluetooth-devices/convertertools </a>

---

Tools for converting python data types

These are very simple tools for manipulating python data structures
to avoid writing out the same code many times in libraries.

## Installation

Install this via pip (or your favourite package manager):

`pip install convertertools`

## Usage

Note that specific types are required for maximum performance.

```python
from convertertools import del_dict_tuple, del_dict_set, pop_dict_tuple, pop_dict_set

# del_dict* raise KeyError on missing keys
del_dict_tuple(d, ("a", "b"))
del_dict_set(d, {"a", "b"})

# pop_dict* ignores missing keys
pop_dict_tuple(d, ("a", "b"))
pop_dict_set(d, {"a", "b"})

# pop_dict_set_if_none ignores missing keys and only
# removes them if their value is None
pop_dict_set_if_none(d, {"a", "b"})
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- prettier-ignore-start -->
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.openhomefoundation.org/"><img src="https://avatars.githubusercontent.com/u/109550163?v=4?s=80" width="80px;" alt="Bluetooth Devices"/><br /><sub><b>Bluetooth Devices</b></sub></a><br /><a href="https://github.com/bluetooth-devices/convertertools/commits?author=Bluetooth-Devices" title="Code">💻</a> <a href="#ideas-Bluetooth-Devices" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bluetooth-devices/convertertools/commits?author=Bluetooth-Devices" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-end -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

This package was created with
[Copier](https://copier.readthedocs.io/) and the
[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)
project template.
