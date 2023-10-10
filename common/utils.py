from common.consts import DateCategory, Status


def make_dict(to_dt: str = None, from_dt: str = None, date_category: DateCategory = None, status: Status = None, limit: int = 10, page: int = 1) -> dict:
    params: dict = {}
    if to_dt != None:
        params['to_dt'] = to_dt
    if from_dt != None:
        params['from_dt'] = from_dt
    if date_category != None:
        params['date_category'] = date_category
    if status != None:
        params['status'] = status
    if limit != None:
        params["limit"] = limit
    if page != None:
        params["page"] = page

    print("Paras", params)

    return params
