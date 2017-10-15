import io

from setuptools import setup, find_packages


def load_requirements(filename):
    with io.open(filename, encoding='utf-8') as reqfile:
        return [line.strip() for line in reqfile if not line.startswith('#')]


setup(
    name='ImaginMail',
    version='1.0.0',
    description='ImaginMail is a program that search on an specific imaginbank web and notify an user'
                'about new offers and films next to Madrid',
    author='Daniel Seijo',
    author_email='daniseijo12@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': ['imaginmail = imaginmail:cli'],
    },
)
