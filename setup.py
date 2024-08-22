from setuptools import setup, find_packages

setup(
    name='myfirstpipy',
    version='0.1',
    packages=find_packages(),
    description='A simple Hello World package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Seu Nome',
    author_email='seu.email@dominio.com',
    url='https://github.com/seu_usuario/myfirstpipy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
