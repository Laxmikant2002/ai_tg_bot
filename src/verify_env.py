import os

def verify_environment_variables():
    telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    database_url = os.getenv("DATABASE_URL")
    debug = os.getenv("DEBUG")

    print(f"TELEGRAM_BOT_TOKEN: {telegram_bot_token}")
    print(f"OPENAI_API_KEY: {openai_api_key}")
    print(f"DATABASE_URL: {database_url}")
    print(f"DEBUG: {debug}")

if __name__ == '__main__':
    verify_environment_variables()