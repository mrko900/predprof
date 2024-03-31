import request_funcs


def parse_date(rooms_count, windows_for_room, floors):
    data = []
    floors_count = len(floors)
    room = 0
    for fl in range(floors_count):
        data.append([])
        roomi = 0
        cur_rooms = 0
        room += 1
        for wnd in floors[fl]:
            cur_rooms += 1
            if cur_rooms > windows_for_room[roomi]:
                roomi += 1
                cur_rooms = 0
                room += 1
            data[-1].append((room, wnd))
    return Date(data)


class Dates:
    def __init__(self):
        self.dates = {}

    def add(self, dmy, date):
        self.dates[dmy] = date


class Date:
    def __init__(self, data):
        self.data = data  # список списков кортежей
        self.rooms = 0
        prev_room = -1
        for fl in data:
            for wnd in fl:
                if wnd[0] != prev_room:
                    prev_room = wnd[0]
                    self.rooms += 1

    def get_light_room(self):
        res = []
        for i in range(self.data.size()):
            for j in range(self.data[i].size()):
                if self.data[i][j][1] and not (self.data[i][j][0] in res):
                    res.append(self.data[i][j][0])
        return res

    def full_check_request(self, request):
        res = [True for i in range(request.size())]
        real_nums = self.get_light_room()
        for i in range(request.size()):
            res[i] = request[i] in real_nums
        return res

    def check_request(self, request):
        res = True
        real_nums = self.get_light_room()
        for i in range(request.size()):
            res *= request[i] in real_nums
        return res


dates = Dates()
dates_raw = request_funcs.get_data_about_all_days()
for k, v in dates_raw.items():
    dates.add(k, parse_date(v[0], v[1], v[2]))
