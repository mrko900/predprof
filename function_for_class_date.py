def get_light_room(self, data):
    res = []
    for i in range(data.size()):
        for j in range(data[i].size()):
            if data[i][j][1] and not(data[i][j][0] in res):
                res.append(data[i][j][0])
    return res
