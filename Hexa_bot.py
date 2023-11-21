import openai

# Assurez-vous d'avoir défini votre clé API
openai.api_key = 'VOTRE_CLE_API'

def chat_with_music_ai(user_input):
    # Appel de l'API GPT-3 avec l'entrée utilisateur
    response = openai.Completion.create(
        engine="text-davinci-002",  # Vous pouvez utiliser un autre moteur si nécessaire
        prompt=user_input,
        temperature=0.7,  # Contrôle la créativité de la réponse, ajustez selon vos besoins
        max_tokens=150  # Limite le nombre de tokens dans la réponse
    )

    # Récupérer la réponse générée par l'IA
    ai_response = response.choices[0].text.strip()

    return ai_response

# Boucle de conversation avec l'IA
while True:
    user_input = input("Vous: ")
    if user_input.lower() == 'exit':
        print("Au revoir!")
        break

    # Appel de la fonction de chat avec l'IA
    ai_response = chat_with_music_ai(user_input)
    print("IA: " + ai_response)