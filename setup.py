import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="djangod",
    version="0.0.1",
    author="Yannick Hillion",
    author_email="yk.hillion@gmail.com",
    description="Django God packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yannickHillion/djangod",
    project_urls={
        "Bug Tracker": "https://github.com/yannickHillion/djangod/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Yannick Hillion",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)