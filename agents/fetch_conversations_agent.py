from utils.api_utils import fetch_conversations

def get_conversations(resident_id: str, resident_name: str, event_type: str) -> (str, int):
    conversations = fetch_conversations(resident_id, resident_name, event_type)
    if conversations:
        summaries = "\n\n".join([conv["summary"] for conv in conversations])
        incident_count = len([conv for conv in conversations if conv["event_type"] == event_type])
        return summaries, incident_count
    else:
        return f"No conversations found for resident_id: {resident_id} and event_type: {event_type}", 0
