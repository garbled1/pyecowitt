from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pyecowitt',
      version='0.21',
      description='Module to communicate with the Ecowitt procotol',
      long_description='Module to communicate with the Ecowitt protocol',
      url='https://github.com/garbled1/pyecowitt',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      author='Tim Rightnour',
      author_email='root@garbled.net',
      license='Apache 2.0',
      packages=['pyecowitt'],
      install_requires=[
          'aiohttp',
      ],
      include_package_data=True,
      zip_safe=False)
