#
#
#

import configparser

class Config(object):
    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        self.username = config.get('Credentials', 'Username', fallback=None)
        self.password = config.get('Credentials', 'Password', fallback=None)

        self.owner_id = config.get('Permissions', 'OwnerID', fallback=None)

        self.command_prefix = config.get('Chat', 'CommandPrefix', fallback='!')

        # Validation logic for bot settings.
        if not self.username or not self.password:
            raise ValueError('A username of password was not specified in the configuration file.')

        if not self.owner_id:
            raise ValueError("An owner is not specified in the configuration file.")