import setuptools

setuptools.setup(
    name="psutilz",
    version="0.9.0",
    packages=["psutilz"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=["psutil>=5.6.7"],
    author="Noah Levitt",
    author_email="nlevitt@gmail.com",
    description="pslisten, dstat",
    entry_points={
        "console_scripts": [
            "pslisten=psutilz.pslisten:main",
            "dstat=psutilz.dstat:main",
            "ps.py=psutilz.ps:main",
        ]
    },
)
