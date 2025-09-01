class AdaptiveLearning:
    def __init__(self, memory_manager):
        self.mm = memory_manager

    def recommend_action(self, lead_id, context):
        lead_data = self.mm.retrieve(lead_id)
        score = context.get("score", 0)
        if score > 0.7:
            return "Email Sent"
        elif score > 0.4:
            return "Call Made"
        else:
            return "No Action"
