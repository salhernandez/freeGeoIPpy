from setuptools import setup

setup(name='freeGeoIPpy',
      version='0.0.1',
      description='freegeopapi.net wrapper',
      url='https://github.com/salhernandez/freeGeoIPpy',
      author='Salvador Hernandez',
      author_email='hernandezg.sal@gmail.com',
      license='MIT 2.0',
      packages=['freeGeoIPpy'],
      install_requires=[
        'requests',
        'json'
      ],
      zip_safe=False)
