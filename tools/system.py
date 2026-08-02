"""系统类 MC Tool 组件。

对应 Mindcraft 的系统控制命令（停止动作、清空聊天等）。
参考源码：[`E:/mindcraft/src/agent/commands/actions.js`](E:/mindcraft/src/agent/commands/actions.js:28)
"""

from __future__ import annotations

from .base import MCToolBase


class StopTool(MCToolBase):
    """强制停止所有动作。"""

    name: str = "mc_stop"
    description: str = (
        "强制停止 Bot 当前正在执行的所有动作。无参数。"
        "用于中断正在进行的持续动作（如跟随、收集等）。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行停止动作命令。"""
        return await self._execute_mc("!stop", [])


class ClearChatTool(MCToolBase):
    """清空聊天历史。"""

    name: str = "mc_clear_chat"
    description: str = (
        "清空 Bot 的聊天历史记录。无参数。"
        "Bot 会忘记之前的对话上下文。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行清空聊天命令。"""
        return await self._execute_mc("!clearChat", [])


class StfuTool(MCToolBase):
    """停止聊天和自主对话。"""

    name: str = "mc_stfu"
    description: str = (
        "停止 Bot 的聊天和自主对话循环（self-prompting）。无参数。"
        "Bot 会安静下来，不再主动说话。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行停止聊天命令。"""
        return await self._execute_mc("!stfu", [])


class RestartTool(MCToolBase):
    """重启 Agent 进程。"""

    name: str = "mc_restart"
    description: str = "重启 Mindcraft Agent 进程。无参数。慎用。"

    async def execute(self) -> tuple[bool, str]:
        """执行重启命令。"""
        return await self._execute_mc("!restart", [])
