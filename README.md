# Frontside #

MAME Frontend in pygame.

You've caught this right at the start. Not a lot here right now. Check back later.

You'll need pygame, sqlite, Python > 2.6 and maybe some other stuff, haven't collated the dependencies yet.

Oh, and a copy of MAME somewhere. Default config file is frontside.ini.

It does bootstrap, there are command line and config options, there is a database. These are as follows:

usage: frontside.py [-h] [-l LOG_FILE]
                    [-L {debug,info,warning,critical,error}] [-C CONFIG_FILE]
                    [-d DATABASE_PATH] [-t THEME] [-p PROFILE] [-v]

Frontside. M.A.M.E. Front end using pyGame. Good for frame buffers.

optional arguments:
  -h, --help            show this help message and exit
  -l LOG_FILE, --log_file LOG_FILE
                        Log file location
  -L {debug,info,warning,critical,error}, --log_level {debug,info,warning,critical,error}
                        Log level
  -C CONFIG_FILE, --config_file CONFIG_FILE
                        Config file location
  -d DATABASE_PATH, --database_path DATABASE_PATH
                        Database file location
  -t THEME, --theme THEME
                        Interface theme
  -p PROFILE, --profile PROFILE
                        User profile selection
  -v, --version         Show the version number
