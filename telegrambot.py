from telegram import Update
from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes
from typing import Final
TOKEN: Final = '6536174087:AAEwIlEzyAUBBQ2pqR0tPuZjm5Jf958nhew'
Bot_username: Final = '@Sehnaiabot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('اهلا بكم في مدارس صحنايا الخاصة, شكرالاختياركم البوت هنا يمكنم ايجاد برنامج الدوام ومسائل رياضية للطلاب')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('يرجى اختيار الموضوع المناسب والاستمرار في الخيارات')

async def show_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('برنامج الدوام قيد التطوير')

async def solve_equation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    example = 'مثال: حل المعادلة التالية:\n\n2x^2 + 3x - 5 = 0\n\nالحل:\n\nx = 1.23 أو x = -2.04'
    await update.message.reply_text(example)

async def solve_derivative(update: Update, context: ContextTypes.DEFAULT_TYPE):
    example = 'مثال: حساب المشتقة للدالة التالية:\n\nf(x) = 3x^2 + 2x + 1\n\nالمشتقة:\n\nf\'(x) = 6x + 2'
    await update.message.reply_text(example)

async def solve_integration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    example = 'مثال: حساب التكامل للدالة التالية:\n\nf(x) = 2x^2 + 3x + 1\n\nالتكامل:\n\nF(x) = (2/3)x^3 + (3/2)x^2 + x + C'
    await update.message.reply_text(example)

async def solve_functions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    example = 'مثال: حل المسألة التالية عن دالة:\n\nf(x) = 2x^3 - 3x^2 + 4x - 1\n\nالحل:\n\nf(2) = 11'
    await update.message.reply_text(example)


async def ask_question1(update: Update, context: CallbackContext):
    question = "ما هي مساحة المربع؟"
    options = ["الطولXالعرض", "الطول+العرض", "ْ(الطول+العرض)2X", "الطول-العرض"]
    correct_option = "الطولXالعرض"

    # إرسال السؤال والخيارات للمستخدم
    question_text = f"{question}\n\n"
    for i, option in enumerate(options, start=1):
        question_text += f"{i}. {option}\n"
    await update.message.reply_text(question_text)

    # تلقي إجابة المستخدم
    user_answer = update.message.text

    # فحص الإجابة وإرسال رد مناسب
    if user_answer == correct_option:
        await update.message.reply_text("إجابة صحيحة!")
    else:
        await update.message.reply_text(f" الإجابة الصحيحة هي: {correct_option}")


async def ask_question2(update: Update, context: CallbackContext):
    question = "صح أم خطأ: المستقيمان المتقاطعان متوازيان."
    correct_option = "خطأ"

    # إرسال السؤال للمستخدم
    await update.message.reply_text(question)

    # تلقي إجابة المستخدم
    user_answer = update.message.text

    # فحص الإجابة وإرسال رد مناسب
    if user_answer == correct_option:
        await update.message.reply_text("إجابة صحيحة!")
    else:
        await update.message.reply_text(f" الإجابة الصحيحة هي: {correct_option}")


async def ask_question3(update: Update, context: CallbackContext):
    question = "صح أم خطأ: إذا ازداد المقام في الكسر، فإن القيمة تقل."
    correct_option = "صح"

    # إرسال السؤال للمستخدم
    await update.message.reply_text(question)

    # تلقي إجابة المستخدم
    user_answer = update.message.text

    # فحص الإجابة وإرسال رد مناسب
    if user_answer == correct_option:
        await update.message.reply_text("إجابة صحيحة!")
    else:
        await update.message.reply_text(f" الإجابة الصحيحة هي: {correct_option}")




if __name__ == '__main__':
    print("starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start_command ))
    app.add_handler(CommandHandler('help',help_command ))
    app.add_handler(CommandHandler('schedule',show_schedule ))
    app.add_handler(CommandHandler('equation',solve_equation ))
    app.add_handler(CommandHandler('derivative',solve_derivative ))
    app.add_handler(CommandHandler('integration',solve_integration ))
    app.add_handler(CommandHandler('functions',solve_functions ))
    app.add_handler(CommandHandler('question1',ask_question1))
    app.add_handler(CommandHandler('question2',ask_question2))
    app.add_handler(CommandHandler('question3',ask_question3))

    print("Polling...")
    app.run_polling(poll_interval=2)