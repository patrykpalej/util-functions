from setuptools import setup

VERSION = "1.0.0"

setup(
  name="util_functions",
  version=VERSION,
  author="Patryk Palej",
  description="Repository contains utility functions which perform commonly needed operations ",
  packages=["util_functions"],
  install_requires=["numpy", "pandas"]
)
