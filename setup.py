from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chicken-disease-classification"
AUTHOR = "Wilsven"
SRC_REPO = "chicken_disease_classification"
AUTHOR_EMAIL = "wilsven_leong96@hotmail.co.uk"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A model for chicken diseases classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
