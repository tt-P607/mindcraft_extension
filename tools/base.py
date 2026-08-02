"""MC Tool 基类。

所有 MC Tool 通过 ``mindcraft_adapter`` 适配器远程执行 Mindcraft 命令。
参考 [`plugins/snowluma_extension/src/tools.py`](plugins/snowluma_extension/src/tools.py:22) 的 Tool 模式。

调用模式：
    1. ``adapter_api.get_adapter(signature)`` 获取适配器实例
    2. ``adapter.send_mc_action(command, args, timeout)`` 发送命令并等待结果
"""

from __future__ import annotations

from typing import Any

from src.app.plugin_system.api import adapter_api
from src.app.plugin_system.api.log_api import get_logger
from src.core.components.base.tool import BaseTool
from src.core.components.types import ChatType

logger = get_logger("mindcraft_extension")

# 适配器签名：plugin_name:component_type:component_name
_MC_ADAPTER_SIGNATURE = "mindcraft_adapter:adapter:mindcraft_adapter"


class MCToolBase(BaseTool):
    """MC Tool 基类。

    所有 MC Tool 通过适配器远程执行 Mindcraft 命令。
    子类只需实现 ``execute()`` 方法，调用 ``self._execute_mc()`` 即可。

    Class Attributes:
        associated_platforms: 关联平台为 ``minecraft``
        chat_type: 支持所有聊天类型
        dependencies: 依赖 ``mindcraft_adapter`` 适配器
    """

    associated_platforms: list[str] = ["minecraft"]
    chat_type: ChatType = ChatType.ALL
    dependencies: list[str] = [_MC_ADAPTER_SIGNATURE]

    async def _execute_mc(
        self,
        command: str,
        args: list[Any],
        timeout: float = 120.0,
    ) -> tuple[bool, str]:
        """通过适配器发送 MC 命令并返回结果。

        Args:
            command: Mindcraft 命令字符串，如 ``!goToPlayer``
            args: 命令参数列表
            timeout: 超时时间（秒），默认 120 秒

        Returns:
            ``(是否成功, 结果文本)``
        """
        adapter = adapter_api.get_adapter(_MC_ADAPTER_SIGNATURE)
        if adapter is None:
            return False, "mindcraft_adapter 未启动：请先启用并启动 mindcraft_adapter 插件。"

        if not hasattr(adapter, "send_mc_action"):
            return False, "mindcraft_adapter 不支持 send_mc_action：请确认版本兼容。"

        logger.debug(f"发送 MC 命令: command={command}, args={args}")

        try:
            result = await adapter.send_mc_action(command, args, timeout=timeout)  # type: ignore[attr-defined]
        except TimeoutError as exc:
            logger.warning(f"MC 命令超时: command={command}, error={exc}")
            return False, f"MC 命令执行超时：{command}"
        except RuntimeError as exc:
            logger.warning(f"MC 命令执行失败: command={command}, error={exc}")
            return False, f"MC 命令执行失败：{exc}"
        except Exception as exc:
            logger.error(f"MC 命令执行异常: command={command}, error={exc}")
            return False, f"MC 命令执行异常：{exc}"

        logger.debug(f"MC 命令结果: command={command}, result={result[:200]}")
        return True, result
