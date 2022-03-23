class ToilletPaperAg():

    def __init__(self,env) -> None:
        self.price_average = 0
        self.usage_average = 0
        self.clock = 0
        self.tobuy = 0
        self.current_percepts = env.initial_percepts()
        self.price = self.current_percepts['price']
        self.TPNumber = self.current_percepts['tpnumber']
        self.capacity = self.current_percepts['max_capacity']
        self.conta = self.current_percepts['conta']

    def act(self,env) -> int:
        tpnum_ant = self.TPNumber
        price_ant = self.price
        
        percepts = env.initial_percepts()
        self.price = percepts['price']
        self.TPNumber = percepts['tpnumber']
        self.capacity = percepts['max_capacity']
        self.conta = percepts['conta']

        print("Valor dispnível: R$" + str(self.conta))
        print("Número de rolos: " + str(self.TPNumber))

        self.clock += 1

        self.usage_average = (self.usage_average * (self.clock - 1) + (self.TPNumber - tpnum_ant))/self.clock
        
        self.price_average = (self.price_average * (self.clock - 1) + (self.price - price_ant))/self.clock
        
        if self.price<(0.9*self.price_average):
            if self.TPNumber < (0.6*self.capacity):         
                self.tobuy = self.capacity - self.TPNumber
        elif self.TPNumber < self.usage_average:
            if 2*self.usage_average < self.capacity:
                self.tobuy = 2*self.usage_average
            elif self.usage_average < self.capacity:
                self.tobuy = self.usage_average
            else:
                self.tobuy = self.capacity - self.TPNumber
        elif self.TPNumber < (0.1*self.capacity):
            self.tobuy = int(0.2*self.capacity)
        else:
            self.tobuy = 0
        
        if (self.tobuy * self.price) > self.conta:
            self.tobuy = int(self.conta/self.price)

        self.TPNumber += self.tobuy

        print("Qtde comprada: " + str(self.tobuy))
        print("Preço total: " + str(self.tobuy*self.price))
        
        return self.tobuy
