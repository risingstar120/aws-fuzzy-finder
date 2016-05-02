from setuptools import setup

setup(
    name='aws-fuzzy-finder',
    version='0.1',
    url='https://github.com/pmazurek/aws-fuzzy-finder',
    description='SSH into AWS instances using fuzzy search through tags.',
    download_url='https://github.com/pmazurek/aws-fuzzy-finder/tarball/0.1',
    author='Piotr Mazurek, Daria Rudkiewicz',
    keywords=['aws', 'ssh', 'fuzzy', 'ec2'],
    packages=['aws_fuzzy_finder'],
    install_requires=[
        'boto3==1.3.1',
        'click==6.6',
    ],
    entry_points=dict(
        console_scripts=[
            'aws-fuzzy = aws_fuzzy_finder.main:entrypoint',
        ]
    )
)
