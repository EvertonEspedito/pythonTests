import contas
import pessoas

class Banco:
    def __init__(self,
        agencias: list[int] | None = None , 
        clientes: list[pessoas.Pessoas] | None =  None, 
        contas:list[contas.Conta] = None
    ):    
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            print(f'_checar_agencia',True)
            return True
        print(f'_checar_agencia',False)
        return False
    
    def _checar_cliente(self, cliente):
        if cliente in self.clientes:
            print(f'_checar_cliente',True)
            return True
        print(f'_checar_Cliente',False)
        return False
    
    def _checar_conta(self, conta):        
        if conta in self.contas:
            print(f'_checar_conta',True)
            return True
        print(f'_checar_conta',False)
        return False
    

    def _conta_e_do_cliente(self,cliente,conta):
        if conta is cliente.conta:
            print(f'_conta_e_do_cliente',True)
            return True
        print(f'_conta_e_do_cliente',False)
        return False    
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r} {self.clientes!r} {self.contas!r})'
        return f'{class_name}{attrs}'  
        
    def autenticar(self, cliente:pessoas.Pessoas, conta:contas.Conta):    
        return self._checar_agencia(conta) and self._checar_cliente(cliente) and self._checar_conta(conta) and self._conta_e_do_cliente(cliente,conta)