thonfrom datetime import datetime, timedelta

def get_timeframe_start(timeframe: str) -> str:
    if timeframe == "1h":
        return (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S')
    elif timeframe == "1d":
        return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    elif timeframe == "7d":
        return (datetime.now() - timedelta(weeks=1)).strftime('%Y-%m-%dT%H:%M:%S')
    elif timeframe == "1y":
        return (datetime.now() - timedelta(weeks=52)).strftime('%Y-%m-%dT%H:%M:%S')
    else:
        return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')