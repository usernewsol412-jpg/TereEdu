from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
#from bot import Bot
from WhatsApp import WhatsAppClient
import os

router = APIRouter()
#bot = Bot()
cliente = WhatsAppClient()

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "TERESITAEDU")


@router.get("/webhook")
@router.get("/webhook/")
async def verificar_webhook(request: Request):
    params = dict(request.query_params)
    print("[WEBHOOK GET] params:", params, flush=True)
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return PlainTextResponse(content=params["hub.challenge"])
    return PlainTextResponse(content="token inválido", status_code=403)


@router.post("/webhook")
@router.get("/webhook/")
async def recibir_mensaje(request: Request):
    data = await request.json()
    print("[WEBHOOK POST] body:", data, flush=True)
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
