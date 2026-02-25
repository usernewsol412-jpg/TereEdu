lofrom fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
#from bot import Bot
from whatsapp import WhatsAppClient
import os

router = APIRouter()
#bot = Bot()
cliente = WhatsAppClient()

TOKEN_CONEXION_META = os.environ.get("TOKEN_CONEXION_META", "TERESITAEDU")


@router.get("/webhook")
async def verificar_webhook(request: Request):
    params = dict(request.query_params)
    if params.get("hub.verify_token") == TOKEN_CONEXION_META:
        return PlainTextResponse(content=params["hub.challenge"])
    return PlainTextResponse(content="token inválido", status_code=403)


@router.post("/webhook")
async def recibir_mensaje(request: Request):
    data = await request.json()
    try:
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]
        numero = mensaje["from"]
        #tipo = mensaje["type"]
        cliente.enviar_mensaje(numero, "Hello World! jijiji") #Mensaje para responder

        #if tipo == "text":
        #   texto = mensaje["text"]["body"]
        #elif tipo == "interactive":
        #    texto = mensaje["interactive"]["list_reply"]["id"]
        #else:
        #    return {"status": "ok"}

       # bot.procesar(texto, numero, cliente)
    except KeyError:
        pass
    return {"status": "ok, todo bien!"}
