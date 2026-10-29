import re
from typing import Union

from langchain.agents.agent import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish

FINAL_ANSWER_ACTION = "Final Answer:"


class CustomMRKLOutputParser(AgentOutputParser):
    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        if FINAL_ANSWER_ACTION in text:
            return AgentFinish(
                {
                    "output": text.split(FINAL_ANSWER_ACTION)[-1].strip(),
                    "Final Thought": text.rsplit(FINAL_ANSWER_ACTION, 1)[0].strip(),
                 }, text
            )
        # \s matches against tab/newline/whitespace
        regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, text, re.DOTALL)
        if not match:
            error_str = f"Could not parse LLM output: `{text[:100]}`"
            error_str = "Status Code: 400. Response: {\"message\": \"" + error_str + "\""
            error_str += ". You should choose one of: (1) change the input and retry; (2) return the 'Final Answer' and explain what happened; (You must choose this one when the error occurs more than 3 times.) (3) call another function."
            raise ValueError(error_str)
        
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(action, action_input.strip(" ").strip('"'), text)

class CustomMRKLOutputParser2(AgentOutputParser):
    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        final_answer_action = "ASSISTANT Response:"
        if final_answer_action in text:
            return AgentFinish(
                {
                    "output": text.split(final_answer_action)[-1].strip(),
                    "Final Thought": text.rsplit(final_answer_action, 1)[0].strip(),
                 }, text
            )
        # \s matches against tab/newline/whitespace
        regex = r"ASSISTANT\s*Action\s*\d*\s*:(.*?)\nASSISTANT\s*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, text, re.DOTALL)
        if not match:
            error_str = f"Could not parse LLM output: `{text[:100]}`"
            error_str = "Status Code: 400. Response: {\"message\": \"" + error_str + "\""
            error_str += ". You should choose one of: (1) change the input and retry; (2) return the 'Final Answer' and explain what happened; (You must choose this one when the error occurs more than 3 times.) (3) call another function."
            raise ValueError(error_str)
        
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(action, action_input.strip(" ").strip('"'), text)
    
class CustomMRKLOutputParser3(AgentOutputParser):
    def parse(self, text: str) -> Union[AgentAction, AgentFinish]:
        final_answer_action = "ASSISTANT Response:"
        if final_answer_action in text:
            return AgentFinish(
                {
                    "output": text.split(final_answer_action)[-1].strip(),
                    "Final Thought": text.rsplit(final_answer_action, 1)[0].strip(),
                 }, text
            )
        # \s matches against tab/newline/whitespace
        regex = r"ASSISTANT\s*Action\s*\d*\s*:(.*?)\nASSISTANT\s*Action\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)\n"
        match = re.search(regex, text, re.DOTALL)
        if not match:
            error_str = f"Could not parse LLM output: `{text[:100]}`"
            error_str = "Status Code: 400. Response: {\"message\": \"" + error_str + "\""
            error_str += ". You should choose one of: (1) change the input and retry; (2) return the 'Final Answer' and explain what happened; (You must choose this one when the error occurs more than 3 times.) (3) call another function."
            raise ValueError(error_str)
        
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(action, action_input.strip(" ").strip('"'), text)