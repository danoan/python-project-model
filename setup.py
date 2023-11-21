from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        [
            Extension(name="danoan.toml_dataclass",
                      sources=["src/danoan/toml_dataclass.pyx"]
                      )
        ]
    )
)
