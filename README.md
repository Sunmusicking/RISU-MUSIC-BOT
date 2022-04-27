# ʀɪsᴜ ᴍᴜsɪᴄ ʙᴏᴛ 

## 🏮 ғᴇᴀᴛᴜʀᴇs 🏮
Starts streaming your inputs while downloading and converting them. Also, it
doesn't make produce files.

### sᴀғᴇ ᴀɴᴅ ʜᴀɴᴅʏ

Restricts control and sensitive commands to admins.

### 🗑 Clean and spam free

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

## 🚀 <a name="deploy"></a>🔸ᴅᴇᴘʟᴏʏ🔸

### ᴅᴇᴘʟᴏʏ ᴛᴏ ʜᴇʀᴏᴋᴜ

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Sumit9969/RISU-MUSIC-BOT)

𝙽𝙾𝚃𝙴: `ғɪʀsᴛ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ sᴛᴀʀs`


##  <a name="self_host"></a>🇮🇳 sᴇʟғ ʜᴏsᴛ 🇮🇳

- ʟᴇɢᴇᴄʏ ᴍᴇᴛʜᴏᴅ
```bash
$ git clone https://github.com/Sumit9969/RISU-MUSIC-BOT
$ cd RISU-MUSIC-BOT
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

- ᴅᴏᴄᴋᴇʀ ʙᴜɪʟᴅ ᴍᴇᴛʜᴏᴅ
```bash
$ git clone https://github.com/Sumit9969/RISU-MUSIC-BOT
$ cd RISU-MUSIC-BOT
$ cp sample.env .env
# < edit .env with your own values >
$ sudo docker build . -t RISU-MUSIC-BOT
$ sudo docker run RISU-MUSIC-BOT
```

## <a name="commands"></a>⭕ ᴄᴏᴍᴍᴀɴᴅs ⭕

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

• /ip | /import ᴜsᴀɢᴇ: `ɪᴍᴘᴏʀᴛ ǫᴜᴇᴜᴇ ғʀᴏᴍ ᴇxᴘᴏʀᴛᴇᴅ ғɪʟᴇ `

• /ep | /export ᴜsᴀɢᴇ : `ᴇxᴘᴏʀᴛ ᴛʜᴇ ǫᴜᴇᴜᴇ ғᴏʀ ɪᴍᴘᴏʀᴛ ɪɴ ғᴜᴛᴜʀᴇ`

• /stop | /leave ᴜsᴀɢᴇ: `ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴠᴄ ᴀɴᴅ ᴄʟᴇᴀʀ ᴛʜᴇ ǫᴜᴇᴜᴇ`

• /restart | /update ᴜsᴀɢᴇ: `ʀᴇsᴛᴀʀᴛ ᴀɴᴅ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ`

© **ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Simple_Mundaa) | [ᴅᴇᴍᴏɴ ᴄʀᴇᴀᴛᴏʀs](https://t.me/Demon_Creators)
 
### 🏮 ᴄʀᴇᴅɪᴛ 🏮
[ᴀsᴍsᴀғᴏɴᴇ](https://github.com/AsmSafone)
