from setuptools import setup

setup(
    name='test_eamanu',
    packages=['test_eamanu'],
    entry_points={
        'console_scripts':[
            'test_eamanu=test_eamanu.test_eamanu:main'
        ]
    }
)
