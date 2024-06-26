# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
  def __init__(self, nome, numero, plano):
    self.nome = nome
    self.numero = numero
    self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
  def fazer_chamada(self, destinatario, duracao):
    
# TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
    custo = self.plano.custo_chamada(duracao)
    saldo = self.plano.verificar_saldo()
        # TODO: Verifique se o saldo do plano é suficiente para a chamada.
    if saldo < custo:
        return "Saldo insuficiente para fazer a chamada."
# TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
    else:
        saldo_final = self.plano.deduzir_saldo(custo)
# TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: {saldo_final:.2f}"

# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
  def __init__(self, saldo_inicial):
    self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:
  def verificar_saldo(self):
    return self.saldo
# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
  def custo_chamada(self, duracao):
    custo = duracao * 0.10
    return custo    
# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
  def deduzir_saldo(self, custo):
    self.saldo -= custo
    return self.saldo
# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input("nome: ")
numero = input("Numero: ")
saldo_inicial = float(input("saldo: "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("destinatário: ")
duracao = int(input("duracao: "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
