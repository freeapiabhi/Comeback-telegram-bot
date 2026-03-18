import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8591440902:AAFFJWKGh5VqBVCltQfyvVG3ZQBaSCESSQg"

# Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome!\nCommands:\n/ip <ip>\n/pincode <code>\n/ifsc <code>")

# IP Info
async def ip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        ip = context.args[0]
        data = requests.get(f"http://ip-api.com/json/{ip}").json()

        msg = f"""
IP: {ip}
Country: {data.get('country')}
Region: {data.get('regionName')}
City: {data.get('city')}
ISP: {data.get('isp')}
        """
        await update.message.reply_text(msg)
    except:
        await update.message.reply_text("Usage: /ip 8.8.8.8")

# Pincode Info (India)
async def pincode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        code = context.args[0]
        data = requests.get(f"https://api.postalpincode.in/pincode/{code}").json()

        post = data[0]['PostOffice'][0]

        msg = f"""
Pincode: {code}
Area: {post['Name']}
District: {post['District']}
State: {post['State']}
        """
        await update.message.reply_text(msg)
    except:
        await update.message.reply_text("Usage: /pincode 110001")

# IFSC Info
async def ifsc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        code = context.args[0]
        data = requests.get(f"https://ifsc.razorpay.com/{code}").json()

        msg = f"""
Bank: {data.get('BANK')}
Branch: {data.get('BRANCH')}
City: {data.get('CITY')}
        """
        await update.message.reply_text(msg)
    except:
        await update.message.reply_text("Usage: /ifsc SBIN0000001")

# Main
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ip", ip))
app.add_handler(CommandHandler("pincode", pincode))
app.add_handler(CommandHandler("ifsc", ifsc))

app.run_polling()