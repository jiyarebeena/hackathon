from datetime import datetime
from typing import List, Dict


def generate_analytics(receipts: List[Dict]):
    """
    receipts: list of receipts like:
    {
        "date": "2026-01-13",
        "total_co2": 14.7
    }
    """

    total_emissions = 0.0
    daily_data = {}
    weekly_data = {}
    monthly_data = {}

    for receipt in receipts:
        # parse date
        date_str = receipt["date"]
        co2 = receipt["total_co2"]

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        week_key = f"{date_obj.year}-W{date_obj.isocalendar()[1]}"
        month_key = date_obj.strftime("%Y-%m")

        # total
        total_emissions += co2

        # daily
        daily_data[date_str] = daily_data.get(date_str, 0) + co2

        # weekly
        weekly_data[week_key] = weekly_data.get(week_key, 0) + co2

        # monthly
        monthly_data[month_key] = monthly_data.get(month_key, 0) + co2

    return {
        "total_emissions": round(total_emissions, 2),
        "daily_breakdown": daily_data,
        "weekly_breakdown": weekly_data,
        "monthly_breakdown": monthly_data
    }
