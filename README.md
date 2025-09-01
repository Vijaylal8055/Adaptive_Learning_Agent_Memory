# Adaptive_Learning_Agent_Memory
Overview
This project is an AI-powered marketing automation system that dynamically classifies leads, recommends engagement strategies, 
and optimizes campaigns using adaptive learning and memory management.

It uses:
Flask API for backend services
Flask-SocketIO for real-time lead updates
Memory Manager to simulate short-term, long-term, episodic, and semantic memory
Adaptive Learning Agent for personalized engagement recommendations

Features
Lead Triage: Classifies leads as Campaign Qualified, General Inquiry, or Cold Lead based on lead score
Engagement Recommendation: Suggests actions like Email Sent, Call Made, or No Action
Campaign Optimization: Provides strategies to improve conversion (e.g., Increase Email Outreach)

Memory Layers:
Short-term: Current lead data
Long-term: Customer history
Episodic: Logs of engagement events
Semantic: Knowledge graph of lead relationships

Real-time UI updates using WebSockets
Memory consolidation and compression

Project Structure
.
├── app.py               # Main Flask app with SocketIO
├── adaptive_module.py   # Adaptive Learning logic
├── memory_manager.py    # Memory management system
├── templates/
│   └── dashboard.html   # (Expected) Real-time dashboard UI
├── requirements.txt     # Python dependencies

Installation
1. Clone the Repository
2. Create Virtual Environment
3. Install Dependencies
4. Running the Application
Start the Flask app:
API Endpoints
1. Simulate Lead
POST /simulate-lead
2.Consolidate Memory
POST /consolidate-memory

How It Works
Lead Score → Category
score > 0.7 → Campaign Qualified
0.4 < score ≤ 0.7 → General Inquiry
score ≤ 0.4 → Cold Lead

Engagement Actions
score > 0.7 → Email Sent
0.4 < score ≤ 0.7 → Call Made
score ≤ 0.4 → No Action

Campaign Optimization
Cold Lead → Increase Email Outreach
Others → Continue Nurturing

Requirements
Flask>=2.3.3
Flask-Cors>=3.1.1
Flask-SocketIO>=5.5.1,<6.0
eventlet>=0.33.3
networkx>=3.1

Future Improvements
Add interactive dashboard (React/Vue) for real-time visualization
Store memory in a database (PostgreSQL/MongoDB) instead of in-memory
Implement machine learning-based lead scoring
Introduce campaign analytics and reporting
