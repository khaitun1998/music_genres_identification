from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import sys

def chunks_audio(file_path):
    song = AudioSegment.from_mp3(file_path)

    length_file = 30 * 1000

    chunks = make_chunks(song, length_file)

    for i, chunk in enumerate(chunks):
        chunks_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), f'test_data/chunks/chunks{i+1}.mp3'))
        chunk_name = chunks_path
        chunk.export(chunk_name, format="mp3")

    return len(chunks)