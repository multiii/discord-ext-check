from distutils.core import setup

setup(
  name = 'discord-ext-checks',
  packages = ['discord-ext-checks'],
  version = '0.1', 
  license = 'MIT',
  description = 'A module which implements various new decorators to check for certain conditions in your discord commands',   # Give a short description about your library
  author = 'multi-yt76',                   # Type in your name
  author_email = '76multi@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/multi-yt76/discord-ext-checks',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['discord', 'check', 'functions'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
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
