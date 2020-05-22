#classe para envio de email
class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalid(f'Formato de email inválido: {remetente}')
        return remetente


class EmailInvalid(Exception):
    pass
