from setuptools import setup


setup(
    name='holidays_comparison',
    version='1.0.0',
    description='Allows the user to get the holidays comparison between two countries',
    url='https://github.com/CarlosDCorrea/holidays_comparison',
    author='Carlos Correa',
    author_email='carlosdcorrea3@gmail.com',
    packages=['holidays_comparison'],
    include_package_data=True,
    install_requires=[
        'holidays', 'openpyxl'
    ],
    entry_points={'console_scripts': ["holidays_comparison=holidays_comparison.main:main"]}
)
