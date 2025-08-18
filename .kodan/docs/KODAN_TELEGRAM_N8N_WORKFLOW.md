# KODAN Telegram Integration via n8n Workflow

## Overview
Create n8n workflow to bridge Telegram bot with KODAN AI for seamless chat functionality.

## Workflow Architecture

```
Telegram Message → n8n Webhook → KODAN API → AI Response → Telegram Reply
```

## n8n Workflow Components

### 1. Telegram Trigger
- **Node**: Telegram Bot webhook
- **Purpose**: Receive messages from Telegram users
- **Configuration**: 
  - Bot token: (already configured in n8n)
  - Webhook URL: `http://n8n.kodan.space/webhook/telegram-chat`

### 2. Message Processing
- **Node**: Function/Code
- **Purpose**: Extract and format message for KODAN API
- **Logic**:
  ```javascript
  // Extract message data
  const message = $json.message.text;
  const userId = $json.message.from.id;
  const chatId = $json.message.chat.id;
  
  return {
    query: message,
    user_id: userId,
    chat_id: chatId,
    timestamp: new Date().toISOString()
  };
  ```

### 3. KODAN API Call
- **Node**: HTTP Request
- **Purpose**: Send query to KODAN for AI processing
- **Configuration**:
  - Method: POST
  - URL: `http://kodan.space/api/chat` (need to verify endpoint)
  - Headers: `Content-Type: application/json`
  - Body:
    ```json
    {
      "q": "{{ $json.query }}",
      "conversation_id": "telegram_{{ $json.user_id }}",
      "stream": false
    }
    ```

### 4. Response Formatting
- **Node**: Function/Code
- **Purpose**: Format KODAN response for Telegram
- **Logic**:
  ```javascript
  const response = $json.response;
  
  // Ensure response fits Telegram message limits
  let message = response.length > 4096 
    ? response.substring(0, 4093) + "..." 
    : response;
    
  return {
    chat_id: $('Message Processing').item.json.chat_id,
    text: message,
    parse_mode: 'Markdown'
  };
  ```

### 5. Telegram Reply
- **Node**: Telegram Bot send message
- **Purpose**: Send AI response back to user
- **Configuration**:
  - Chat ID: `{{ $json.chat_id }}`
  - Message: `{{ $json.text }}`
  - Parse mode: Markdown

## Enhanced Features

### Research Mode Integration
Add conditional logic to detect `/research` command and route to KODAN's research endpoint:

```javascript
// In Message Processing node
const message = $json.message.text;
const isResearch = message.startsWith('/research ');

if (isResearch) {
  return {
    endpoint: '/api/research',
    query: message.replace('/research ', ''),
    mode: 'research'
  };
} else {
  return {
    endpoint: '/api/chat',
    query: message,
    mode: 'chat'
  };
}
```

### Error Handling
Add error handling nodes:
- Network timeout handling
- KODAN API error responses
- Fallback responses for users

### User Session Management
- Store conversation history
- Implement user preferences
- Track usage statistics

## Implementation Steps

1. **Create n8n Workflow**
   - Use n8n-mcp to generate workflow structure
   - Configure nodes with KODAN API endpoints
   - Test with sample messages

2. **KODAN API Discovery**
   - Identify correct chat and research endpoints
   - Test API responses and formats
   - Configure authentication if needed

3. **Telegram Bot Setup**
   - Verify webhook configuration
   - Test message delivery
   - Configure commands (/research, /help, etc.)

4. **Integration Testing**
   - End-to-end message flow
   - Error scenario testing
   - Performance optimization

## Next Actions

1. Use n8n-mcp tools to create initial workflow
2. Discover KODAN API endpoints through code examination
3. Deploy and test workflow in n8n
4. Configure Telegram bot webhook
