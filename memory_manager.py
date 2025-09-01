import networkx as nx
from datetime import datetime

class MemoryManager:
    def __init__(self):
        self.short_term = {}       # Current lead contexts
        self.long_term = {}        # Customer history & preferences
        self.episodic = []         # Successful problem-resolution patterns
        self.semantic = nx.Graph() # Domain knowledge graph

    # Short-term memory
    def update_short_term(self, lead_id, context):
        self.short_term[lead_id] = context

    # Long-term memory
    def update_long_term(self, lead_id, info):
        if lead_id in self.long_term:
            self.long_term[lead_id].update(info)
        else:
            self.long_term[lead_id] = info

    # Episodic memory
    def log_episode(self, lead_id, info):
        info["timestamp"] = datetime.now().isoformat()
        self.episodic.append({lead_id: info})

    # Semantic memory: add relationships
    def add_semantic_relation(self, entity1, entity2, relation):
        self.semantic.add_edge(entity1, entity2, relation=relation)

    # Consolidation: move short-term → long-term
    def consolidate(self):
        for lead_id, context in self.short_term.items():
            self.update_long_term(lead_id, context)
        self.short_term.clear()

    # Retrieve all memory for a lead
    def retrieve(self, lead_id):
        return {
            "short_term": self.short_term.get(lead_id),
            "long_term": self.long_term.get(lead_id),
            "episodic": [e for e in self.episodic if lead_id in e]
        }

    # Simple compression for long-term memory
    def compress_long_term(self):
        for lead_id, data in self.long_term.items():
            if isinstance(data, dict) and len(data) > 5:
                keys = list(data.keys())[:5]
                self.long_term[lead_id] = {k: data[k] for k in keys}
