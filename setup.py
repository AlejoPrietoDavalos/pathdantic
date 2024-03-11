from pathlib import Path
import setuptools

_NAME = "pathdantic"
_VERSION = "0.0.2"
_AUTHOR = "Alejo Prieto Dávalos"
_README = "README.md"
_REQUIREMENTS = "requirements.txt"
_URL_PYPI = "https://pypi.org/project/pathdantic"
_AUTHOR_EMAIL = "alejoprietodavalos@gmail.com"
_URL_SOURCE = "https://github.com/AlejoPrietoDavalos/pathdantic/"
_PYTHON_REQUIRES = ">=3.10,<3.12"

setuptools.setup(
    name = _NAME,
    version = _VERSION,
    author = _AUTHOR,
    long_description = Path(_README).read_text(),
    long_description_content_type = "text/markdown",
    url = _URL_PYPI,
    author_email = _AUTHOR_EMAIL,
    project_urls = {
        "Source": _URL_SOURCE
    },
    python_requires = _PYTHON_REQUIRES,
    install_requires = Path(_REQUIREMENTS).read_text().strip().split("\n"),
    packages = setuptools.find_packages(),
    include_package_data = True
)