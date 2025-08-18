# KODAN Development Rules

## 🎯 Project Overview
KODAN (Knowledge Omni-Directional Discovery And Navigation) is a self-hosted AI assistant based on Khoj v2.0.0-beta.13 with enhanced Telegram integration, n8n automation, and production deployment capabilities.

## 🏗️ Architecture Principles

### Core Components
- **KODAN Server**: Main AI backend (port 42110)
- **n8n Integration**: Workflow automation (port 5678) 
- **Telegram Bot**: Real-time chat interface
- **PostgreSQL**: Database with pgvector for embeddings
- **Dokploy**: Production deployment platform

### File Organization
```
/workspaces/khoj/
├── src/khoj/                 # Core KODAN/Khoj source
├── src/interface/            # Web and client interfaces  
├── .kodan/                   # KODAN-specific files
│   ├── docs/                 # Documentation
│   ├── config/               # Configuration files
│   └── scripts/              # Utility scripts
├── .cursor/                  # Cursor IDE configuration
└── .taskmaster/              # Task Master MCP files
```

## 🛠️ Development Standards

### Code Style
- **Python**: Follow PEP 8, use type hints
- **TypeScript/JavaScript**: Use modern ES6+ syntax
- **API Design**: RESTful endpoints with clear documentation
- **Error Handling**: Comprehensive error handling and logging

### Git Workflow
- **Main Branch**: `kodan-v2-development`
- **Commit Messages**: Use conventional commits format
- **Documentation**: Update README and docs with changes
- **Testing**: Test all changes before committing

### Infrastructure
- **Docker**: Use docker-compose for local development
- **Production**: Deploy via Dokploy with proper SSL
- **Environment**: Use .env files for configuration
- **Security**: Never commit API keys or secrets

## 🔧 Technical Guidelines

### API Development
- **Authentication**: Use Bearer tokens for API access
- **Rate Limiting**: Implement rate limiting for public endpoints
- **CORS**: Configure CORS for web interface access
- **Validation**: Validate all input parameters

### Integration Patterns
- **n8n Workflows**: Use webhooks, not polling
- **Telegram**: Use webhook mode for real-time responses
- **MCP Tools**: Prefer MCP tools over direct API calls
- **External APIs**: Use proper error handling and retries

### Performance
- **Database**: Use pgvector for efficient similarity search
- **Caching**: Implement caching for frequent queries
- **Async**: Use async/await for I/O operations
- **Resource Management**: Monitor memory and CPU usage

## 🚀 Feature Development

### New Feature Checklist
- [ ] Research existing capabilities to avoid duplication
- [ ] Design API endpoints following REST conventions
- [ ] Implement proper error handling and validation
- [ ] Add comprehensive logging for debugging
- [ ] Create or update documentation
- [ ] Test integration with existing features
- [ ] Update Task Master with development tasks

### Telegram Integration Guidelines
- **Commands**: Use slash commands for special functions
- **Responses**: Keep responses concise but informative
- **Error Handling**: Provide user-friendly error messages
- **Context**: Maintain conversation context across messages

### n8n Workflow Guidelines
- **Node Naming**: Use descriptive, action-oriented names
- **Error Handling**: Include error paths in workflows
- **Documentation**: Comment complex expressions
- **Testing**: Test workflows before production deployment

## 🧪 Testing Standards

### Required Tests
- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test API endpoints and workflows
- **End-to-End Tests**: Test complete user journeys
- **Performance Tests**: Monitor response times and resource usage

### Testing Environment
- **Local**: Use docker-compose for local testing
- **Staging**: Test on VPS before production
- **Production**: Monitor real-world usage and performance

## 📚 Documentation Requirements

### Code Documentation
- **Docstrings**: All functions and classes
- **Type Hints**: Use Python type hints
- **Comments**: Explain complex logic and business rules
- **README**: Keep project README up to date

### API Documentation
- **Endpoints**: Document all API endpoints
- **Parameters**: Specify required and optional parameters
- **Examples**: Provide usage examples
- **Error Codes**: Document possible error responses

## 🔐 Security Guidelines

### Authentication
- **API Keys**: Store in environment variables
- **Tokens**: Use JWT tokens with proper expiration
- **Validation**: Validate all user inputs
- **Authorization**: Implement proper access controls

### Data Protection
- **Encryption**: Encrypt sensitive data at rest
- **HTTPS**: Use HTTPS for all external communications
- **Backups**: Regular database backups
- **Privacy**: Respect user data privacy

## 🎯 Current Development Focus

### Immediate Priorities
1. **Enhanced Telegram Features**: Slash commands, file upload
2. **n8n UI Integration**: Workflow management in KODAN
3. **Feature Optimization**: Improve existing capabilities
4. **Documentation**: Comprehensive user and developer docs

### Long-term Vision
- **Voice Integration**: Speech-to-text and text-to-speech
- **Mobile Apps**: Native mobile applications
- **Advanced Agents**: Sophisticated AI agent capabilities
- **Enterprise Features**: Multi-tenant, advanced security

---

*KODAN Development Rules - Last Updated: August 17, 2025*
