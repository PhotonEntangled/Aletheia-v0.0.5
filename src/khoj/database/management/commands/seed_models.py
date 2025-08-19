# src/khoj/database/management/commands/seed_models.py
# Seeds the database with default AI model configurations for development
# NOT FOR: Production use - this is only for local development setup

import os
from django.core.management.base import BaseCommand
from khoj.database.models import AiModelApi, ChatModel, TextToImageModelConfig, VoiceModelOption

class Command(BaseCommand):
    help = 'Seeds the database with default AI model configurations.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Apply the seeding to the database.',
        )

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding for AI models...")

        # === Seed OpenAI API Provider and DALL-E Models ===
        openai_key = os.environ.get("OPENAI_API_KEY")
        if openai_key:
            openai_provider, created = AiModelApi.objects.get_or_create(
                name="OpenAI",
                defaults={
                    "api_key": openai_key,
                    "api_base_url": os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created AiModelApi: {openai_provider.name}'))

            dalle3_data = {
                "model_name": "dall-e-3", "friendly_name": "DALL-E 3", 
                "model_type": TextToImageModelConfig.ModelType.OPENAI, "ai_model_api": openai_provider, "price_tier": "standard"
            }
            dalle2_data = {
                "model_name": "dall-e-2", "friendly_name": "DALL-E 2", 
                "model_type": TextToImageModelConfig.ModelType.OPENAI, "ai_model_api": openai_provider, "price_tier": "standard"
            }
            
            model, created = TextToImageModelConfig.objects.get_or_create(model_name="dall-e-3", defaults=dalle3_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created TextToImageModelConfig: {model.friendly_name}'))

            model, created = TextToImageModelConfig.objects.get_or_create(model_name="dall-e-2", defaults=dalle2_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created TextToImageModelConfig: {model.friendly_name}'))
        else:
            self.stdout.write(self.style.WARNING('OPENAI_API_KEY not found. Skipping DALL-E model seeding.'))

        # === Seed Voice Models ===
        voice_models = [
            {"model_id": "eleven_multilingual_v2", "name": "Eleven Multilingual v2", "price_tier": "standard"},
            {"model_id": "eleven_turbo_v2", "name": "Eleven Turbo v2", "price_tier": "standard"},
            {"model_id": "eleven_monolingual_v1", "name": "Eleven English v1", "price_tier": "standard"},
            {"model_id": "eleven_multilingual_v1", "name": "Eleven Multilingual v1", "price_tier": "standard"},
        ]

        for voice_data in voice_models:
            model, created = VoiceModelOption.objects.get_or_create(model_id=voice_data["model_id"], defaults=voice_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created VoiceModelOption: {model.name}'))
        
        # === Seed Default Chat Model ===
        google_api, created = AiModelApi.objects.get_or_create(name="Google")
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created AiModelApi: {google_api.name}'))

        chat_model_data = {
            "name": "google/gemini-2.5-pro-latest", "friendly_name": "Gemini 2.5 Pro",
            "model_type": ChatModel.ModelType.GOOGLE, "price_tier": "standard", "vision_enabled": True, "ai_model_api": google_api
        }
        model, created = ChatModel.objects.get_or_create(name="google/gemini-2.5-pro-latest", defaults=chat_model_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created ChatModel: {model.friendly_name}'))
        
        if not options['apply']:
            self.stdout.write(self.style.WARNING("\nThis was a dry run. No changes were saved to the database."))
            self.stdout.write("Run the command with the --apply flag to save these changes.")
        else:
            self.stdout.write(self.style.SUCCESS("\nDatabase seeding complete. Changes have been applied."))
