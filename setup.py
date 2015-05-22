from setuptools import setup

setup(
    name='eliot-tree',
    version='15.0.0',
    description='Render Eliot logs as an ASCII tree',
    author='Jonathan Jacobs',
    url='https://github.com/jonathanj/eliottree',
    platforms='any',
    license='MIT',
    py_modules=['eliottree'],
    entry_points={
        # These are the command-line programs we want setuptools to install.
        'console_scripts': [
            'eliottree = eliottree:main',
        ],
    },
    install_requires=[
        'eliot >= 0.7'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: System :: Logging',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
