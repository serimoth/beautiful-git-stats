from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="git-stats-cli",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Beautiful Git repository statistics and insights in your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/git-stats",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "gitpython>=3.1.0",
        "rich>=13.0.0",
        "click>=8.0.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "git-stats=gitstats.cli:main",
        ],
    },
)
