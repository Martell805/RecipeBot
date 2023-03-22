import setuptools

setuptools.setup(
    name='RecipeBot',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=['aiogram', 'sqlalchemy'],
    url='https://github.com/Martell805/RecipeBot',
    license='',
    author='Martell',
    author_email='vovasamb@yandex.ru',
    description='TG bot for recipes',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
