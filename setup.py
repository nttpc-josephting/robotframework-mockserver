from distutils.core import setup


setup(name = 'robotframework-mockserver',
      packages = ['MockServerLibrary'],
      package_dir  = {'' : 'src'},
      version = '0.1.0',
      description = 'Robot framework library for MockServer',
      author = 'Timo Yrjölä',
      author_email = 'timo.yrjola@gmail.com',
      url = 'https://github.com/tyrjola/robotframework-mockserver',
      download_url = 'https://github.com/tyrjola/robotframework-mockserver/archive/0.1.1.tar.gz',
      keywords = ['testing', 'robotframework', 'mockserver'],
      classifiers = [],
      install_requires=['requests'],
)
