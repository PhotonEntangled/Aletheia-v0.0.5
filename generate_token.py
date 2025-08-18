import os
import sys
import django
import asyncio
from pathlib import Path

# This function will run in a synchronous context
def generate_sync():
    from khoj.database.models import KhojUser
    from khoj.database.adapters import create_khoj_token

    async def get_user_and_token():
        admin_email = os.getenv("KHOJ_ADMIN_EMAIL")
        if not admin_email:
            print("Error: KHOJ_ADMIN_EMAIL environment variable is not set.", file=sys.stderr)
            return None

        user = await KhojUser.objects.filter(email=admin_email).afirst()
        if not user:
            print(f"Error: Admin user with email '{admin_email}' not found.", file=sys.stderr)
            return None

        token_name = "obsidian-plugin-key"
        api_user = await create_khoj_token(user, token_name)
        return user, api_user

    # Use asyncio.run() to execute the async part and get the result
    result = asyncio.run(get_user_and_token())

    if result:
        user, api_user = result
        print("\n" + "="*50)
        print("  KODAN API TOKEN SUCCESSFULLY GENERATED")
        print("="*50)
        print(f"  User: {user.email}")
        print(f"  Token Name: {api_user.name}")
        print(f"  Your API Key is: {api_user.token}")
        print("="*50)
        print("\nCopy the API Key and paste it into the 'Khoj API Key' field in your Obsidian plugin settings.")
        print(f"Set the 'Khoj URL' to: https://{os.getenv('KHOJ_DOMAIN', 'kodan.space')}\n")

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "khoj.app.settings")
    try:
        django.setup()
    except Exception as e:
        print(f"Error during Django setup: {e}", file=sys.stderr)
        sys.exit(1)

    # Now that Django is set up, run the synchronous function
    generate_sync()

if __name__ == "__main__":
    main()
