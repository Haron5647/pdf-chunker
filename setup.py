from setuptools import setup, find_packages

setup(
    name="pdf-chunker",
    version="0.1.0",
    description="CLI tool for processing PDF documents into JSONL chunks",
    author="Charounik",

    packages=find_packages(),

    install_requires=[
        "click==8.1.7",
        "PyMuPDF==1.27.2.2",
        "langchain-text-splitters==1.1.1",
    ],

    entry_points={
        "console_scripts": [
            "pdf-chunker=src.main:main"
        ]
    },

    python_requires=">=3.10",
)