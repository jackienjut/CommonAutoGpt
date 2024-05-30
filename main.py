from dotenv import load_dotenv, find_dotenv

from Agent.AutoGpt import AutoGpt

_ = load_dotenv(find_dotenv())
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories.in_memory import ChatMessageHistory


def lauch_agent(agent):
    human_icon = "\U0001F468"
    ai_icon = "\U0001F916"
    chat_history = ChatMessageHistory()

    while True:
        user_input = input(f"{ai_icon} 我可以帮你什么？:\n {human_icon}: ")
        if user_input.strip().lower() == "exit":
            break
        replay = agent.run(user_input, chat_history, verbose=True)
        print(f"{ai_icon} {replay}")


def main():
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
        model_kwargs={
            "seed": 43
        }
    )
    # 自定义工具集
    tools = []

    # 定义智能体
    agent = AutoGpt(
        name="AutoGPT",
        llm=llm,
        tools=tools,
        work_dir="./work_dir",
        main_prompt_file="./prompt.txt",
        max_thought_steps=20
    )
    # 运行智能体
    lauch_agent(agent)


if __name__ == '__main__':
    main()
