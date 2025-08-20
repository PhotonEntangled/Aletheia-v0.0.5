FROM node:18-slim

# Set working directory
WORKDIR /app

# Install task-master-ai globally
RUN npm install -g task-master-ai

# Expose the default MCP port (though we'll use a dynamic one)
EXPOSE 65432

# Start the MCP server
CMD ["task-master-ai", "mcp", "--port=65432", "--host=0.0.0.0"]
