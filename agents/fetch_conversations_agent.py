from utils.api_utils import fetch_conversations
import re

def get_conversations(resident_id: str, resident_name: str, event_type: str) -> (str, int):
    """
    Fetch conversations from the API and return summaries and count.
    Remove the **Recommendations:** and **Recommendations**: sections from each incident summary.
    """
    conversations = fetch_conversations(resident_id, resident_name, event_type)
    
    if conversations:
        summaries = []
        
        for conv in conversations:
            summary = conv.get("summary", "")
            
            summary_cleaned = re.sub(r'\*\*\d*\.*\s*Recommendations\**:.*', '', summary, flags=re.DOTALL)
            summaries.append(summary_cleaned)
        
        joined_summaries = "\n\n".join(summaries)
        incident_count = len([conv for conv in conversations if conv["event_type"] == event_type])
        
        return joined_summaries, incident_count
    else:
        return f"No conversations found for resident_id: {resident_id} and event_type: {event_type}", 0
