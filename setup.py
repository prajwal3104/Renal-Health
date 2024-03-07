import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "Renal-Health"
AUTHOR = "prajwal3104"
SRC_REPO = "renalClassifier"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)