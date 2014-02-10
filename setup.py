from setuptools import setup, find_packages
import highlighter

setup(
    name='twentytab-highlighter',
    version=highlighter.__version__,
    author='20Tab S.r.l.',
    author_email='info@20tab.com',
    description='A django app permits to highlight the searched words (self.query) in a long text and truncates it, counts number of chars == max_length',
    url='https://github.com/20tab/twentytab-highlighter',
    packages=find_packages(),
)
