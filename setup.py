"""Install script for the uppercase example Sparv plugin."""

import setuptools

setuptools.setup(
    name="sparv-uppercase",
    version="0.1",
    description="Uppercase converter (example plug-in for Sparv)",
    license="MIT",
    author="",
    author_email="",
    packages=["uppercase"],
    python_requires=">=3.6",
    install_requires=["sparv-pipeline>=4,<5"],
    entry_points={"sparv.plugin": ["uppercase = uppercase"]}
)
