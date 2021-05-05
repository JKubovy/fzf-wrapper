import os
import setuptools

project_dir = os.path.dirname(__file__)


def read_file(filename):
    with open(os.path.join(project_dir, filename), 'r', encoding='utf-8') as f:
        return f.read()


setuptools.setup(
    name='fzf-wrapper',
    version=read_file('VERSION').strip(),
    author='Jan Kubovy',
    author_email='JanKubovy94@gmail.com',
    license='MIT',
    description='Python wrapper for junegunn\'s fzf. Let user interactively choose from given choices',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/JKubovy/fzf-wrapper',
    project_urls={
        'Bug Tracker': 'https://github.com/JKubovy/fzf-wrapper/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)
