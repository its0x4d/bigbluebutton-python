import setuptools

setuptools.setup(
    name="bigbluepy",
    version="0.1.8",
    author="UWSGI",
    url="https://github.com/its0x4d/bigbluepython-python",
    author_email="mosydev2016@gmail.com",
    description="An unofficial Bigbluebutton api.",
    packages=setuptools.find_packages(),
    platforms=['any'],
    license="MIT",
    install_requires=['packaging', 'xmltodict', 'requests'],
    long_description="An unofficial bigbluebutton api written in python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
