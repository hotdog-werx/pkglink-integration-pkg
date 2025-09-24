from .version import __version__
from pydantic import BaseModel

class InfoModel(BaseModel):
    name: str
    version: str

# pkglink_integration_pkg/main.py
def main():
    info = InfoModel(name="PKG Link Integration Package", version=__version__)
    print(info.json())
