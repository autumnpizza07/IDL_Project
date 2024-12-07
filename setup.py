from setuptools import setup, find_packages

setup(
    name='conformer',
    packages = find_packages(),
    version='1.0',
    description='Convolution-augmented Transformer for Speech Recognition',
    author='Soohwan Kim',
    author_email='sh951011@gmail.com',
    url='https://github.com/sooftware/conformer',
    install_requires=[
        'torch>=1.4.0',
        'numpy',
    ],
    keywords=['asr', 'speech_recognition', 'conformer', 'end-to-end'],
    python_requires='>=3.6'
)
