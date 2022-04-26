import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "10581222")
        self.API_HASH: str = os.environ.get("API_HASH", "3821fef6f828ec26b116c520db18dc70")
        self.SESSION: str = os.environ.get("SESSION", "AQAN_WYAoDH9cyyD3_Fe3c3KJqVipYvu2gxCw4AS436T76F38fvxnPZ8UzSIQ9F1Uro3cfDeLKsajqKS_E0CcL51IpP6-huREHMatxzqN2AnUsD2yplKzvnOfZ7fq-xU95q5RKGsEbW517MFjcIeEU2-yBikqN3reWVYeJy-K04JTE8CmuzlUaY2Du6bmh8KC6QSW7_CJlk9yegok906Z-OBJNhuxRsjLBGo2iJV9p00bOVlBMkkfoylii_EtfeZJuTwb8tOGYFA-UI0CttvL5Ijy6x10mPEwjtb8HALSd0jyNkrMyf02yg3KKUtshCToTt6ld5SFUy5L_hByn9b3rn7AAAAATbl3U8A")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5190612090:AAFADwTTVC6PsstylETeFM9PygpORjzMxFg")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " 5009839424 5221911121 5290547167").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "/,.,!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
