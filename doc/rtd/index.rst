.. MLPro Documentations documentation master file, created by
   sphinx-quickstart on Wed Sep 15 12:06:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MLPro-Int-Hyperopt - Integration of Hyperopt into MLPro
=================================================

Welcome to MLPro-Int-Hyperopt, an extension to MLPro to integrate the Hyperopt package.
MLPro is a middleware framework for standardized machine learning in Python. It is
developed by the South Westphalia University of Applied Sciences, Germany, and provides
standards, templates, and processes for hybrid machine learning applications. Hyeperopt, in
turn, provides state-of-the-art algorithms for hyper parameter tuning in the context of machine
learning model development.

MLPro-Int-Hyperopt provides wrapper classes that enable the use of the Hyper Parameter Tuning mechanism
in your MLPro applications. The use of these wrappers is illustrated in following example programs.



**Preparation**

Before running the examples, please install the latest versions of MLPro, Hyperopt, and MLPro-Int-Hyperopt as follows:

.. code-block:: bash

   pip install mlpro-int-hyperopt[full] --upgrade


**See also**
   - `MLPro - The integrative middleware framework for standardized machine learning in Python <https://mlpro.readthedocs.io>`_ 
   - `MLPro-BF-ML - Sub-framework for machine learning <https://mlpro.readthedocs.io/en/latest/content/02_basic_functions/mlpro_bf/sub/layer4_machine_learning/03_training_and_tuning.html>`_
   - `Hyperopt - Distributed Asynchronous Hyper-parameter Optimization <https://hyperopt.github.io/hyperopt/>`_
   - `MLPro-Int-Hyperopt on GitHub <https://github.com/fhswf/MLPro-Int-Hyperopt>`_
   - `MLPro-Int-Hyperopt on PyPI <https://pypi.org/project/mlpro-int-hyperopt>`_
   - `Further MLPro extensions <https://mlpro.readthedocs.io/en/latest/content/04_extensions/main.html>`_


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: HOME

   self

.. toctree::
   :maxdepth: 2
   :caption: EXAMPLE POOL
   :glob:


   content/01_examples_pool/*

.. toctree::
   :maxdepth: 2
   :caption: API REFERENCES
   :glob:


   content/02_api_references/*

.. toctree::
   :maxdepth: 2
   :caption: ABOUT
   :glob:


   content/03_about/*
