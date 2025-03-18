CROPS_PRICES = {
    "Maize" : 200,
    "Wheat": 250,
    "Rice" : 300
}

WEATHER_UPDATES = {
    "Kigali" : "Sunny, 25ºC",
    "Musanze" : "Rainy, 22ºC",
    "Nyabihu" : "Cloud, 28ºC",
    "Huye" : "Sunny, 25ºC",
    "Nyagatare" : "Sunny, 27ºC"
}

PRODUCTS = {
    "Feritilizer" : {"code": "1", "price": 50},
    "Seeds" : {"code": "2", "price": 30}
}

TRANSLATIONS = {
    "en": {
        "main_menu": """
            CON What would you like to check?\n
            1. My Account\n
            2. My phone number\n
            3. Crops Prices\n
            4. Weather updates\n
            5. Order Supplies
        """,
        "account_menu": """
            CON Choose account information:\n
            1. Account Balance\n
            2. Account number
        """,
        "invalid_choice": "END Invalid choice. Please try again.",
        "account_not_found": "END Account not found",
        "crops_prices": "END Crops Prices:\n",
        "weather_updates": "END Weather Updates:\n",
        "order_supplies": "END Order Supplies:\n",
        "phone_number": "END Your phone number is {}",
        "balance": "END Your account balance is ${}",
    },
    "fr": {
        "main_menu": """
            CON Que voulez-vous vérifier?\n
            1. Mon compte\n
            2. Mon numéro de téléphone\n
            3. Prix des cultures\n
            4. Mises à jour météo\n
            5. Commander des fournitures
        """,
        "account_menu": """
            CON Choisissez les informations de compte:\n
            1. Solde du compte\n
            2. Numéro de compte
        """,
        "invalid_choice": "END Choix invalide. Veuillez réessayer.",
        "account_not_found": "END Compte introuvable",
        "crops_prices": "END Prix des cultures:\n",
        "weather_updates": "END Mises à jour météo:\n",
        "order_supplies": "END Commander des fournitures:\n",
        "phone_number": "END Votre numéro de téléphone est {}",
        "balance": "END Votre solde est ${}",
    },
    "rw": {
        "main_menu": """
            CON Mushaka kureba iki?\n
            1. Konti yanjye\n
            2. Nimero yanjye ya telefoni\n
            3. Ibiciro by'ibihingwa\n
            4. Iteganyagihe\n
            5. Gukoresha ibikoresho
        """,
        "account_menu": """
            CON Hitamo amakuru ya konti:\n
            1. Umutungo wa konti\n
            2. Nimero ya konti
        """,
        "invalid_choice": "END Hitamo si cyo. Ongera ugerageze.",
        "account_not_found": "END Konti ntiboneka",
        "crops_prices": "END Ibiciro by'ibihingwa:\n",
        "weather_updates": "END Iteganyagihe:\n",
        "order_supplies": "END Gukoresha ibikoresho:\n",
        "phone_number": "END Nimero ya telefoni yawe ni {}",
        "balance": "END Umutungo wawe ni ${}",
    },
}
