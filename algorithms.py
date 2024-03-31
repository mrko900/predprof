class Date:
    def __init__(self, data):
        self.data = data  # список списков кортежей

    def get_light_room(self):
        res = []
        for i in range(self.data.size()):
            for j in range(self.data[i].size()):
                if self.data[i][j][1] and not (self.data[i][j][0] in res):
                    res.append(self.data[i][j][0])
        return res

