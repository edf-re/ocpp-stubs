from distutils.core import setup


setup(
    name="typedpkg_stubs",
    url="ethanhs.me",
    author="Ethan Smith",
    author_email="ethan@ethanhs.me",
    version="0.1",
    package_data={"typedpkg_stubs": ['py.typed',
                                     'sample.pyi',
                                     '__init__.pyi']},
    packages=["typedpkg_stubs"]
)