import os
import time

TTS_VAL = "test"

os.system('echo %s | festival --tts', %TTS_VAL)
time.sleep(1)