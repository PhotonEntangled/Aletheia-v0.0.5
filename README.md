# ALETHEIA 🚀
**Agentic Learning Engine for Transformative, Holistic Exploration and Intelligent Analysis**

[![Deploy Status](https://github.com/PhotonEntangled/kodan/actions/workflows/deploy.yml/badge.svg)](https://github.com/PhotonEntangled/kodan/actions/workflows/deploy.yml)
[![discord](https://img.shields.io/discord/1112065956647284756?style=plastic&label=discord)](https://discord.gg/BDgyabRM6e)

> Self-hosted AI assistant based on Khoj v2.0.0-beta.13 with enhanced Telegram bot integration, n8n automation, and production-ready Dokploy deployment.

## 🎯 What is ALETHEIA?

ALETHEIA is your personal AI second brain that extends the capabilities of [Khoj](https://khoj.dev) with a focus on robust, self-hosted deployment and automation. It smoothly scales up from an on-device personal AI to a cloud-scale enterprise AI.

- 🤖 **Telegram Bot Integration** - Chat with your AI directly in Telegram.
- 🔄 **n8n Automation Platform** - Create powerful AI-driven workflows.
- 🚀 **Production Deployment** - Ready-to-deploy with Dokploy on your own VPS.
- 🔍 **Research Mode** - Start any message with `/research` for enhanced AI research capabilities.
- 🎭 **Custom Agents** - Create specialized AI agents for different tasks with tunable personality, tools, and knowledge bases.
- 🌐 **Self-Hosted** - Retain complete control over your data and AI.
- 💬 **Chat with any LLM** - Supports local and online models (e.g., Llama 3, Qwen, Gemma, Mistral, GPT, Claude, Gemini, DeepSeek).
- 📄 **Knowledge Retrieval** - Get answers from the internet and your documents (including images, PDFs, Markdown, Org-mode, Word, Notion).
- 🖼️ **Image Generation** - Generate images directly from your chat.

## 🏗️ Architecture

```
Telegram Bot ↔ n8n.kodan.space ↔ n8n Container ↔ ALETHEIA Container
                                                      ↕
                                               PostgreSQL + pgvector
```

## ✨ See it in action

![demo_chat](https://github.com/khoj-ai/khoj/blob/master/documentation/assets/img/quadratic_equation_khoj_web.gif?raw=true)

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
1. Upload `docker-compose.production.yml` to Dokploy.
2. Configure domain routing:
   - `kodan.space` → server service (port 42110)
   - `n8n.kodan.space` → n8n service (port 5678)
3. Deploy and enjoy!

## 🤖 Telegram Bot Setup

1. Create a bot with [@BotFather](https://t.me/botfather).
2. Get your bot token.
3. Configure a webhook in your n8n instance pointing to the ALETHEIA API endpoint.
4. Start chatting with your new AI assistant!

## 🔧 Configuration

### Environment Variables
Key settings in `production.env`:
- `KHOJ_DOMAIN=kodan.space` - Your domain
- `OPENAI_API_KEY=sk-or-v1-...` - Your OpenRouter API key
- `KHOJ_DEFAULT_CHAT_MODEL=google/gemini-2.5-pro-latest` - Your preferred AI model
- `WEBHOOK_URL=https://n8n.kodan.space` - Your n8n webhook URL

### Docker Services
- **ALETHEIA Server** - Main AI backend (port 42110)
- **n8n** - Automation platform (port 5678)
- **PostgreSQL** - Database with pgvector for vector search
- **SearXNG** - Private, metasearch engine
- **Terrarium** - Code execution sandbox

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

The repository is configured for automated deployment on push to the `kodan-v2-development` branch. The workflow will:
1. **Test** - Run automated tests.
2. **Build** - Create Docker images.
3. **Deploy** - Update the production environment via SSH.

Configure these secrets in your GitHub repository settings for the pipeline to work:
- `HOST` - Your VPS IP address
- `USERNAME` - SSH username
- `SSH_KEY` - Private SSH key for server access

## 📊 Tech Stack

- **Backend**: Python, FastAPI, Django
- **Database**: PostgreSQL + pgvector
- **Frontend**: Next.js, TypeScript, React
- **Deployment**: Docker, Dokploy, Traefik
- **Automation**: n8n workflow platform
- **AI**: OpenRouter (for models like Gemini, GPT, Claude)

## 🤝 Contributing

This project is a fork and contributions specific to ALETHEIA are welcome.
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

For general contributions to the underlying platform, please see the original [Khoj Contributing Guidelines](https://docs.khoj.dev/contributing/development).

## 📄 License

Based on [Khoj](https://github.com/khoj-ai/khoj) - AGPL-3.0 License

## 🙏 Acknowledgments

- [Khoj AI](https://khoj.dev) - The foundation of ALETHEIA
- [n8n](https://n8n.io) - Workflow automation
- [Dokploy](https://dokploy.com) - Deployment platform

---

**ALETHEIA** - Your AI-powered knowledge navigation system 🧠✨

---

## 📋 Core Features & Capabilities

### **💬 Chat & Research**
- **Full-featured Web Chat**: Main interface at `kodan.space` with conversation management, message history, and streaming responses.
- **Telegram Integration**: Real-time chat via an integrated Telegram Bot.
- **Online Search**: Integration with SearXNG for web research.
- **Document & Knowledge Search**: Vector-based search across uploaded documents (PDF, text, markdown) and your knowledge base.
- **Citation Support**: Provides references and source links for retrieved information.

### **🎭 AI Agents & Models**
- **Multi-LLM Support**: Chat with a wide range of local and online models (Llama 3, GPT, Claude, Gemini, etc.).
- **Custom Agents**: Create specialized AI agents with unique personalities, tools, and knowledge bases.
- **Image Generation**: Generate images directly from your chat.
- **Code Analysis**: Process and understand code files.

### **🔄 Automation & Integration**
- **n8n Workflow Automation**: Integrated with the n8n platform for powerful automation.
- **API Access**: REST API for external access and integrations.
- **Code Execution Sandbox**: Uses Terrarium for safe code execution.

### **🔧 Developer & Deployment**
- **MCP Support**: Built-in Model Context Protocol integration.
- **Docker Deployment**: Fully containerized for easy and consistent deployment.
- **Self-Hosted**: Provides complete control over your data and infrastructure.