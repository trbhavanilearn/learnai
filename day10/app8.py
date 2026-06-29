from faster_whisper import WhisperModel
from pprint import pprint
model=WhisperModel('base',device="cpu")
segments,info=model.transcribe("llm_chk.m4a")
for segement in segments:
    pprint(segement.text)
