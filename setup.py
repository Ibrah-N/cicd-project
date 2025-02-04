from setuptools import setup, find_packages



with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "cicd-project"
AUTHOR_NAME = "Ibrah-N"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "ibrahimibraheducation@gmail.com"

__version__ = "0.0.1"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
