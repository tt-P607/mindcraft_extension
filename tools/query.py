"""查询类 MC Tool 组件。

对应 Mindcraft 的查询命令，只返回信息不影响世界。
参考源码：[`E:/mindcraft/src/agent/commands/queries.js`](E:/mindcraft/src/agent/commands/queries.js:13)
"""

from __future__ import annotations

from typing import Annotated

from .base import MCToolBase


class QueryStatsTool(MCToolBase):
    """获取 Bot 状态信息。"""

    name: str = "mc_query_stats"
    description: str = (
        "获取 Bot 当前状态信息，包括：位置坐标、生命值、饥饿值、"
        "当前时间、附近玩家、已启用的自动行为模式。无参数。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行状态查询命令。"""
        return await self._execute_mc("!stats", [])


class QueryInventoryTool(MCToolBase):
    """获取背包内容。"""

    name: str = "mc_query_inventory"
    description: str = (
        "获取 Bot 背包内容和装备信息。无参数。"
        "返回所有物品及其数量。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行背包查询命令。"""
        return await self._execute_mc("!inventory", [])


class QueryNearbyBlocksTool(MCToolBase):
    """获取附近方块。"""

    name: str = "mc_query_nearby_blocks"
    description: str = (
        "获取 Bot 附近的方块信息。无参数。"
        "返回周围方方的类型和相对位置。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行附近方块查询命令。"""
        return await self._execute_mc("!nearbyBlocks", [])


class QueryCraftableTool(MCToolBase):
    """获取可合成物品。"""

    name: str = "mc_query_craftable"
    description: str = (
        "获取当前可以合成的物品列表。无参数。"
        "基于当前背包中的材料判断。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行可合成查询命令。"""
        return await self._execute_mc("!craftable", [])


class QueryEntitiesTool(MCToolBase):
    """获取附近实体。"""

    name: str = "mc_query_entities"
    description: str = (
        "获取 Bot 附近的实体信息。无参数。"
        "返回实体类型、距离、村民职业和 ID（如有）。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行实体查询命令。"""
        return await self._execute_mc("!entities", [])


class QueryModesTool(MCToolBase):
    """获取模式状态。"""

    name: str = "mc_query_modes"
    description: str = (
        "获取所有自动行为模式及开关状态。无参数。"
        "模式包括：self_preservation, unstuck, cowardice, self_defense, "
        "hunting, item_collecting, torch_placing, elbow_room, idle_staring, cheat。"
    )

    async def execute(self) -> tuple[bool, str]:
        """执行模式状态查询命令。"""
        return await self._execute_mc("!modes", [])


class QuerySavedPlacesTool(MCToolBase):
    """列出已保存位置。"""

    name: str = "mc_query_saved_places"
    description: str = "列出所有已保存的位置名称。无参数。"

    async def execute(self) -> tuple[bool, str]:
        """执行已保存位置查询命令。"""
        return await self._execute_mc("!savedPlaces", [])


class QueryCraftingPlanTool(MCToolBase):
    """获取合成计划。"""

    name: str = "mc_query_crafting_plan"
    description: str = (
        "获取指定物品的合成计划，包括所需材料和步骤。"
        "参数：target_item 为目标物品名称，quantity 为数量（默认1）。"
    )

    async def execute(
        self,
        target_item: Annotated[str, "目标物品名称"],
        quantity: Annotated[int, "数量"] = 1,
    ) -> tuple[bool, str]:
        """执行合成计划查询命令。"""
        return await self._execute_mc("!getCraftingPlan", [target_item, quantity])
