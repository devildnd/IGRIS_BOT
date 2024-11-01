from SaitamaRobot.sample_config import Config

class Development(Config):
    OWNER_ID = 5969684674  # your telegram ID
    OWNER_USERNAME = "khoonkhardevils"  # your telegram username
    API_KEY = "6834532674:AAEpAlwzL84xk7Y6sDpfHIoyGFVrYQlisNs"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    JOIN_LOGGER = '-1001218284362' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    SUDO_USERS = [18673980, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
