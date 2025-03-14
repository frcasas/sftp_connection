from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="sftp_connection",
    version="0.1",
    include_package_data=True,
    python_requires='>=3.9',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    description="A short description of your package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.13",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)