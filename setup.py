from setuptools import setup, find_packages

setup(
    name="gitstat",
    version="1.0.0",
    description="A CLI tool that generates beautiful GitHub repo analytics reports",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="roohan-514",
    author_email="roohan.rizvi@gmail.com",
    url="https://github.com/roohan-514/open-source-contributions",
    packages=find_packages(),
    package_data={"gitstat": ["templates/report.html"]},
    include_package_data=True,
    install_requires=["requests>=2.25.0"],
    entry_points={
        "console_scripts": [
            "gitstat=gitstat.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
)
