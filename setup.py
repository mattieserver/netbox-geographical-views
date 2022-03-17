from setuptools import setup, find_packages


setup(
    name='netbox-geographical-views',
    version='0.0.1-alpha.1',
    description='A netbox plugin that plots your devices on a world map',
    url='https://github.com/mattieserver/netbox-geographical-views',
    author='Mattijs Vanhaverbeke',
    license='Apache 2.0',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    project_urls={
        'Source': 'https://github.com/mattieserver/netbox-geographical-views',
    },
)