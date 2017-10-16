import io

from setuptools import setup, find_packages


def load_requirements(filename):
    with io.open(filename, encoding='utf-8') as reqfile:
        return [line.strip() for line in reqfile if not line.startswith('#')]


setup(
    name='ImaginEmail',
    packages=find_packages(),
    include_package_data=True,
    version='1.0.3',
    description='ImaginEmail is a program that searches on an specific imaginbank web '
                'and notifies a user about new offers and films next to Madrid.',
    author='Daniel Seijo',
    author_email='daniseijo12@gmail.com',
    url='https://github.com/daniseijo/imaginemail',
    download_url='https://github.com/daniseijo/imaginemail/archive/1.0.3.tar.gz',
    license='MIT',
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': ['imaginemail = imaginemail.imaginemail:cli'],
    },
    keywords=['scraper', 'imaginbank', 'email'],
)
