import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomless",
    version="0.0.6",
    author="Artem Pavlov",
    description="A True Random Number Generator for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/artempavlov/randomless",
    #packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    #py_modules=['randomless'],
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
    install_requires=[
        'opencv-python==4.4.0',
        'numpy==1.19.1',
    ],
    #package_dir={'': 'randomless'},
)