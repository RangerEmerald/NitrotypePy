from setuptools import setup, find_namespace_packages

setup(
    name="NitrotypePy",
    version="0.0.3",
    description="A way to access nitrotype's unofficial api.",
    author="The Moon That Rises",
    url="https://www.github.com/RangerEmerald/NitrotypePy",
    license="MIT",
    packages=find_namespace_packages(include="NitrotypePy.*"),
    install_requires=[
        "cloudscraper >= 1.2.58",
    ],
)
