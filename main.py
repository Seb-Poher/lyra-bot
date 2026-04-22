import telebot
import os

print("DEBUG ENV KEYS:", [k for k in os.environ.keys() if "TELEGRAM" in k or "TOKEN" in k])

telegram_api_key = (
    os.getenv("TELEGRAM_BOT_TOKEN")
    or os.getenv("BOT_TOKEN")
    or os.getenv("TOKEN")
)

if not telegram_api_key:
    raise ValueError("Aucune variable de token trouvée. Vérifie Railway Variables.")

bot = telebot.TeleBot(telegram_api_key)
 
WELCOME_MESSAGE = """Bienvenue dans le BDA Club 🔥
(Business • Développement • Action)

Tu es ici pour une seule raison :
👉 avancer concrètement dans ton business.

🎯 Ce que tu vas trouver ici
Un environnement pensé pour passer à l’action :

•  🤝 Des connexions entre entrepreneurs
•  ⚡️ De l’entraide concrète
•  🔥 Des partages de résultats
•  🧠 Des méthodes et ressources utiles
•  💰 Des opportunités business

🧭 Par où commencer (IMPORTANT)

👉 Étape 1 : Présente-toi ici → #Présentations & Discussions
(Qui tu es, ce que tu fais, ce que tu cherches)
👉 Étape 2 : Va voir les opportunités → #Connexions & Matching
👉 Étape 3 : Pose une question → #Entraide
👉 Étape 4 : Passe à l’action → puis partage ta win → #Wins & Partages


⚠️ Règle simple du club
Ici, on ne reste pas spectateur.

👉 Tu avances
👉 Tu testes
👉 Tu partages

C’est comme ça que tu progresses.
C’est comme ça que les autres progressent.

🏛 Le + du BDA Club
Tu as accès à un QG interactif (espace immersif) pour :

•  networking en live
•  sessions d’entraide
•  coworking
•  événements
👉 Les infos sont dans #Annonces


🔥 Maintenant, à toi de jouer

Commence par te présenter 👇
Puis passe à l’action."""


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, WELCOME_MESSAGE)


@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_members(message):
    bot.send_message(message.chat.id, WELCOME_MESSAGE)


@bot.message_handler(content_types=['left_chat_member'])
def goodbye_member(message):
    first_name = message.left_chat_member.first_name
    bot.send_message(
        message.chat.id,
        f"👋 {first_name},  Joie d'avoir fait ta connaissance ! 🤝"
    )


print("Bot lancé...")
bot.infinity_polling()