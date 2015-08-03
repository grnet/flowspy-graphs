from setuptools import setup

setup(
    name='flowspy-graphs',
    version='0.1',
    description='monitoring plugin for flowspy',
    author='Stavros Kroustouris',
    author_email='staurosk@noc.grnet.gr',
    license='GPLv3',
    packages=['graphs'],
    install_requires=['requests'],
    zip_safe=False
)
