import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config


class IP:
    def __init__(self, ip_address):
        x = 0
        for ip in ip_address:
            x = x+1
            if not ip:
                self.IP = None
            elif x == 4:
                self.IP = Parser(self.manual(ip_address))
                self.IP = self.IP.feed_back()

    @staticmethod
    def manual(ip_address):
        return ip_address


class Parser:
    def __init__(self, ip_address=None):
        self.ip_address = ip_address
        self.ip_address = Core(ip_address=self.verification())
        self.ip_address = self.ip_address.feed_back()

    def verification(self):
        ip_address = self.ip_address
        if ip_address == ['']:
            return 'IP-адрес не введён'
        try:
            ttl = 4  # Time to live
            for numeral in ip_address:
                numeral = int(numeral)
                ttl = ttl - 1
                if 0 <= numeral <= 255:
                    if ttl == 0:
                        self.ip_address = ip_address
                        return {10: ip_address,
                                2: None}
                else:
                    raise ValueError
        except ValueError:
            return self.super_verification(ip_address=ip_address)
        except TypeError:
            return self.super_verification(ip_address=ip_address)

    def super_verification(self, ip_address):
        for str_numeral in ip_address:
            if len(str_numeral) != 8:
                return 'Error 1'
            else:
                for char in str_numeral:
                    if char != '0' and char != '1':
                        return f'Error 2 with char = {char}'
                self.ip_address = ip_address
                return {10: None,
                        2: ip_address}

    def feed_back(self):
        return self.ip_address


class Core:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def converter(self, ip_address):
        if not ip_address[2]:
            return self.convert_to_2(ip_address)
        elif not ip_address[10]:
            return self.convert_to_10(ip_address)

    @staticmethod
    def convert_to_10(ip_address):
        numbers = 0
        ip_address[10] = [0] * 4
        for octaves in ip_address[2]:
            power = 0
            for char in octaves:
                if char == '1':
                    ip_address[10][numbers] = ip_address[10][numbers] + 2 ** (7 - power)
                power = power + 1
            numbers = numbers + 1
        return ip_address

    @staticmethod
    def convert_to_2(ip_address):
        numbers = 0
        ip_address[2] = [''] * 4
        for octaves in ip_address[10]:
            octaves = int(octaves)
            for power in range(8):
                if octaves >= 2 ** (7 - power):
                    ip_address[2][numbers] = ip_address[2][numbers] + '1'
                    octaves = octaves - 2 ** (7 - power)
                else:
                    ip_address[2][numbers] = ip_address[2][numbers] + '0'
            numbers = numbers + 1
        return ip_address

    def feed_back(self):
        return self.converter(ip_address=self.ip_address)


class MyGrid(Widget):
    def clear(self):
        self.one_text.text = ''
        self.two_text.text = ''
        self.three_text.text = ''
        self.four_text.text = ''

    def convert(self):
        ip_address = [None]*4
        ip_address[0] = self.one_text.text
        ip_address[1] = self.two_text.text
        ip_address[2] = self.three_text.text
        ip_address[3] = self.four_text.text
        a = IP(ip_address)
        if a.IP:
            string = str(a.IP[10][0])+'.'+str(a.IP[10][1])+'.'+str(a.IP[10][2])+'.'+str(a.IP[10][3])+'\n'
            string = string + a.IP[2][0]+'.'+a.IP[2][1]+'.'+a.IP[2][2]+'.'+a.IP[2][3]
        else:
            string = str(a.IP)
        self.output_text.text = string


class InterfaceApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    POINT = '.'
    kivy.require('2.0.0')
    Config.set('graphics', 'resizable', 0)
    Window.size = (1080//2.25, 1920//2.25)
    InterfaceApp().run()
