# coding: utf-8

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pip==8.1.2",
    "future==0.15.2",
    "wheel==0.29.0",
]

test_requirements = [
    "pytest==2.9.2",
    "pytest-runner==2.8",
    "coverage==4.0.3",
]

setup(
    name='shopidown',
    version='0.1.0',
    description="Simple markdown parser for Shopify",
    long_description=readme + '\n\n' + history,
    author="Douglas Soares de Andrade",
    author_email='contato@douglasandrade.com',
    url='https://github.com/douglas/shopidown',
    packages=[
        'shopidown',
    ],
    package_dir={'shopidown':
                 'shopidown'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='shopidown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    setup_requires=test_requirements,
    tests_require=test_requirements,
)
