from random import choice

class Desenvolvedor:
    def __init__(self, linguagens_programacao=None):
        self.linguagens_programacao = linguagens_programacao
        print(f'Novo Desenvolvedor com expertise nas Linguagens:\n\t{self.linguagens_programacao}')

    def desenvolver_codigo(self):
        print(f'Pssssssiu! Estou codando em {choice(self.linguagens_programacao)}!')

class Gerente:
    def __init__(self, softskills=None):
        self.softskills = softskills
        print(f'Novo Gerente com habilidade nas SoftSkills:\n\t{self.softskills}')

    def gerenciar_equipe(self):
        print(f'Gerente está utilizando {choice(self.softskills)} para gerenciar sua equipe!')

class TechLead(Desenvolvedor, Gerente):
    def __init__(self, linguagens_programacao=None, softskills=None):
        # Chama o construtor da classe Desenvolvedor para inicializar as linguagens de programação
        Desenvolvedor.__init__(self, linguagens_programacao)
        # Chama o construtor da classe Gerente para inicializar as habilidades de soft skills
        Gerente.__init__(self, softskills)

# Instancia um TechLead com linguagens de programação e habilidades de soft skills
tech_lead = TechLead(['C', 'C++', 'Python'], ['Liderança', 'Comunicação Ativa', 'Feedbacks Positivos'])

# O TechLead executa métodos herdados das classes Desenvolvedor e Gerente
tech_lead.desenvolver_codigo()  # Chama o método de desenvolvimento de código do Desenvolvedor
tech_lead.gerenciar_equipe()    # Chama o método de gerenciamento de equipe do Gerente
