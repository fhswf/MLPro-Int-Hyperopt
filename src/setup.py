from setuptools import setup


setup(name='mlpro_int_hyperopt',
version='0.1.3',
description='MLPro: Integration Hyperopt',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_hyperopt'],

# Package dependencies for full installation
extras_require={
    "full": [
        "dill",
        "numpy",
        "matplotlib",
        "multiprocess",
        "mlpro",
        "hyperopt",
        "pandas"
    ],
},

zip_safe=False)