from setuptools import setup, find_packages

setup(
    name="mobilegraph-agent",
    version="0.1.0",
    description="Autonomous Mobile Refactoring, Design Modernization & Security Engine using AST Knowledge Graphs",
    author="Eren Şimşir",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mobilegraph=mobilegraph.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
    ],
)
