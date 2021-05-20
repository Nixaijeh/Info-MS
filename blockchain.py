from 实验一.basic import Base


class Block(Base):
    def __init__(self, prev_hash: str = None):
        self.items = []
        self.prev_hash = prev_hash

    def add(self, item):
        item.prev_hash = self.items[-1].hash() if len(self.items) else None
        self.items.append(item)

    def validate(self):
        for i in range(len(self.items)):
            assert i == 0 or self.items[i].prev_hash == self.items[i - 1].hash()


class Blockchain(Base):
    def __init__(self):
        self.blocks = []
        self.temp = 0

    def add(self, block):
        block.prev_hash = self.blocks[-1].hash() if len(self.blocks) else None
        self.blocks.append(block)

    def validate(self):
        for i in range(len(self.blocks)):
            assert i == 0 or self.blocks[i].prev_hash == self.blocks[i - 1].hash()
            self.blocks[i].validate()

class Ledger(Blockchain):
    def balance(self,uid):
        led=0
        for i in self.blocks:
            for j in i.items:
                if(uid == j.receiver):
                    led = led + j.amount
                if(uid == j.sender):
                    led = led - j.amount

        return led


    def add(self, block):
        self.blocks.append(block)
        block.prev_hash = self.blocks[-1].hash() if len(self.blocks) else None
        for j in block.items:
            bal= self.balance(j.sender)
            if(j.sender!='admin'):
                try:
                    assert (bal>=0)
                except:
                    self.temp=1
                    print(j.sender+"余额不足")
        if (self.temp==1):
            assert False


