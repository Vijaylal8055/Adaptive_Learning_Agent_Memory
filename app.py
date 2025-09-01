from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import random
from memory_manager import MemoryManager
from adaptive_module import AdaptiveLearning

# Initialize Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize memory and adaptive agent
memory_manager = MemoryManager()
adaptive_agent = AdaptiveLearning(memory_manager)

lead_counter = 100000  # simple lead ID generator

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/simulate-lead', methods=['POST'])
def simulate_lead():
    global lead_counter
    data = request.json or {}
    lead_counter += 1
    lead_id = lead_counter

    # Simulate lead context
    context = data.get("context", {"score": round(random.random(), 2)})
    memory_manager.update_short_term(lead_id, context)

    # Lead Triage
    if context["score"] > 0.7:
        category = "Campaign Qualified"
    elif context["score"] > 0.4:
        category = "General Inquiry"
    else:
        category = "Cold Lead"

    memory_manager.update_short_term(lead_id, {"category": category})
    # Add semantic relation
    memory_manager.add_semantic_relation(f"Lead-{lead_id}", category, "belongs_to")

    # Emit Lead Triage update
    socketio.emit("lead_update", {"lead_id": lead_id, "context": context, "category": category})

    # Engagement Agent
    engagement_status = adaptive_agent.recommend_action(lead_id, context)
    memory_manager.update_long_term(lead_id, {"engagement_status": engagement_status})
    memory_manager.log_episode(lead_id, {"category": category, "engagement": engagement_status})

    # Emit Engagement update
    socketio.emit("engagement_update", {"lead_id": lead_id, "engagement_status": engagement_status})

    # Campaign Optimization
    if category == "Cold Lead":
        recommended_action = "Increase Email Outreach"
    else:
        recommended_action = "Continue Nurturing"

    # Emit Campaign Optimization update
    socketio.emit("campaign_update", {"lead_id": lead_id, "recommended_action": recommended_action})

    return jsonify({"lead_id": lead_id, "category": category, "engagement_status": engagement_status, "recommended_action": recommended_action})

@app.route('/consolidate-memory', methods=['POST'])
def consolidate_memory():
    memory_manager.consolidate()
    memory_manager.compress_long_term()
    return jsonify({"status": "Memory consolidated"})

if __name__ == "__main__":
    # Use localhost binding for browser accessibility
    socketio.run(app, host="127.0.0.1", port=8000, debug=True)
