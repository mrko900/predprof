def get_light_room(self):
    res = []
    for i in range(self.data.size()):
        for j in range(self.data[i].size()):
            if self.data[i][j][1] and not(self.data[i][j][0] in res):
                res.append(self.data[i][j][0])
    return res

def full_check_request(self, request):
    res = [True for i in range(request.size())]
    real_nums = get_light_room()
    for i in range(request.size()):
        res[i] = request[i] in real_nums
    return res

def check_request(self, request):
    res = True
    real_nums = get_light_room()
    for i in range(request.size()):
        res *= request[i] in real_nums
    return res
