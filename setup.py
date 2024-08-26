from setuptools import setup, find_packages

import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/docs/requirements.txt"
install_requires = [] # Here we'll add: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

print(install_requires)

setup(
    name="syng_bts_imports",
    version='0.5.6',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'syng_bts_imports.RealData': ['SKCMPositive_4.csv'],
        'syng_bts_imports.Case.BRCASubtype': ['BRCASubtypeSel.csv'],
        'syng_bts_imports.Case.BRCASubtype': ['BRCASubtypeSel_test.csv'],
        'syng_bts_imports.Case.BRCASubtype': ['BRCASubtypeSel_train_epoch285_CVAE1-20_generated.csv'],
        'syng_bts_imports.Case.BRCASubtype': ['BRCASubtypeSel_train.csv'],
    },
    install_requires = install_requires,
    python_requires='>=3.6',
)