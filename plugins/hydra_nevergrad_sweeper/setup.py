# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="hydra_nevergrad_sweeper",
        version="0.1.0",
        author="Jeremy Rapin",
        author_email="jrapin@fb.com",
        description="Hydra Nevergrad Sweeper plugin",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/facebookresearch/hydra/",
        packages=find_packages(exclude=["tests", "example"]),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: OS Independent",
        ],
        install_requires=["hydra-core>=1.0.0rc1", "nevergrad>=0.3.2"],
        include_package_data=True,
    )
