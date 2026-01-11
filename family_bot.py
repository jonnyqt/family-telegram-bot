from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Асинхронная функция-обработчик
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой семейный бот!")

# Создаем приложение бота
app = ApplicationBuilder().token("ВАШ_ТОКЕН").build()

# Регистрируем обработчик команды /start
app.add_handler(CommandHandler("start", start))

# Запуск бота
app.run_polling()
