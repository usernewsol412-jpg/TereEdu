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
@router.post("/webhook/")
async def recibir_mensaje(request: Request):
    data = await request.json()

    try:
        value = data["entry"][0]["changes"][0]["value"]

        # 🔹 Solo procesar mensajes entrantes
        if "messages" in value:
            mensaje = value["messages"][0]
            numero = mensaje["from"]
            texto = mensaje.get("text", {}).get("body", "")

            print(f"MENSAJE DE {numero}: {texto}", flush=True)

            # Responder
            cliente.enviar_mensaje(numero, "Hello World jiji!")

        # 🔹 Ignorar completamente statuses
        # (no hacemos nada si solo viene 'statuses')

    except Exception:
        pass

    return {"status": "OKA"}
