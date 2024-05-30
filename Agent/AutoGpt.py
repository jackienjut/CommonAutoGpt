from typing import Optional

from langchain.memory import ConversationTokenBufferMemory
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.tools import BaseTool
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory

from Agent.Action import Action


class AutoGpt:
    def __init__(self,
                 name: str,
                 llm: BaseChatModel,
                 tools: list[BaseTool],
                 work_dir: str,
                 main_prompt_file: str,
                 max_thought_steps: Optional[int] = 10
                 ):
        self.name = name
        self.llm = llm
        self.tools = tools
        self.work_dir = work_dir
        self.main_prompt_file = main_prompt_file
        self.max_thought_steps = max_thought_steps

        self.output_parser = PydanticOutputParser(pydantic_object=Action)

    def run(self,
            user_input: str,
            chat_history: ChatMessageHistory,
            verbose=True) -> str:
        """
                运行智能体
                :param user_input: 用户输入
                :param chat_history: 对话上下文（长时记忆）
                :param verbose: 是否显示详细信息
                """

        short_term_mem = ConversationTokenBufferMemory(
            llm=self.llm,
            max_token_limit=3000
        )

        thought_steps_count = 0

        replay = ""

        while thought_steps_count < self.max_thought_steps:
            if verbose:
                self.verbose_handler.on_thought_start(thought_steps_count)
                print(f"Thought step {thought_steps_count}")

        return replay
