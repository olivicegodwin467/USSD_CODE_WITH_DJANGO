from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import UserSession, Account
from .data import CROPS_PRICES, WEATHER_UPDATES, PRODUCTS, TRANSLATIONS

logger = logging.getLogger(__name__)

@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            session_id = data.get("session_id")
            phone_number = data.get("phone_number")
            text = data.get("text", "").strip()

            if not session_id or not phone_number:
                return JsonResponse({"Error": "session_id and phone_number are required"}, status=400)

            # Get or create a user session
            session, created = UserSession.objects.get_or_create(
                session_id=session_id,
                defaults={"phone_number": phone_number, "step": "main_menu", "language": "en"}
            )

            response = ""

            # Language selection menu
            if text == "":
                session.step = "language_menu"
                session.save()
                response = """
                CON Choose your language:\n
                1. English\n
                2. Français\n
                3. Kinyarwanda
                """
            elif session.step == "language_menu":
                if text == "1":
                    session.language = "en"
                elif text == "2":
                    session.language = "fr"
                elif text == "3":
                    session.language = "rw"
                else:
                    response = TRANSLATIONS[session.language]["invalid_choice"]
                    return JsonResponse({"response": response})

                session.step = "main_menu"
                session.save()
                response = TRANSLATIONS[session.language]["main_menu"]
            elif text == "1":
                session.step = "account_menu"
                session.save()
                response = TRANSLATIONS[session.language]["account_menu"]
            elif text == "1*1":
                try:
                    account = Account.objects.get(phone_number=phone_number)
                    response = TRANSLATIONS[session.language]["balance"].format(account.balance)
                except Account.DoesNotExist:
                    response = TRANSLATIONS[session.language]["account_not_found"]
            elif text == "2":
                response = TRANSLATIONS[session.language]["phone_number"].format(phone_number)
            elif text == "3":
                crops_prices = TRANSLATIONS[session.language]["crops_prices"] + "\n".join(
                    [f"{crop}: {price}" for crop, price in CROPS_PRICES.items()]
                )
                response = crops_prices
            elif text == "4":
                weather_updates = TRANSLATIONS[session.language]["weather_updates"] + "\n".join(
                    [f"{city}: {update}" for city, update in WEATHER_UPDATES.items()]
                )
                response = weather_updates
            elif text == "5":
                order_supplies = TRANSLATIONS[session.language]["order_supplies"] + "\n".join(
                    [f"{product}: {price}" for product, price in PRODUCTS.items()]
                )
                response = order_supplies
            else:
                response = TRANSLATIONS[session.language]["invalid_choice"]

            return JsonResponse({"response": response})

        except json.JSONDecodeError:
            return JsonResponse({"Error": "Invalid JSON format"}, status=400)

    return JsonResponse({"Error": "Invalid request"}, status=400)
