from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_topal',
    version='0.0.1',
    description='clean folder - script puts things in order in the specified folder ',
    url='http://github.com/dummy_user/useful',
    author='Yurii Topal',
    author_email='yuriy.topal@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder_topal.main:main']}
)