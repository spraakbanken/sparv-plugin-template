"""Install script for the uppercase example Sparv plugin."""

import setuptools

setuptools.setup(
    name="sparv-sbx-uppercase",
    version="0.1",
    description="Uppercase converter (example plug-in for Sparv)",
    license="MIT",
    author="",
    author_email="",
    packages=["sbx_uppercase"],
    python_requires=">=3.6",
    install_requires=["sparv-pipeline>=5.0.dev0,<6"],
    entry_points={"sparv.plugin": ["sbx_uppercase = sbx_uppercase"]}
)
