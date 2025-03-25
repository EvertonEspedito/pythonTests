import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        self.detalhes(f"Saque de {valor} realizado com sucesso!")        

    def depositar( self, valor:float) -> float:
        self.saldo+=valor
        self.detalhes(f"Deósito de {valor} realizado com sucesso!")
        return self.saldo
    
    def detalhes(self, msg: str='') -> None:
        print(f"{msg}\n- Sua a Agência é: {self.agencia}\n- O número da sua conta é: {self.conta}\n- Seu saldo é: {self.saldo}")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r} {self.conta!r} {self.saldo!r})'
        return f'{class_name}{attrs}'          

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"Saque de {valor} realizado com sucesso!") 
        else:
            self.detalhes(f"Saque de {valor} não realizado, pois não há saldo suficiente!")

class ContaCorrent(Conta):
    def __init__(self, agencia: int, conta:int , saldo:float=0 , limite:float=0):
        super().__init__(agencia, conta , saldo )
        self.limite = limite

    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f"Saque de {valor} realizado com sucesso!\n-Seu Limite é {limite_maximo}") 
            
        else:
            self.detalhes(f"Saque de {valor} não realizado, pois não há saldo suficiente!\n- Seu limite é {limite_maximo}")    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r} {self.conta!r} {self.saldo!r} {self.limite!r})'
        return f'{class_name}{attrs}'                     