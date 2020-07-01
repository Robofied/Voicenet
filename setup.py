import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="Voicenet",
    version="0.1.0",
    author="Akshat Gupta, Ridhima Garg, Laxman Singh Tomar",
    description="Voicenet is a comprehensive library for gender recognition from voice.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="voice gender classification gaussian mixture model gmm machine learning deep learning python",
    license="BSD-3",
    url="https://github.com/Robofied/Voicenet",
    download_url = "https://github.com/Robofied/Voicenet/archive/v1.0.zip",
    packages=find_packages(),
    install_requires=read("requirements.txt").split()

)


# from setuptools import find_packages, setup

# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Voicenet is a comprehensive library',
#     author='Akshat Gupta, Ridhima Garg',
#     license='BSD-3',
# )
