import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        with open("CHANGELOG.md", "r") as changelog:
            return readme.read() + "\n\n" + changelog.read()


setuptools.setup(
    name="PyCronExpression",
    version="0.1.0",
    author="Vubon Roy",
    author_email="vubon.roy@gmail.com",
    description="A simple Python Cron Expression lib",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vubon/PyCronExpression.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'pytz',
        'tzlocal'
    ],
    python_requires='>=3.6',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
