import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Переменные из Environment
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_KEY

# Проверка переменных (для отладки)
print("TELEGRAM_TOKEN =", TELEGRAM_TOKEN)
print("OPENAI_KEY =", OPENAI_KEY)

# Функция общения с OpenAI
async def ask_openai(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": text}],
            max_tokens=200
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Ошибка OpenAI: {e}"

# Команды бота
async def start(update: Update, context):
    await update.message.reply_text(
        "Привет! Я семейный бот 🤖\n"
        "Команды:\n"
        "/quiz — викторина\n"
        "/joke — шутка\n"
        "/translate текст — перевод\n"
        "/schedule — расписание"
    )

async def quiz(update: Update, context):
    reply = await ask_openai("Сделай короткую семейную викторину из 3 вопросов")
    await update.message.reply_text(reply)

async def joke(update: Update, context):
    reply = await ask_openai("Расскажи семейную шутку")
    await update.message.reply_text(reply)

async def translate(update: Update, context):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Напиши текст после команды")
        return
    reply = await ask_openai(f"Переведи на русский: {text}")
    await update.message.reply_text(reply)

schedule_data = [
    "Понедельник: школа 08:00",
    "Вторник: театр 18:30",
    "Среда: тренировка 17:00"
]

async def show_schedule(update: Update, context):
    await update.message.reply_text("\n".join(schedule_data))

async def chat(update: Update, context):
    reply = await ask_openai(update.message.text)
    await update.message.reply_text(reply)

# Настройка бота
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("joke", joke))
app.add_handler(CommandHandler("translate", translate))
app.add_handler(CommandHandler("schedule", show_schedule))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

app.run_polling()
