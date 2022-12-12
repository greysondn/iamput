import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iamput',
    version='0.0.1',
    author='J. "Dorian Greyson" L.',
    author_email='greysondn@gmail.com',
    description='a mod management system for forge',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    project_urls = {
        "Bug Tracker": ""
    },
    packages=['iamput'],
    install_requires=[
    ],
)