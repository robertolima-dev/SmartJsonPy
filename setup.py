from setuptools import find_packages, setup

setup(
    name="SmartJsonPy",
    version="0.1.0",
    description="📦 Funções inteligentes para manipulação e validação de JSON em Python",
    author="Roberto Lima",
    author_email="robertolima.izphera@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    keywords=["json", "validador", "limpeza", "parser", "conversão", "utils", "python"],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    project_urls={
        "Homepage": "https://github.com/robertolima-dev/SmartJsonPy", # noqa501
        "Repository": "https://github.com/robertolima-dev/SmartJsonPy", # noqa501
        "Issues": "https://github.com/robertolima-dev/SmartJsonPy/issues", # noqa501
    },
)
