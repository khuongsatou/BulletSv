from api.models import Note
from api.src.utils.time_line_util import get_time
from django.db.models import Q


def store(data, context, time_start):
    # tìm vị trí bắt đầu và kết thúc
    limit = data['limit']
    page = data['page']
    start = (page - 1) * limit
    to = (page * limit)
    if len(data['search']) > 0:
        # có sắp xếp hay không (-) là sắp xếp giảm dần
        order_by = "" if data['order_by'] == "asc" else "-"

        query_1 = Q(status="1",
                    id_user=data['user_id'],
                    id__contains=data['search'])

        query_2 = Q(status="1",
                    id_user=data['user_id'],
                    name__contains=data['search'])

        # Thực hiện select
        s = Note.objects.all().filter(query_1 | query_2).order_by(
            order_by + 'id')[
            start: to]
        c = s.count()
    else:
        # có sắp xếp hay không (-) là sắp xếp giảm dần
        order_by = "" if data['order_by'] == "asc" else "-"

        # Thực hiện select
        s = Note.objects.all().filter(status="1", id_user=data['user_id']).order_by(
            order_by + 'id')[
            start: to]
        c = Note.objects.filter(status="1", id_user=data['user_id']).count()

    # Nếu có dư thì thêm 1 page
    data['number_page'] = int(c / limit) + (0 if c % limit == 0 else 1)
    data['store'] = list(s.values())
    data['total_count'] = c
    index = []
    active = []
    for i in range(data['number_page']):
        index.append(i + 1)
        if page == (i + 1):
            active.append(True)
        else:
            active.append(False)
    data["records"] = index
    data["active"] = active
    data["timer_select"] = get_time("timer_select", time_start)
    return data
