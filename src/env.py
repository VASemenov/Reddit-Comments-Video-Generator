import os
from pathlib import Path

# Paths config
ROOT_PATH = str(Path(__file__).parent.parent)
MEDIA_PATH = ROOT_PATH + '/media/'
AUDIO_PATH = ROOT_PATH + '/media/audio/'
VIDEO_PATH = ROOT_PATH + '/media/video/'
FRAMES_PATH = ROOT_PATH + '/media/frames/'
MUSIC_PATH = ROOT_PATH + '/media/music/'
TRANSITIONS_PATH = ROOT_PATH + '/media/transition/'

# Set of paths that will be created at the start
paths = [
    MEDIA_PATH,
    AUDIO_PATH,
    VIDEO_PATH,
    FRAMES_PATH,
    MUSIC_PATH,
    TRANSITIONS_PATH,
]

# Create directories
# Called at the start
def init_paths():
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)