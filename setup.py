from setuptools import setup, find_packages

setup(
    name='fpextraction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "opencv-python==4.10.0.82",
        "numpy==1.26.4",
        "scikit-image==0.23.2"
    ],
    url='https://github.com/DevjareUN/Fingerprint-Feature-Extraction',
)

