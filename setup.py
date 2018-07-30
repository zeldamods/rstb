import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rstb",
    version="1.0.0-1",
    author="leoetlino",
    author_email="leo@leolam.fr",
    description="Breath of the Wild RSTB parser and editing tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leoetlino/rstb",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires='>=3.6',
    install_requires=['wszst_yaz0~=1.0'],
    entry_points = {
        'console_scripts': [
            'rstbtool = rstb.__main__:main',
        ]
    },
)
