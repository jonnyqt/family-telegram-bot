from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой семейный бот!")

# Создаем приложение
app = ApplicationBuilder().token("ВАШ_ТОКЕН_ТЕЛЕГРАМ").build()

# Регистрируем обработчик
app.add_handler(CommandHandler("start", start))

# Запуск бота
app.run_polling()
