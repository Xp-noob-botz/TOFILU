import re
import os
from os import getenv, environ
from Script import script 
from dotenv import load_dotenv

load_dotenv()
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
# Owner Information
API_ID = int(environ.get("API_ID", "22287041"))
API_HASH = environ.get("API_HASH", "c149386dcd58a40fa9fe60e632e161d4")
ADMINS = int(environ.get("ADMINS", "6141937812"))
# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://filetourlpublic:p2vQrgGzOekTb2je@cluster0.aebxqii.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "Cluster0")
FORCE_SUB = os.environ.get("FORCE_SUB", "PandaWep") 
# Bot Information
BOT_TOKEN = environ.get("BOT_TOKEN", "7195438444:AAFktIMnt2b3tz-LugeFOftjCNuFb5s7r00")
BOT_USERNAME = environ.get("BOT_USERNAME", "ToolForTGBOT") # your bot username without @

PICS = (environ.get('PICS', 'https://image.pandawep.in/gojox.png https://graph.org/file/d68cff609fb9b1ffca594.jpg https://graph.org/file/c321989941ce389568583.jpg https://graph.org/file/6c947549f7415347e8071.jpg https://graph.org/file/d257e0e98212703704661.jpg https://graph.org/file/75f9ae7726adcd9ae74ac.jpg https://graph.org/file/461dfe378c836d497705a.jpg')).split() # Bot Start Picture
DVEPICS = (environ.get('DVEPICS', 'https://graph.org/file/7eab3cf9705bdb8e807af.jpg https://graph.org/file/7eab3cf9705bdb8e807af.jpg')).split()
USEPICS = (environ.get('USEPICS', 'https://graph.org/file/afc6eb64059916bb1e336.jpg https://graph.org/file/2ed012e38ea1a208b71ee.jpg')).split()
QRPICS = (environ.get('QRPICS', 'https://graph.org/file/b6c322f3ea20a3c7036f7.jpg')).split()

# Auto Delete Information
AUTO_DELETE = int(environ.get("AUTO_DELETE", "10")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "600")) # Time in Seconds


# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002018490404"))
# FCHANNEL_ID = int(environ.get("FCHANNEL_ID", "-1002231931962"))
FORCE_SUB_CHANNEL = int(environ.get("FORCE_SUB_CHANNEL", "-1002018490404"))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002018490404')).split()]
# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
# Enable - True or Disable - False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# File Stream Config
class Var(object):
    MULTI_CLIENT = False
    name = str(getenv('name', 'filetolinkvjbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002018490404'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    
    if HAS_SSL:
        URL = "https://xyz-pandawep.koyeb.app/"
    else:
        URL = "https://xyz-pandawep.koyeb.app/"
