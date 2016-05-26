from setuptools import setup

setup(
    name='aws-fuzzy-finder',
    version='0.3.4',
    url='https://github.com/pmazurek/aws-fuzzy-finder',
    description='SSH into AWS instances using fuzzy search through tags.',
    download_url='https://github.com/pmazurek/aws-fuzzy-finder/tarball/0.3.4',
    author='Piotr Mazurek, Daria Rudkiewicz',
    keywords=['aws', 'ssh', 'fuzzy', 'ec2'],
    packages=['aws_fuzzy_finder'],
    package_data={'': [
        'libs/fzf-0.12.1-linux_386',
        'libs/fzf-0.12.1-linux_amd64',
        'libs/fzf-0.12.1-darwin_386',
        'libs/fzf-0.12.1-darwin_amd64',
    ]},
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
