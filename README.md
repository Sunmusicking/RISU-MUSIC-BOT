 

## <a name="🏮 ғᴇᴀᴛᴜʀᴇs 🏮"></a>Features
Starts streaming your inputs while downloading and converting them. Also, it
doesn't make produce files.

### 👮🏻‍♀️ Safe and handy

Restricts control and sensitive commands to admins.

# 🗑 Clean and spam free

Deletes old playing trash to keep your chats clean.

### 😎 Has cool controls

Lets you switch stream mode, loop, pause, resume, mute, unmute anytime.

### 🖼 Has cool thumbnails

Response your commands with cool thumbnails on the chat.

### 😉 Streams whatever you like

You can stream audio or video files, YouTube videos with any duration,
YouTube lives, YouTube playlists and even custom live streams like radios or m3u8 links or files in
the place it is hosted!

### 📊 Streams in multiple places

Allows you to stream different things in multiple chats simultaneously. Each
chat will have its own song queue.

### 🗣 Speaks different languages

Music Player is multilingual and speaks [various languages](#languages),
thanks to the translators.

## 🚀 <a name="deploy"></a>Deploy

[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://deploy.safone.tech)

Note: `First Fork The Repo Then Click On Deploy To Heroku Button!`


## ☁️ <a name="self_host"></a>Self Host

- Legecy Method
```bash
$ git clone https://github.com/AsmSafone/MusicPlayer
$ cd MusicPlayer
$ sudo apt install git curl python3-pip ffmpeg -y
$ pip3 install -U pip
$ curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
$ sudo apt install -y nodejs
$ sudo apt install build-essential
$ sudo npm install pm2@latest -g
$ pip3 install -U -r requirements.txt
$ cp sample.env .env
# < edit .env with your own values >
$ python3 main.py
```

- Docker Build Method
```bash
$ git clone https://github.com/AsmSafone/MusicPlayer
$ cd MusicPlayer
$ cp sample.env .env
# < edit .env with your own values >
$ sudo docker build . -t musicplayer
$ sudo docker run musicplayer
```

## ⚒ <a name="configs"></a>Configs

- `API_ID`: Telegram app id from https://my.telegram.org/apps.
- `API_HASH`: Telegram app hash from https://my.telegram.org/apps.
- `SESSION`: Pyrogram string session. You can generate from [here](https://replit.com/@AsmSafone/genStr).
- `SUDOERS`: ID of sudo users (separate multiple ids with space).
- `BOT_TOKEN`: Telegram bot token from https://t.me/botfather. (optional)
- `QUALITY`: Custom stream quality (high/medium/low) for the userbot in vc. Default: `high`
- `PREFIX`: Bot commad prefixes (separate multiple prefix with space). Eg: `! /`
- `LANGUAGE`: An [available](#languages) bot language (can change it anytime). Default: `en`
- `STREAM_MODE`: An stream mode like audio or video (can change it anytime). Default: `audio`
- `ADMINS_ONLY`: Put `True` if you want to make /play commands only for admins. Default: `False`
- `SPOTIFY_CLIENT_ID`: Spotify client id get it from [here](https://developer.spotify.com/dashboard/applications). (optional)
- `SPOTIFY_CLIENT_SECRET`: Spotify client secret get it from [here](https://developer.spotify.com/dashboard/applications). (optional)


## 📄 <a name="commands"></a>Commands

• /ping ᴜsᴀɢᴇ: `ᴄʜᴇᴄᴋ ɪғ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ`
• /repo 
ᴜsᴀɢᴇ: `ғɪʀsᴛ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ `
• /start | /help
ᴜsᴀɢᴇ: `sʜᴏᴡ ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴄᴏᴍᴍᴀɴᴅᴀs`
• /mode | /switch
nᴜsᴀɢᴇ: `sᴡɪᴛᴄʜ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴍᴏᴅᴇ (ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ)`
• /p | /play [sᴏɴɢ ɴᴀᴍᴇ | ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ]
ᴜsᴀɢᴇ: `ᴘʟᴀʏ ᴀ sᴏɴɢ ɪɴ ᴠᴄ ɪғ ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ ᴀᴅᴅ ᴛᴏ ǫᴜᴇᴜᴇ `
• /radio | /stream [ʀᴀᴅɪᴏ ᴜʀʟ | sᴛʀᴇᴀᴍ ʟɪɴᴋ]
ᴜsᴀɢᴇ: `ᴘʟᴀʏ ᴀ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ɪɴ ᴠᴄ ɪғ ᴀʟʀᴇᴀᴅʏ ᴘʟᴀʏɪɴɢ ᴀᴅᴅ ᴛᴏ ǫᴜᴇᴜᴇ`
• /pl | /playlist [ʏᴏᴜᴛᴜʙᴇ ᴘʟᴀʏʟɪsᴛ ʟɪɴᴋ]
ᴜsᴀɢᴇ: `ᴘʟᴀʏ ᴛʜᴇ ᴡʜᴏʟᴇ ʏᴏᴜᴛᴜʙᴇ ᴘʟᴀʏʟɪsᴛ ᴀᴛ ᴏɴᴄᴇ`
• /skip | /next
ᴜsᴀɢᴇ: `sᴋɪᴘ ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴏɴɢ`
• /m | /mute\nᴜsᴀɢᴇ: `ᴍᴜᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ`
• /um | /unmute
ᴜsᴀɢᴇ: `ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴍᴜᴛᴇᴅ sᴛʀᴇᴀᴍ`
• /ps | /pause\nᴜsᴀɢᴇ: `ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛʀᴇᴀᴍ`
• /rs | /resume
ᴜsᴀɢᴇ: `ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ`
• /list | /queue
ᴜsᴀɢᴇ: `sʜᴏᴡ ᴛʜᴇ sᴏɴɢs ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ`
• /mix | /shuffle
ᴜsᴀɢᴇ: `sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴘʟᴀʏʟɪsᴛ`
• /loop | /repeat
ᴜsᴀɢᴇ: `ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ʟᴏᴏᴘ ᴍᴏᴅᴇ`
• /lang | language [ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ ]
ᴜsᴀɢᴇ : `sᴇᴛ ᴛʜᴇ ʙᴏᴛ ʟᴀɴɢᴜᴀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ`
• /ip | /import\nᴜsᴀɢᴇ: `ɪᴍᴘᴏʀᴛ ǫᴜᴇᴜᴇ ғʀᴏᴍ ᴇxᴘᴏʀᴛᴇᴅ ғɪʟᴇ `\n\n• <prefix>ep | <prefix>export\nᴜsᴀɢᴇ : `ᴇxᴘᴏʀᴛ ᴛʜᴇ ǫᴜᴇᴜᴇ ғᴏʀ ɪᴍᴘᴏʀᴛ ɪɴ ғᴜᴛᴜʀᴇ`\n\n• <prefix>stop | <prefix>leave\nᴜsᴀɢᴇ: `ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴠᴄ ᴀɴᴅ ᴄʟᴇᴀʀ ᴛʜᴇ ǫᴜᴇᴜᴇ`\n\n• <prefix>restart | <prefix>update\nᴜsᴀɢᴇ: `ʀᴇsᴛᴀʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ`\n\n© **ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Simple_Mundaa) | [ᴅᴇᴍᴏɴ ᴄʀᴇᴀᴛᴏʀs](https://t.me/Demon_Creators)**"
}
 
