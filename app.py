from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# simple memory storage
chat_memory = {}

def get_reply(msg):
    msg = msg.lower()

    # greetings
    if any(x in msg for x in ["hi", "hello", "hey"]):
        return "Hello 👋 Welcome to Smart Support. How can I help you today?"

    elif "how are you" in msg:
        return "😊 I'm doing great! How can I assist you today?"

    elif "your name" in msg:
        return "🤖 I'm Smart Support Assistant."

    elif "what can you do" in msg:
        return "I can help with orders, refunds, cancellations, delivery updates, and general queries."
    #technical questions
    
    elif "java" in msg:
        return "☕ Java is a powerful programming language used in web, mobile, and enterprise applications."

    elif "python" in msg:
        return "🐍 Python is an easy and powerful language used in AI, web development, and automation."

    elif "oops" in msg or "oop" in msg:
        return "📘 OOP stands for Object-Oriented Programming. It includes concepts like class, object, inheritance, and encapsulation."
    
        # 🍔 FOOD QUESTIONS
    elif " food" in msg or "I am feeling hungry" in msg:
        return "🍔 I recommend something light like sandwiches or dosa. What do you like?"

    elif "biryani" in msg:
        return "🍗 Biryani is always a great choice 😋 Hyderabadi biryani is famous!"

    elif "healthy food" in msg:
        return "🥗 You can try fruits, salads, boiled eggs, and home-cooked meals."

    elif "breakfast" in msg:
        return "🍳 Idli, dosa, poha, or oats are great breakfast options."
        # 🟢 CUSTOMER SERVICE & SUPPORT
    elif "business hours" in msg or "working hours" in msg:
        return "🕒 Our business hours are 9 AM to 6 PM, Monday to Saturday."

    elif "contact support" in msg or "how can i contact" in msg:
        return "📞 You can contact support via email at support@example.com or call 9876543210."

    elif "where is my order" in msg:
        return "📦 Please share your order ID so I can check the status."

    elif "return policy" in msg or "refund policy" in msg:
        return "🔁 We have a 7-day return policy for unused products."

    elif "reset my password" in msg:
        return "🔐 Use the 'Forgot Password' option on the login page."

    # 🟢 PRODUCT & SERVICE INFORMATION
    elif "services" in msg or "products do you offer" in msg:
        return "🛍️ We offer a wide range of products including electronics, clothing, and accessories."

    elif "cost" in msg or "price" in msg:
        return "💰 Prices vary by product. Please specify the item."

    elif "stock" in msg:
        return "📦 Most items are in stock. Please tell the product name."

    elif "shipping options" in msg:
        return "🚚 We offer standard (3–5 days) and express (1–2 days) shipping."

    # 🟢 TECHNICAL & GENERAL ASSISTANCE
    elif "human" in msg or "real person" in msg:
        return "👨‍💻 Sure! I can connect you to a human support agent."

    elif "how do i use" in msg:
        return "📘 Please check our user guide section or tell me what you need help with."

    elif "location" in msg or "service area" in msg:
        return "📍 We provide services across India."

    elif "error" in msg:
        return "⚠️ Please describe the error or share a screenshot for help."

    # 🟢 GENERAL AI QUESTIONS
    elif "weather" in msg:
        return "🌤️ I can't check live weather now, but you can use Google Weather."

    elif "joke" in msg:
        return "😂 Why did the computer show up late? Because it had a hard drive!"

    elif "story" in msg:
        return "📖 Once upon a time, a developer solved all bugs with patience 😄"

    elif "summarize" in msg:
        return "📝 Please paste the text. I will summarize it."

    elif "draft email" in msg:
        return "✉️ Sure! Tell me topic and I will draft an email."

    # ✈️ TRAVEL QUESTIONS
    elif "travel" in msg:
        return "✈️ Traveling is refreshing! Do you prefer beaches, hills, or cities?"

    elif "best place" in msg or "tourist" in msg:
        return "🌍 Goa, Ooty, Manali, and Kerala are very popular travel destinations."

    elif "budget travel" in msg:
        return "💸 Book early tickets and use public transport to save money."

    elif "solo travel" in msg:
        return "🎒 Solo travel is great! Just stay safe and plan properly."

    # 📚 STUDIES QUESTIONS
    elif "study" in msg or "studies" in msg:
        return "📚 Make a daily schedule and revise regularly for better results."

    elif "exam" in msg:
        return "📝 Practice previous papers and focus on important topics."

    elif "concentrate" in msg:
        return "🎯 Try Pomodoro technique and avoid mobile distractions."

    elif "motivation" in msg:
        return "🔥 Stay consistent and remember your goals!"

    # 💬 DAILY LIFE QUESTIONS
    elif "weather" in msg:
        return "🌤️ I hope it's a pleasant day! Stay hydrated."

    elif "time" in msg:
        return "⏰ Please check your system clock 😊"

    elif "joke" in msg:
        return "😂 Why do programmers prefer dark mode? Because light attracts bugs!"

    elif "movie" in msg:
        return "🎬 I suggest watching a good comedy or thriller."

    elif "music" in msg:
        return "🎧 Music is great for relaxing. What genre do you like?"

    # order flow
    elif "order" in msg:
        chat_memory["context"] = "order"
        return "📦 Sure! Please share your order ID."

    elif chat_memory.get("context") == "order":
        chat_memory["context"] = ""
        return f"✅ Thanks! I checked order {msg.upper()} — it's on the way 🚚"

    elif "track" in msg:
        return "📍 You can track your order using the tracking link sent to your email."

    elif "delivery" in msg:
        return "🚚 Delivery usually takes 3–5 working days."

    elif "delay" in msg or "late" in msg:
        return "⏳ Sorry for delay. We are checking with the delivery partner."

    # payment/refund
    elif "refund" in msg:
        return "💰 Refund takes 5–7 working days after approval."

    elif "payment" in msg:
        return "💳 We accept UPI, debit card, credit card, and net banking."

    # cancel flow
    elif "cancel" in msg:
        return "❌ Please share your order ID to cancel your order."

    # account/help
    elif "login" in msg:
        return "🔐 Please reset your password using the 'Forgot Password' option."

    elif "help" in msg:
        return "🙂 Sure! Please tell me your issue. I'm here to help."

    # goodbye
    elif "bye" in msg or "thank" in msg:
        return "👋 Thank you for contacting Smart Support!"

    # default reply
    else:
        return "🤖 I understand. Could you please explain a bit more?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_reply(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)