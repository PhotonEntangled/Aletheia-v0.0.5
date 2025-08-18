# KODAN Feature Roadmap

This document outlines the planned features and enhancements for the Kodan project. It serves as a high-level guide for our development efforts.

## 🚀 **Phase 1: Core Enhancements & UX**

This phase focuses on improving the user experience and extending the core capabilities of Kodan.

| Feature ID | Feature | Description | Priority | Status |
|---|---|---|---|---|
| RDM-001 | **Visible Thinking Process** | Implement a UI element that displays the AI's thought process (e.g., retrieved context, tool usage) before delivering the final response, similar to modern AI chat interfaces. | High | `Pending` |
| RDM-002 | **Context Window Indicator** | Add a visual indicator in the chat UI that shows the current context window usage as a percentage, helping users manage long conversations. | High | `Pending` |
| RDM-003 | **Advanced Voice Integration** | Replace the basic speech-to-text with a more robust system or API that supports custom keyword recognition and is less prone to errors, ensuring a smoother voice interaction flow. | Medium | `Pending` |
| RDM-004 | **Database Sharding Strategy** | Research and document a strategy for database sharding with `pgvector`. Define thresholds (e.g., number of documents, videos) for when this will become necessary. | Medium | `Pending` |

## 🌐 **Phase 2: Platform & Ecosystem Expansion**

This phase is about extending Kodan's reach and integrating it more deeply into user workflows.

| Feature ID | Feature | Description | Priority | Status |
|---|---|---|---|---|
| RDM-005 | **Intuitive n8n Interface** | Develop a UI within Kodan to manage and interact with n8n workflows. This could include viewing workflow status, triggering workflows, and a simplified builder. | High | `Pending` |
| RDM-006 | **Browser Extension** | Create a Chrome browser extension for RAG capabilities on any webpage. Features to include summarizing content, analyzing documents in the browser, and interacting with web content like youtube where the user would like features like youtube video transcript summarisation and further research and connections to previous learnings. | High | `Pending` |
| RDM-007 | **AI-Powered Task Management** | Integrate a comprehensive AI to-do list and life planning system. The AI should be able to manage tasks (create, complete, reschedule) based on natural language commands. | High | `Pending` |

## 💡 **Phase 3: Deep Intelligence & Proactivity**

This phase aims to make Kodan a more proactive and intelligent assistant.

| Feature ID | Feature | Description | Priority | Status |
|---|---|---|---|---|
| RDM-008 | **Proactive Agent Actions** | Based on scheduled automations and chat context, allow agents to proactively perform actions, such as pre-fetching research for a calendar event or suggesting relevant notes during a conversation. | High | `Pending` |
| RDM-009 | **Automated Knowledge Synthesis** | Create a workflow where Kodan periodically reviews new information (from notes, web, documents) and automatically generates synthesis notes, connecting disparate ideas and identifying new insights. | Medium | `Pending` |
| RDM-010 | **Embedded IDE Experience** | Integrate a web-based IDE (like Monaco Editor) into the Kodan frontend, connected to the Terrarium sandbox, allowing for a fully interactive code editing and execution environment within the chat. | Low | `Pending` |
| RDM-011 | **Conversational Memory Management** | Implement a `/remember` command to explicitly commit parts of a conversation to the vector database and a `/forget` command to remove them, giving the user fine-grained control over the AI's memory. | Medium | `Pending` |

## 🏛️ **Phase 4: Polymath & Self-Improvement Tools**

This phase focuses on building highly specialized tools for deep research, financial management, and personal development, transforming Kodan into a true polymath's assistant.

| Feature ID | Feature | Description | Priority | Status |
|---|---|---|---|---|
| RDM-012 | **Truth-Seeker Toolkit** | Develop a specialized research mode for deep, multi-source investigation into complex topics like historical conspiracies or ancient civilizations. It will go beyond mainstream sources, analyze iconography, and cross-reference disparate data types to uncover hidden connections. | Medium | `Pending` |
| RDM-013 | **Integrated Finance & Trading Tools** | Add a dedicated module for finance. This will include tools for investment tracking, algorithmic trading strategy development, market analysis, and personal finance management, all powered by AI. | Medium | `Pending` |
| RDM-014 | **The Opinion Bank** | Create a dedicated feature for users to log, track, and analyze their opinions on any topic. The system will allow for updates, track how opinions evolve, and help users identify biases and gaps in their understanding, serving as a powerful self-improvement tool. | High | `Pending` |

---
*This roadmap is a living document and will be updated as the project evolves.*
