from nicegui import ui
import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@ui.page('/')
def home():
    ui.label('Mi Chatbot con Gemini').classes('text-2xl font-bold text-center w-full mt-4')
    chat = ui.column().classes('w-full max-w-2xl mx-auto p-4 gap-2 h-[70vh] overflow-auto border rounded')

    def enviar():
        pregunta = entrada.value.strip()
        if not pregunta:
            return
        with chat:
            ui.label(f'Tú: {pregunta}').classes('bg-blue-100 p-2 rounded self-end')
        entrada.value = ''
        try:
            respuesta = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=pregunta
            )
            with chat:
                ui.label(f'Bot: {respuesta.text}').classes('bg-gray-100 p-2 rounded')
        except Exception as e:
            with chat:
                ui.label(f'Error: {e}').classes('bg-red-100 p-2 rounded')

    with ui.row().classes('w-full max-w-2xl mx-auto mt-2'):
        entrada = ui.input(label='Escribe tu pregunta').classes('flex-grow').on('keydown.enter', enviar)
        ui.button('ENVIAR', on_click=enviar)

import os
ui.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
