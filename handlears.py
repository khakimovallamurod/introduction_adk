from telegram import Update
from telegram.ext import CallbackContext
from multi_tool_agent.agent import root_agent  

# start funktsiyasini asinxron qilib qayta yozing
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(
        text=f"Assalomu aleykum {user.full_name}! Men shahardagi vaqt va ob-havo haqida ma'lumot beruvchi botman.\n"
        "Shunchaki shahar(🌆) nomini yuboring!"
    )

# handle_message ni asinxron qilib yozish
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    print(dir(root_agent)) 
    result = root_agent.run_live(user_message)

    if isinstance(result, dict):
        if result.get("status") == "success":
            reply_text = result["report"]
        else:
            reply_text = result.get("error_message", "Xatolik yuz berdi.")
    else:
        reply_text = str(result)
    
    await update.message.reply_text(reply_text)
