import os
import uuid
from setuptools import setup, find_packages

try:
    from pip.req import parse_requirements
except ImportError:
    raise ImportError('You should install pip')

REQUIREMENTS = [str(ir.req) for ir in parse_requirements(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'),
    session=uuid.uuid1()
)]

setup(
    name='chineseMarkov',
    version='0.1.3',
    description='Chinese Sentence Generator',
    long_description=open('README.md').read(),
    author='Kimice',
    author_email='kimiceqc@gmail.com',
    url='https://github.com/Kimice/ChineseMarkov',
    license='GPLv3',
    packages=find_packages(exclude=['test', ]),
    install_requires=REQUIREMENTS
)
