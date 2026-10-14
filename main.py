import os
from nicegui import ui
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
cliente = genai.Client(api_key=api_key)

MODEL_ID = "gemini-3-flash-preview"

def enviar():
    pregunta = entrada.value
    if not pregunta.strip():
        return
    resultado.set_text('Pensando... ⏳')
    try:
        response = cliente.models.generate_content(model=MODEL_ID, contents=pregunta)
        resultado.set_text(response.text)
    except Exception as e:
        resultado.set_text(f'Error: {e}')

with ui.card().classes('w-96 mx-auto mt-10 p-4'):
    ui.label('Chat Gemini!').classes('text-xl font-bold')
    entrada = ui.input(placeholder='Escribe tu pregunta').classes('w-full')
    ui.button('ENVIAR', on_click=enviar).classes('w-full bg-blue-500 text-white')
    resultado = ui.label('').classes('w-full whitespace-pre-wrap mt-4')

port = int(os.environ.get("PORT", 8080))
ui.run(title="Chat Gemini", host="0.0.0.0", port=port)
