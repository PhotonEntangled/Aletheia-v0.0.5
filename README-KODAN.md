# KODAN 🚀
**Knowledge Omni-Directional Discovery And Navigation**

[![Deploy Status](https://github.com/PhotonEntangled/kodan/actions/workflows/deploy.yml/badge.svg)](https://github.com/PhotonEntangled/kodan/actions/workflows/deploy.yml)

> Self-hosted AI assistant based on Khoj v2.0.0-beta.13 with enhanced Telegram bot integration, n8n automation, and production-ready Dokploy deployment.

## 🎯 What is KODAN?

KODAN is your personal AI second brain that extends Khoj's capabilities with:

- 🤖 **Telegram Bot Integration** - Chat with your AI directly in Telegram
- 🔄 **n8n Automation Platform** - Create powerful AI-driven workflows  
- 🚀 **Production Deployment** - Ready-to-deploy with Dokploy on VPS
- 🔍 **Research Mode** - Advanced AI research with `/research` command
- 🎭 **Custom Agents** - Create specialized AI agents for different tasks
- 🌐 **Self-Hosted** - Complete control over your data and AI

## 🏗️ Architecture

```
Telegram Bot ↔ n8n.kodan.space ↔ n8n Container ↔ KODAN Container
                                                      ↕
                                               PostgreSQL + pgvector
```

## 🚀 Quick Start

### Prerequisites
- VPS with Docker and Dokploy installed
- Domain name (e.g., `kodan.space`)
- OpenRouter API key for AI models

### 1. Clone and Configure
```bash
git clone https://github.com/PhotonEntangled/kodan.git
cd kodan
cp production.env.example production.env
# Edit production.env with your settings
```

### 2. Deploy with Dokploy
1. Upload `docker-compose.production.yml` to Dokploy
2. Configure domain routing:
   - `kodan.space` → server service (port 42110)
   - `n8n.kodan.space` → n8n service (port 5678)
3. Deploy and enjoy!

## 🤖 Telegram Bot Setup

1. Create bot with [@BotFather](https://t.me/botfather)
2. Get your bot token
3. Configure webhook in n8n pointing to KODAN API
4. Start chatting with your AI assistant!

## 🔧 Configuration

### Environment Variables
Key settings in `production.env`:
- `KHOJ_DOMAIN=kodan.space` - Your domain
- `OPENAI_API_KEY=sk-or-v1-...` - OpenRouter API key  
- `KHOJ_DEFAULT_CHAT_MODEL=google/gemini-2.5-pro-latest` - AI model
- `WEBHOOK_URL=https://n8n.kodan.space` - n8n webhook URL

### Docker Services
- **KODAN Server** - Main AI backend (port 42110)
- **n8n** - Automation platform (port 5678)
- **PostgreSQL** - Database with pgvector
- **SearXNG** - Private search engine
- **Terrarium** - Code execution sandbox

## ✨ Features

### 🔍 Research Mode
Start any message with `/research` for enhanced AI research capabilities.

### 🎭 Custom Agents
Create specialized AI agents with custom:
- Personality and behavior
- Knowledge bases
- Available tools and capabilities

### 🔄 Automation
Use n8n to create workflows that:
- Process Telegram messages
- Trigger KODAN research
- Send notifications
- Integrate with other services

## 🛠️ Development

### Local Setup
```bash
git checkout kodan-v2-development
pip install -r requirements.txt
docker-compose up -d database
python src/khoj/main.py --host="0.0.0.0" --port=42110
```

### Testing
```bash
pytest tests/
```

## 🚀 CI/CD Pipeline

Automated deployment on push to `kodan-v2-development`:
1. **Test** - Run automated tests
2. **Build** - Create Docker images
3. **Deploy** - Update production via SSH

Configure these secrets in GitHub:
- `HOST` - Your VPS IP address
- `USERNAME` - SSH username
- `SSH_KEY` - Private SSH key

## 📊 Tech Stack

- **Backend**: Python, FastAPI, Django
- **Database**: PostgreSQL + pgvector
- **Frontend**: Next.js, TypeScript, React
- **Deployment**: Docker, Dokploy, Traefik
- **Automation**: n8n workflow platform
- **AI**: OpenRouter, Gemini, GPT, Claude

## 🔒 Security

- Private GitHub repository
- Environment variables for secrets
- SSH key authentication
- HTTPS with Let's Encrypt
- API key rotation support

## 📈 Monitoring

- Docker health checks
- Automated backups
- Log aggregation
- Performance metrics
- Uptime monitoring

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

Based on [Khoj](https://github.com/khoj-ai/khoj) - AGPL-3.0 License

## 🙏 Acknowledgments

- [Khoj AI](https://khoj.dev) - The foundation of KODAN
- [n8n](https://n8n.io) - Workflow automation
- [Dokploy](https://dokploy.com) - Deployment platform

---

**KODAN** - Your AI-powered knowledge navigation system 🧠✨
