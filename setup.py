import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="votifier2",
    version="0.1.0",
    author="ano95",
    author_email="adam@ano95.eu",
    description="Votifier protocol v2 client for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ano95/votifier2-py",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.6'
)
