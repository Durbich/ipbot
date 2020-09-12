from datetime import datetime as dt

def unique(reason):
    """Возвращает длинное число из текущей даты и времени.\n
    Требуется там, где нужны неповторяющиеся id"""
    now = dt.now()
    if reason == "r_id":
        ans = f"&random_id={now:%y%m%d%H%M%S%f}"
    elif reason == "id":
        ans = f"{now:%y%m%d%H%M%S%f}"
    elif reason == "report":
        ans = f"{now:%y_%m_%d-%H_%M_%S}"
    else:
        ans = "FUCK OFF"
    return ans