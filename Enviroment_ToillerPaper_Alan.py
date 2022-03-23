import numpy as np

class ToilletPaperEnv():

    def __init__(self, price , 
        tpnumber,max_capacity) -> None:
        
        self.price = price
        self.TPNumber = tpnumber
        self.max_capacity = max_capacity
        self.clock = 0
        self.conta = 0

    def initial_percepts(self) -> dict[float,int,int,float]:

        self.percepts = {'price':self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity':self.max_capacity,
                    'conta': self.conta}
        return self.percepts

    def change_state(self,action) -> None:

        self.TPNumber += int(action)

        self.conta -= self.price * int(action)

        self.conta += 10000 + np.random.randn()*5000
        if self.conta<0:
            self.conta = self.conta*(-1)

        self.usage = 1000 + int(np.random.randn()*100)

        if(self.usage > 0 and self.usage<self.TPNumber):
            self.TPNumber -= self.usage
        elif(self.TPNumber>1000):
            self.TPNumber -= 1000
        else:
            self.TPNumber = 0

        self.price = 10 + self.clock*0.01 + 0.5 + np.random.randn() * 0.1

        self.percepts = {'price':self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity': self.max_capacity,
                    'conta': self.conta}
        

        self.clock += 1
