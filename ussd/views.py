from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import UserSession, Account
from .data import CROPS_PRICES, WEATHER_UPDATES, PRODUCTS

logger = logging.getLogger(__name__)

@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received Data: {data}")  # Log incoming request data

            # Extract values safely
            session_id = data.get("session_id")
            phone_number = data.get("phone_number")
            text = data.get("text", "").strip()

            # Check if required fields exist
            if not session_id or not phone_number:
                return JsonResponse({"Error": "session_id and phone_number are required"}, status=400)

            # Get or create a user session
            session, created = UserSession.objects.get_or_create(
                session_id=session_id,
                defaults={"phone_number": phone_number, "step": "main_menu"}
            )

            response = ""  # Default response

            if text == "":
                session.step = 'main_menu'
                session.save()
                response = """CON What would you like to check?\n
                1. My Account\n 
                2. My phone number\n 
                3. Crops Prices\n 
                4. Weather updates\n
                5. Order Supplies
                """
            elif text == "1":
                session.step = "account_menu"
                session.save()
                response = "CON Choose account information: \n1. Account Balance\n2. Account number"
            elif text == "1*1":
                try:
                    account = Account.objects.get(phone_number=phone_number)
                    response = f"END Your account balance is ${account.balance}"
                except Account.DoesNotExist:
                    response = "END Account not found"
            elif text == "2":
                response = f"END Your phone number is {phone_number}"
            elif text == "3":
                response = "END Crops Prices:\n" + "\n".join([f"{x}: {y} Rwfr" for x, y in CROPS_PRICES.items()])
            elif text == "4":
                response = "END Weather Updates:\n" + "\n".join([f"{a}: {b}" for a, b in WEATHER_UPDATES.items()])
            elif text == "5":
                response = "END Order Supplies:\n" + "\n".join([f"{o}: {p}" for o, p in PRODUCTS.items()])
            else:
                response = "END Invalid choice. Please try again."

            return JsonResponse({"response": response})

        except json.JSONDecodeError:
            return JsonResponse({"Error": "Invalid JSON format"}, status=400)

    return JsonResponse({"Error": "Invalid request"}, status=400)
