from setuptools import setup, find_packages

setup(
    name='FractalGlyphEngine',
    version='1.0.0',
    author='Dicaoz – Eduardo Molina 🇪🇨',
    author_email='ernestomunozmolina@gmail.com',
    description='Sistema simbólico fractal con codificación cuántico-lingüística',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'scikit-learn'
    ],
    python_requires='>=3.7',
)
