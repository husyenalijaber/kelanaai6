def get_trip_category(budget):
    """
    Determines trip category based on budget.

    Args:
        budget (float): Total travel budget

    Returns:
        str: Trip category ("Backpacker", "Standard", or "Luxury")
    """
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"


def get_travel_season(travel_month):
    """
    Determines travel season based on month.

    Args:
        travel_month (str): Month of travel (e.g. "December")

    Returns:
        str: Season category
    """
    month_normalized = travel_month.strip().lower()

    if month_normalized == "december":
        return "Peak Season"
    elif month_normalized == "june":
        return "Holiday Season"
    else:
        return "Regular Season"


def calculate_daily_budget(budget, days):
    """
    Calculates daily budget allocation.

    Args:
        budget (float): Total travel budget
        days   (int)  : Number of travel days

    Returns:
        float: Daily budget amount
    """
    return budget / days


def get_place_recommendations(destination):
    """
    Returns a list of recommended places based on destination.

    Args:
        destination (str): Travel destination name

    Returns:
        list: List of recommended place names
    """
    recommendations = {
        "japan": [
            "Tokyo Tower",
            "Shibuya Crossing",
            "Mount Fuji",
            "Kyoto Temples",
            "Osaka Castle",
        ],
        "indonesia": [
            "Bali Rice Terraces",
            "Borobudur Temple",
            "Komodo Island",
            "Raja Ampat",
            "Bromo Volcano",
        ],
        "france": [
            "Eiffel Tower",
            "Louvre Museum",
            "Palace of Versailles",
            "Mont Saint-Michel",
            "French Riviera",
        ],
        "thailand": [
            "Grand Palace",
            "Phi Phi Islands",
            "Chiang Mai Night Bazaar",
            "Ayutthaya Ruins",
            "Railay Beach",
        ],
        "italy": [
            "Colosseum",
            "Vatican City",
            "Venice Canals",
            "Amalfi Coast",
            "Cinque Terre",
        ],
    }

    key = destination.strip().lower()
    return recommendations.get(key, [
        f"Old Town {destination}",
        f"Central Museum {destination}",
        f"National Park {destination}",
        f"Local Market {destination}",
        f"Waterfront {destination}",
    ])
