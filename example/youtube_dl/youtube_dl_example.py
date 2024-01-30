from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioParameters
from pytgcalls.types import AudioQuality
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoParameters
from pytgcalls.types import VideoQuality


app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
call_py.join_group_call(
    -1001234567890,
    MediaStream(
        'https://www.youtube.com/watch?v=msiLgFkXvD8',
        audio_parameters=AudioParameters.from_quality(AudioQuality.HIGH),
        video_parameters=VideoParameters.from_quality(VideoQuality.HD_720p),
    ),
)
idle()
