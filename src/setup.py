from setuptools import setup


setup(name='mlpro_int_hyperopt',
version='1.0.1',
description='MLPro: Integration Hyperopt',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_hyperopt'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro>=1.4.0",
        "hyperopt>=0.2.7",
        "setuptools >= 80.3.1"
    ],
},

zip_safe=False)
