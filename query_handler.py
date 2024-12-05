# Basic query logic (you can replace this with AI-based logic later)
def handle_query(user_input):
    if "recommend" in user_input or "product" in user_input:
        return "Sure! What kind of product are you looking for?"
    elif "order status" in user_input:
        return "Please provide your order ID to check the status."
    elif "return" in user_input or "exchange" in user_input:
        return "You can return or exchange products within 30 days."
    elif "payment" in user_input:
        return "For payment issues, please check your card or try another method."
    elif "shipping" in user_input:
        return "Standard shipping takes 3-5 days."
    else:
        return "I'm not sure how to help with that. Could you rephrase?"
    




