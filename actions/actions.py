from rasa_sdk import Action
from typing import Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class PreguntarOpcion(Action):
    def name(self):
        return "utter_preguntar_opcion"

    def run(self, dispatcher, tracker, domain):
        opciones = "1. Paquetes 2. Asesorias 3. Cotizar 4. Preguntas Frecuentes"

        dispatcher.utter_message("¿Con que necesitas ayuda? {opciones}")

        return []


class CapturarInfoCliente(Action):
    def name(self) -> str:
        return "action_capturar_info_cliente"


    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        nombre = tracker.get_slot("nombre")
        apellido = tracker.get_slot("apellido")
        correo = tracker.get_slot("correo")
        num_tel = tracker.get_slot("num_tel")
        
        dispatcher.utter_message("Bienvenido {nombre} {apellido}, Su correo es: {correo} y su numero de contacto es: {num_tel}")

        return []