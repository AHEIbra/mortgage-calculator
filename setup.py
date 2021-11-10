from setuptools import find_packages, setup

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='mortgage-calculator',
    version='0.0.1',
    license='MIT',
    description='Simple mortgage calculator for calculating mortgage payments',
    long_description=long_description,
    author='Ahmed Ibrahim',
    author_email='aibrahim9449@gmail.com',
    install_requires=read_requirements(),
    include_requirements=True,
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(where='src', exclude=['tests*']),
    python_requires='>=3.9',
    entry_points='''
        [console_scripts]
        mortgage-calculator=mortgage_calculator.cli:main
    ''',
)
