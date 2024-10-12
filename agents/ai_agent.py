import os
from typing import Optional, List, Mapping, Any
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
import openai
from langchain_openai import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY", "")

class OpenAILLM(LLM):
    model_name: str = "gpt-4"
    temperature: float = 0.5
    max_tokens: int = 2048

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                stop=stop
            )

            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            raise Exception(f"OpenAI API Error: {e}")
        
    @property
    def _llm_type(self) -> str:
        return f"openai-{self.model_name}"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }

prompt_template = PromptTemplate(
    input_variables=["resident_name", "event_type", "incident_count", "incident_data"],
    template=(
        "You are an assistant helping to generate a preventive care plan for a resident "
        "based on past incidents.\n\n"
        "Resident: {resident_name}\n"
        "Event Type: {event_type}\n"
        "Total Number of Incidents Reported: {incident_count}\n\n"
        "Incident Summaries:\n"
        "{incident_data}\n\n"
        "Based on the above incidents, please provide a detailed preventive care plan that includes the following sections:\n"
        "1. **What we learned from the events**:\n"
        "   - Highlight common patterns or issues observed across the {incident_count} incidents.\n"
        "2. **What can we do to prevent this in the future**:\n"
        "   - List specific strategies or changes that can be implemented to mitigate similar incidents.\n"
        "3. **Impact Level**:**No injury / Minor / Moderate / Major\n"
        "   - Assess the potential severity of incidents and categorize them as No injury / Minor / Moderate / Major.\n\n"
        "Ensure that each section is well-articulated and provides actionable insights for care home staff, specifically addressing {resident_name}'s needs and circumstances."
    )
)

def initialize_preventive_agent():
    llm = ChatOpenAI(model="gpt-4", api_key=openai.api_key)
    agent = prompt_template | llm
    return agent

def generate_preventive_plan(agent, resident_id, resident_name, event_type, incident_data, incident_count):
    prompt_data = {
        "resident_name": resident_name,
        "event_type": event_type,
        "incident_count": incident_count, 
        "incident_data": incident_data
    }
    
    return agent.invoke(prompt_data)

