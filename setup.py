from setuptools import setup, find_packages

setup(
    name='ear',
    description='EBU ADM Renderer',
    version='2.1.0',

    url='https://github.com/ebu/ebu_adm_renderer',

    author='EBU',
    author_email='ear-admin@list.ebu.ch',
    license='BSD-3-Clause-Clear',

    long_description=open('README.md').read() + '\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',

    install_requires=[
        'numpy~=1.14',
        'scipy~=1.0',
        'attrs>=22.2',
        'PyYAML~=6.0',
        'lxml~=4.4',
        'six~=1.11',
        'multipledispatch~=1.0',
        # required until 2024-10 when python 3.9 will be the minimum supported version
        'importlib_resources>=5.0',
    ],

    extras_require={
        'test': [
            'pytest~=6.2',
            'pytest-datafiles~=2.0',
            'pytest-cov~=3.0',
            'soundfile~=0.10',
        ],
        'dev': [
            'flake8~=3.5',
            'flake8-print~=3.1',
            'flake8-string-format~=0.2',
        ],
    },

    packages=find_packages(),

    package_data={
        "ear.test": ["data/*.yaml", "data/*.wav"],
        "ear.core": ["data/*.yaml", "data/*.dat"],
        "ear.core.test": ["data/psp_pvs/*.npz"],
        "ear.core.objectbased.test": ["data/gain_calc_pvs/*"],
        "ear.fileio.adm": ["data/*.xml"],
        "ear.fileio.adm.test": ["test_adm_files/*.xml"],
        "ear.fileio.bw64.test": ["test_wav_files/*.wav"],
    },

    entry_points={
        'console_scripts': [
            'ear-render = ear.cmdline.render_file:main',
            'ear-utils = ear.cmdline.utils:main'
        ]
    },
)
