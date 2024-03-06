class CustomError(Exception):
    def init(self, mensagem):
        super().init(mensagem)
        self.mensagem = mensagem
