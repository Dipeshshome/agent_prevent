from agents.fetch_conversations_agent import get_conversations
from agents.ai_agent import initialize_preventive_agent, generate_preventive_plan

def main(resident_id,resident_name, event_type):
    conversation_data = get_conversations(resident_id,resident_name, event_type)
    print(conversation_data)

    preventive_agent = initialize_preventive_agent()

    preventive_plan = generate_preventive_plan(preventive_agent, resident_id, resident_name, event_type, conversation_data)

    print("Generated Preventive Measures Plan:")
    print(preventive_plan)

if __name__ == "__main__":
    resident_id = "Res_01"
    resident_name="John Smith"
    event_type = "Skin integrity"
    main(resident_id,resident_name,event_type)
