"""Mindcraft 扩展能力插件入口。

提供 Minecraft 的游戏动作和查询能力作为 MoFox Tool 组件。
依赖 ``mindcraft_adapter`` 适配器插件。

参考实现：[`plugins/snowluma_extension/plugin.py`](plugins/snowluma_extension/plugin.py:62)
"""

from __future__ import annotations

from typing import cast

from src.app.plugin_system.api.log_api import get_logger
from src.core.components.base import BasePlugin
from src.core.components.loader import register_plugin

from .config import MindcraftExtensionConfig
from .tools.interaction import (
    AttackPlayerTool,
    AttackTool,
    ClearFurnaceTool,
    CollectBlocksTool,
    ConsumeTool,
    CraftTool,
    DiscardTool,
    EndConversationTool,
    EndGoalTool,
    EquipTool,
    GiveItemTool,
    GoalTool,
    LookAtPlayerTool,
    LookAtPositionTool,
    NewActionTool,
    PlaceBlockTool,
    PutInChestTool,
    ShowVillagerTradesTool,
    SmeltTool,
    StartConversationTool,
    TakeFromChestTool,
    TradeWithVillagerTool,
    UseOnTool,
    ViewChestTool,
    SetModeTool,
)
from .tools.movement import (
    DigDownTool,
    FollowPlayerTool,
    GoToBedTool,
    GoToCoordsTool,
    GoToPlaceTool,
    GoToPlayerTool,
    GoToSurfaceTool,
    MoveAwayTool,
    RememberPlaceTool,
    SearchBlockTool,
    SearchEntityTool,
    StayTool,
    TpToPlayerTool,
)
from .tools.query import (
    QueryCraftableTool,
    QueryCraftingPlanTool,
    QueryEntitiesTool,
    QueryInventoryTool,
    QueryModesTool,
    QueryNearbyBlocksTool,
    QuerySavedPlacesTool,
    QueryStatsTool,
)
from .tools.system import (
    ClearChatTool,
    RestartTool,
    StfuTool,
    StopTool,
)

logger = get_logger("mindcraft_extension")


@register_plugin
class MindcraftExtensionPlugin(BasePlugin):
    """Mindcraft 扩展能力插件。

    提供 MC 游戏动作和查询能力作为 MoFox Tool 组件。
    依赖 ``mindcraft_adapter`` 适配器插件提供 WebSocket 通信通道。
    """

    plugin_name = "mindcraft_extension"
    configs: list[type] = [MindcraftExtensionConfig]

    def get_components(self) -> list[type]:
        """返回插件包含的组件类列表。

        当插件配置 disabled 时返回空列表。
        """
        if self.config is not None:
            config = cast(MindcraftExtensionConfig, self.config)
            if hasattr(config, "plugin") and not config.plugin.enabled:
                return []

        return [
            # 移动类 Tool
            GoToPlayerTool,
            TpToPlayerTool,
            FollowPlayerTool,
            GoToCoordsTool,
            SearchBlockTool,
            SearchEntityTool,
            MoveAwayTool,
            GoToPlaceTool,
            GoToBedTool,
            StayTool,
            DigDownTool,
            GoToSurfaceTool,
            RememberPlaceTool,
            # 交互类 Tool
            CollectBlocksTool,
            PlaceBlockTool,
            AttackTool,
            AttackPlayerTool,
            GiveItemTool,
            ConsumeTool,
            EquipTool,
            PutInChestTool,
            TakeFromChestTool,
            ViewChestTool,
            DiscardTool,
            CraftTool,
            SmeltTool,
            ClearFurnaceTool,
            UseOnTool,
            ShowVillagerTradesTool,
            TradeWithVillagerTool,
            LookAtPlayerTool,
            LookAtPositionTool,
            SetModeTool,
            GoalTool,
            EndGoalTool,
            NewActionTool,
            StartConversationTool,
            EndConversationTool,
            # 查询类 Tool
            QueryStatsTool,
            QueryInventoryTool,
            QueryNearbyBlocksTool,
            QueryCraftableTool,
            QueryEntitiesTool,
            QueryModesTool,
            QuerySavedPlacesTool,
            QueryCraftingPlanTool,
            # 系统类 Tool
            StopTool,
            ClearChatTool,
            StfuTool,
            RestartTool,
        ]
