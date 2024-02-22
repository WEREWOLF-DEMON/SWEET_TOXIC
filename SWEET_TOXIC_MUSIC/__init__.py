from SWEET_TOXIC_MUSIC.core.bot import SWEET_TOXIC_DEVIL
from SWEET_TOXIC_MUSIC.core.dir import dirr
from SWEET_TOXIC_MUSIC.core.git import git
from SWEET_TOXIC_MUSIC.core.userbot import Userbot
from SWEET_TOXIC_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DAXX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
