from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io
from gtts import gTTS
import base64

app = FastAPI()

@app.post("/tts")
async def text_to_speech(text: str):
    # Cria um objeto gTTS com o texto fornecido
    tts = gTTS(text=text, lang='pt')
    bytes_list = []
    audio_bytes = tts.stream()
    for audio_bit in audio_bytes:
        bytes_list.append(audio_bit)
    audio_buffer = io.BytesIO(*bytes_list)
    audio_data = audio_buffer.read()
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')

    return {"audio_base64": audio_base64}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)