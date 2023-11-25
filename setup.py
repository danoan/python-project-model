from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        [
            Extension(name="danoan.quick_notes.api.to_markdown",
                      sources=["src/danoan/quick_notes/api/to_markdown.pyx"]
                      ),
            Extension(name="danoan.quick_notes.api.to_toml",
                      sources=["src/danoan/quick_notes/api/to_toml.pyx"]
                      ),
            Extension(name="danoan.quick_notes.api.model",
                      sources=["src/danoan/quick_notes/api/model.pyx"]
                      )
        ]
    )
)
