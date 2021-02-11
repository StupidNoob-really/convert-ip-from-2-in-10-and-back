class IP:
    def __init__(self, ip2="0.0.0.0", ip10="0.0.0.0"):
        self.ip2 = ip2.split('.')
        self.ip10 = ip10.split('.')
        if self.ip2 != ['0', '0', '0', '0']:
            self.convert_to10()
        if self.ip10 != ['0', '0', '0', '0']:
            self.convert_to2()

    def convert_to2(self):
        self.ip2.clear()
        point_number = 4
        for i in self.ip10:
            i = int(i)
            point_number = point_number - 1
            for x in range(8):
                if 2 ** (7 - x) <= i:
                    self.ip2.append('1')
                    i = i - 2 ** (7 - x)
                else:
                    self.ip2.append('0')
            if point_number != 0:
                self.ip2.append('.')
        s = ''
        s = s.join(self.ip2)
        self.ip2 = s.split('.')

    def convert_to10(self):
        self.ip10.clear()
        self.ip10 = [0] * 4
        e = int(0)
        for i in self.ip2:
            ch = 7
            for x in i:
                if x == '1':
                    self.ip10[e] = self.ip10[e] + 2 ** ch
                else:
                    pass
                ch = ch - 1
            self.ip10[e] = str(self.ip10[e])
            e = e + 1

    def print(self):
        i, p = '', ''
        point_number_i, point_number_p = 3, 3
        for ip2 in self.ip2:
            i = i + str(ip2)
            if point_number_i != 0:
                i = i + '.'
            point_number_i = point_number_i - 1
        for ip10 in self.ip10:
            p = p + str(ip10)
            if point_number_p != 0:
                p = p + '.'
            point_number_p = point_number_p - 1
        print(i)
        print(p)


if __name__ == "__main__":
    ip = input('Введите IP-адрес: ')
    print('Если в вести не верно то код посчитает не правильно')
    si = input('IP-адрес в двоичном коде?[Д/н]: ')
    flag = False
    for zn in ['Д', 'д', 'Y', 'y']:
        if si == zn:
            a = IP(ip2=ip)
            flag = True
    for zn in ['Н', 'н', 'N', 'n']:
        if si == zn:
            a = IP(ip10=ip)
            flag = True
    if flag:
        a.print()
