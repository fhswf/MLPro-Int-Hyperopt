.. _Howto RL HT 001:
Howto RL-HT-001: Hyperparameter Tuning using Hyperopt
=====================================================

**Prerequisites**

Please install the following packages to run this examples properly:

    - `Hyperopt <https://pypi.org/project/hyperopt/>`_



**Executable code**

.. literalinclude:: ../../../../test/howtos/rl/howto_rl_ht_001_hyperopt.py
	:language: python



**Results**

.. code-block:: bashh

    2023-02-12  16:44:58.495569  I  HyperParam Tuner "Hyperopt": Instantiated
    2023-02-12  16:44:58.496565  I  HyperParam Tuner "Hyperopt": Wrapped package hyperopt installed in version 0.2.7
    2023-02-12  16:44:58.496565  I  HyperParam Tuner "Hyperopt": Hyperopt configuration is successful
    2023-02-12  16:44:58.496565  I  Training "RL": Instantiated
    2023-02-12  16:44:58.497574  I  Training "RL": Training started (with hyperparameter tuning)
    2023-02-12  16:44:58.503565  I  HyperParam Tuner "Hyperopt": Spaces for hyperopt is ready
    2023-02-12  16:44:58.503565  I  HyperParam Tuner "Hyperopt": ------------------------------------------------------------------------------

    2023-02-12  16:44:58.536565
    I  HyperParam Tuner "Hyperopt":
    Trial number 0 has started

    2023-02-12  16:44:58.537565
    I  HyperParam Tuner "Hyperopt":
    ------------------------------------------------------------------------------

    2023-02-12  16:45:00.336566
    I  HyperParam Tuner "Hyperopt":
    Trial number 1 has finished

    2023-02-12  16:45:00.337566
    I  HyperParam Tuner "Hyperopt":
    ------------------------------------------------------------------------------

    2023-02-12  16:45:00.353564
    I  HyperParam Tuner "Hyperopt":
    Trial number 1 has started

    2023-02-12  16:45:00.353564
    I  HyperParam Tuner "Hyperopt":
    ------------------------------------------------------------------------------

    2023-02-12  16:45:02.055567
    I  HyperParam Tuner "Hyperopt":
    Trial number 2 has finished

    2023-02-12  16:45:02.056566
    I  HyperParam Tuner "Hyperopt":
    ------------------------------------------------------------------------------




**Cross Reference**

    - `API Reference - RL Agent <https://mlpro.readthedocs.io/en/latest/content/99_appendices/appendix2/sub/core/mlpro_rl/11_agents.html>`_
    - `API Reference - RL Environments <https://mlpro.readthedocs.io/en/latest/content/99_appendices/appendix2/sub/core/mlpro_rl/01_environments.html>`_
    - `API Reference - RL Scenario and Training <https://mlpro.readthedocs.io/en/latest/content/99_appendices/appendix2/sub/core/mlpro_rl/21_scenarios_training.html>`_
    - `API Reference - Machine Learning <https://mlpro.readthedocs.io/en/latest/content/99_appendices/appendix2/sub/core/mlpro_bf/05_layer4_machine_learning.html>`_
