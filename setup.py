from setuptools import setup, find_packages

name = "zc.recipe.filestorage"
setup(
    name=name,
    version="1.0a6",
    author="Jim Fulton",
    author_email="jim@zope.com",
    description="ZC Buildout recipe for defining a file-storage",
    long_description=open("README.txt").read(),
    license="ZPL 2.1",
    keywords=["zodb", "zc.buildout"],
    url="http://pypi.python.org/pypi/%s/" % name,
    classifiers=[
        #"Development Status :: 5 - Production/Stable",
        "Framework :: ZODB",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    packages=find_packages(),
    include_package_data=True,
    data_files=[(".", ["README.txt"])],
    namespace_packages=["zc", "zc.recipe"],
    install_requires=["zc.buildout", "zope.testing", "setuptools"],
    entry_points={"zc.buildout": ["default=%s:Recipe" % name]},
    zip_safe=True,
    )
