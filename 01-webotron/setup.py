from setuptools import setup

setup(
    name='webotron-01',
    version='0.1',
    author='Shan Lu',
    author_email='lucian.lu63@gmail.com',
    description='Webotron 01 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/Lucian63/automation-aws-with-python/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)