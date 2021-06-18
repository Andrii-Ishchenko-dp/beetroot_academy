CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self,channels):
        self.channels = channels
        self.current_channel = self.channels[0]

    def first_channel(self):
        self.current_channel = self.channels[0]
        print(self.channels[0])

    def last_channel (self):
        self.current_channel = self.channels[-1]
        print(self.channels[-1])

    def turn_channel(self,n):
        self.current_channel = self.channels[n-1]
        print(self.channels[n-1])

    def next_channel(self):
        if self.current_channel == self.channels[-1]:
            self.current_channel = self.channels[0]
            print(self.current_channel)
        else:
            n = self.channels.index(self.current_channel)
            self.current_channel = self.channels[n+1]
            print(self.current_channel)

    def previous_channel (self):
        if self.current_channel == self.channels[0]:
            self.current_channel = self.channels[0]
            print(self.current_channel)
        else:
            n = self.channels.index(self.current_channel)
            self.current_channel = self.channels[n-1]
            print(self.current_channel)

    def cur_channel(self):
        print(self.current_channel)


    def is_exist(self,channel):
        try:
            if channel in self.channels or self.channels[channel] in self.channels:
                print('YES!')
            else:
                print('NO!')
        except IndexError:
            print('NO')

controller = TVController(CHANNELS)
controller.first_channel()

controller.last_channel()

controller.turn_channel(1)

controller.next_channel()

controller.previous_channel()

controller.cur_channel()

controller.is_exist(4)

controller.is_exist("BBC")