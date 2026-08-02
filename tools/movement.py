"""移动类 MC Tool 组件。

对应 Mindcraft 的移动相关动作命令。
参考源码：[`E:/mindcraft/src/agent/commands/actions.js`](E:/mindcraft/src/agent/commands/actions.js:28)
"""

from __future__ import annotations

from typing import Annotated

from .base import MCToolBase


class GoToPlayerTool(MCToolBase):
    """前往指定玩家的位置。"""

    name: str = "mc_go_to_player"
    description: str = (
        "前往指定玩家的位置。"
        "参数：player_name 为目标玩家名称，closeness 为靠近距离（格，默认3.0）。"
        "注意：这是寻路移动，可能较慢。若需瞬间到达请用 mc_tp_to_player。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "目标玩家名称"],
        closeness: Annotated[float, "靠近距离（格）"] = 3.0,
    ) -> tuple[bool, str]:
        """执行前往玩家命令。"""
        return await self._execute_mc("!goToPlayer", [player_name, closeness])


class TpToPlayerTool(MCToolBase):
    """瞬间传送到指定玩家位置。"""

    name: str = "mc_tp_to_player"
    description: str = (
        "瞬间传送到指定玩家的位置（绕过寻路，直接 /tp）。"
        "参数：player_name 为目标玩家名称。"
        "需要服务器开启 allow-cheats；若失败可改用 mc_go_to_player 寻路。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "目标玩家名称"],
    ) -> tuple[bool, str]:
        """执行传送命令。"""
        return await self._execute_mc("!tpToPlayer", [player_name])


class FollowPlayerTool(MCToolBase):
    """持续跟随指定玩家。"""

    name: str = "mc_follow_player"
    description: str = (
        "持续跟随指定玩家。"
        "参数：player_name 为目标玩家名称，follow_dist 为跟随距离（格，默认4.0）。"
        "这是一个持续动作，会一直跟随直到被中断。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "目标玩家名称"],
        follow_dist: Annotated[float, "跟随距离（格）"] = 4.0,
    ) -> tuple[bool, str]:
        """执行跟随玩家命令。"""
        return await self._execute_mc("!followPlayer", [player_name, follow_dist])


class GoToCoordsTool(MCToolBase):
    """前往指定坐标。"""

    name: str = "mc_go_to_coords"
    description: str = (
        "前往指定坐标。"
        "参数：x, y, z 为目标坐标，closeness 为靠近距离（格，默认2.0）。"
    )

    async def execute(
        self,
        x: Annotated[float, "X 坐标"],
        y: Annotated[float, "Y 坐标"],
        z: Annotated[float, "Z 坐标"],
        closeness: Annotated[float, "靠近距离（格）"] = 2.0,
    ) -> tuple[bool, str]:
        """执行前往坐标命令。"""
        return await self._execute_mc("!goToCoordinates", [x, y, z, closeness])


class SearchBlockTool(MCToolBase):
    """搜索并前往最近的指定方块。"""

    name: str = "mc_search_block"
    description: str = (
        "搜索并前往最近的指定方块。"
        "参数：type 为方块名称（如 diamond_ore），search_range 为搜索范围（格，最小32）。"
    )

    async def execute(
        self,
        type: Annotated[str, "方块名称，如 diamond_ore"],
        search_range: Annotated[float, "搜索范围（格）"] = 32.0,
    ) -> tuple[bool, str]:
        """执行搜索方块命令。"""
        return await self._execute_mc("!searchForBlock", [type, max(search_range, 32.0)])


class SearchEntityTool(MCToolBase):
    """搜索并前往最近的指定实体。"""

    name: str = "mc_search_entity"
    description: str = (
        "搜索并前往最近的指定实体。"
        "参数：type 为实体类型（如 cow），search_range 为搜索范围（格，范围32-512）。"
    )

    async def execute(
        self,
        type: Annotated[str, "实体类型，如 cow"],
        search_range: Annotated[float, "搜索范围（格）"] = 64.0,
    ) -> tuple[bool, str]:
        """执行搜索实体命令。"""
        search_range = max(32.0, min(search_range, 512.0))
        return await self._execute_mc("!searchForEntity", [type, search_range])


class MoveAwayTool(MCToolBase):
    """远离当前位置。"""

    name: str = "mc_move_away"
    description: str = "远离当前位置。参数：distance 为远离距离（格）。"

    async def execute(
        self,
        distance: Annotated[float, "远离距离（格）"] = 16.0,
    ) -> tuple[bool, str]:
        """执行远离命令。"""
        return await self._execute_mc("!moveAway", [distance])


class GoToPlaceTool(MCToolBase):
    """前往已保存的位置。"""

    name: str = "mc_go_to_place"
    description: str = "前往已保存的位置。参数：name 为位置名称（需先用 mc_remember_place 保存）。"

    async def execute(
        self,
        name: Annotated[str, "位置名称"],
    ) -> tuple[bool, str]:
        """执行前往已保存位置命令。"""
        return await self._execute_mc("!goToRememberedPlace", [name])


class GoToBedTool(MCToolBase):
    """前往最近的床睡觉。"""

    name: str = "mc_go_to_bed"
    description: str = "前往最近的床睡觉。无参数。"

    async def execute(self) -> tuple[bool, str]:
        """执行前往床睡觉命令。"""
        return await self._execute_mc("!goToBed", [])


class StayTool(MCToolBase):
    """原地停留。"""

    name: str = "mc_stay"
    description: str = "原地停留指定时间。参数：seconds 为停留秒数（-1=无限停留）。"

    async def execute(
        self,
        seconds: Annotated[int, "停留秒数（-1=无限）"] = 30,
    ) -> tuple[bool, str]:
        """执行原地停留命令。"""
        return await self._execute_mc("!stay", [seconds])


class DigDownTool(MCToolBase):
    """向下挖掘。"""

    name: str = "mc_dig_down"
    description: str = "向下挖掘指定距离。参数：distance 为挖掘深度（格）。"

    async def execute(
        self,
        distance: Annotated[int, "挖掘深度（格）"] = 10,
    ) -> tuple[bool, str]:
        """执行向下挖掘命令。"""
        return await self._execute_mc("!digDown", [distance])


class GoToSurfaceTool(MCToolBase):
    """前往地表。"""

    name: str = "mc_go_to_surface"
    description: str = "前往地表。无参数。适用于在地下时回到地面。"

    async def execute(self) -> tuple[bool, str]:
        """执行前往地表命令。"""
        return await self._execute_mc("!goToSurface", [])


class RememberPlaceTool(MCToolBase):
    """保存当前位置。"""

    name: str = "mc_remember_place"
    description: str = "保存当前位置。参数：name 为位置名称。后续可用 mc_go_to_place 前往。"

    async def execute(
        self,
        name: Annotated[str, "位置名称"],
    ) -> tuple[bool, str]:
        """执行保存位置命令。"""
        return await self._execute_mc("!rememberHere", [name])
