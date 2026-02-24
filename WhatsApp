import requests
import os


class WhatsAppClient:
    def __init__(self):
        self.access_token = os.environ.get("ACCESS_TOKEN", "")
        self.phone_id = os.environ.get("PHONE_ID", "")
        self.url = f"https://graph.facebook.com/v22.0/{self.phone_id}/messages"

    def _dividir(self, texto: str, limite: int = 4096) -> list:
        """Divide el texto en bloques que no superen el límite, respetando separadores de producto (\n\n)."""
        if len(texto) <= limite:
            return [texto]
        bloques = texto.split("\n\n")
        chunks = []
        actual = ""
        for bloque in bloques:
            segmento = (bloque + "\n\n") if actual else bloque
            if actual and len(actual) + len("\n\n" + bloque) > limite:
                chunks.append(actual)
                actual = bloque
            else:
                actual = actual + ("\n\n" + bloque if actual else bloque)
        if actual:
            chunks.append(actual)
        return chunks

    def enviar_mensaje(self, numero: str, texto: str):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        for parte in self._dividir(texto):
            body = {
                "messaging_product": "whatsapp",
                "to": numero,
                "type": "text",
                "text": {"body": parte}
            }
            r = requests.post(self.url, json=body, headers=headers)
            if r.status_code != 200:
                print(f"[WA ERROR] status={r.status_code} len={len(parte)} body={r.text[:300]!r}")

    def enviar_lista(self, numero: str, texto: str, boton: str, secciones: list):
        """
        secciones = [
            {
                "title": "Nombre de sección",
                "rows": [
                    {"id": "opcion_1", "title": "Opción 1", "description": "opcional"},
                    {"id": "opcion_2", "title": "Opción 2"},
                ]
            }
        ]
        """
        headers = {"Authorization": f"Bearer {self.access_token}"}
        body = {
            "messaging_product": "whatsapp",
            "to": numero,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {"text": texto},
                "action": {
                    "button": boton,
                    "sections": secciones
                }
            }
        }
        requests.post(self.url, json=body, headers=headers)
