import re

# Entrada do usuário
prompt_usuario = input()

# Função para verificar se o texto contém frases-chave
def verificar_frases(texto):
    frases_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia"]
    for frase in frases_chave:
        if re.search(frase, texto, re.IGNORECASE):
            return True
    return False

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém frases-chave relevantes
    if verificar_frases(prompt):
        return "O prompt está adequado."
    else:
        return "O prompt não está adequado. Inclua palavras-chave relevantes."

# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(prompt_usuario)

# Exibir feedback
print(feedback_usuario)