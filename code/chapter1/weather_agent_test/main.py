"""
天气代理测试 - 主入口文件
"""

import os
from config import API_CONFIG
from clients import OpenAICompatibleClient
from core import AgentRunner


def main():
    # 配置环境变量
    os.environ['TAVILY_API_KEY'] = API_CONFIG['tavily_api_key']

    # 初始化 LLM 客户端
    llm = OpenAICompatibleClient(
        model=API_CONFIG['model_id'],
        api_key=API_CONFIG['api_key'],
        base_url=API_CONFIG['base_url']
    )

    # 创建 Agent 运行器
    runner = AgentRunner(llm)

    # 用户输入
    user_prompt = "你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。"

    # 运行 Agent
    result = runner.run(user_prompt)
    print(f"\n最终结果: {result}")


if __name__ == "__main__":
    main()