from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.mensagem = msg 
        
    @abstractmethod
    def enviar(self ) -> bool: ...
    
    
class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True
    
    
    
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False #false para exemplo
        
        
def notificar(notificacao: Notificacao):
    notificacao_enviada  = notificacao.enviar()
    
    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao Não enviada')
        
        
notificacao_email = NotificacaoEmail('testando Email')

notificar(notificacao_email)

notificacao_SMS = NotificacaoSMS('testando SMS')

notificar(notificacao_SMS)
