from agents.fetch_conversations_agent import get_conversations
from agents.ai_agent import initialize_preventive_agent, generate_preventive_plan

def main(resident_id, resident_name, event_type):
    conversation_data, incident_count = get_conversations(resident_id, resident_name, event_type)
    print(conversation_data)

    preventive_agent = initialize_preventive_agent()

    preventive_plan = generate_preventive_plan(preventive_agent, resident_id, resident_name, event_type, conversation_data, incident_count)

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    print("Generated Preventive Measures Plan:")
    print(preventive_plan)

if __name__ == "__main__":
    resident_id = "Res_01"
    resident_name = "John Smith"
    event_type = "Fall"
    main(resident_id, resident_name, event_type)
