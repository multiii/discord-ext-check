from distutils.core import setup

setup(
  name = 'discord-ext-checks',
  packages = ['discord-ext-checks'],
  version = '0.1', 
  license = 'MIT',
  description = 'A module which implements various new decorators to check for certain conditions in your discord commands',
  author = 'multi-yt76',
  author_email = '76multi@gmail.com',
  url = 'https://github.com/multi-yt76/discord-ext-checks',
  download_url = 'https://github.com/multi-yt76/discord-ext-checks/archive/v0.1.tar.gz',
  keywords = ['discord', 'check', 'functions'],
  install_requires=[
          'discord',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
