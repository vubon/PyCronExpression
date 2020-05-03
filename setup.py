import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyCronExpression-vubon",  # Replace with your own username
    version="0.0.1",
    author="Vubon Roy",
    author_email="vubon.roy@gmail.com",
    description="A simple Python Cron Expression lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vubon/PyCronExpression.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
