import json
import random

# Carregar os dados
with open("dados_filmes.json", "r", encoding="utf-8") as f:
    filmes = json.load(f)

print("🎬 Bem-vindo ao Chatbot Recomendador de Filmes!")
print("Me diga o que você está procurando hoje: ação, comédia, romance ou terror?")
genero = input("Você quer assistir um filme de que gênero? ").lower()

# Verificar gênero e recomendar filme
if genero in filmes:
    sugestao = random.choice(filmes[genero])
    print(f"\n📽️ Boa escolha! Eu recomendo: *{sugestao}*")
else:
    print("\n🤔 Desculpa, ainda não conheço esse gênero. Tente: ação, comédia, romance ou terror.")
