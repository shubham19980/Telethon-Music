import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "28748046"))
    API_HASH = os.environ.get("API_HASH", "53d10070adc69ac731ba1ac763a2ac55")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","6192785868:AAEWaPVcbxXdnhrZ_2JWbe7jlTCR3SKEMrc")
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOIcBu00uYQd3sQIwa5n6QwkPKaGaHyK8gSpw7BzwNH6tkzFX9YQWhZIrTQ3hCxajwvINw2ZhypeuobJRl3HBarmHz6VGVS3-1fs6vUkKVez2BLxw88N87lNjQcE33Go_q-V9lMj7Nl4N1cMvNdERWgaNTYGeHWrFQMNm0nLCJ_MpcBbjYoAu6ujDuaoOXGwHpNkE0UOYf-hrJXvz3dG4szlvJiXfz84etXL4_SIYBWZ2x9fdWdb2wVqk-ZLHuYdLpR_bsBlnpx6p0ioSpcnaR5VRHOWqwNq1OmEg2-ULz5qlChGRxQgqMFJQQTKuqH4uqVYjoj5JPa_urAbG1bLAIxnq9Hg= )
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
