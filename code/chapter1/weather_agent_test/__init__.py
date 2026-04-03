"""
Weather Agent Test - 天气代理测试
按层级架构拆分的模块化代码
"""

from .config import AGENT_SYSTEM_PROMPT, API_CONFIG
from .tools import get_weather, get_attraction, available_tools
from .clients import OpenAICompatibleClient
from .core import AgentRunner