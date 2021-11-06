from setuptools import find_packages, setup

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='mortgage-calculator',
    version='0.0.1',
    license='MIT',
    description='Simple mortgage calculator for calculating mortgage payments',
    long_description=long_description,
    author='Ahmed Ibrahim',
    author_email='aibrahim9449@gmail.com',
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(where='src', exclude=['tests*']),
    python_requires='>=3.9',
)
