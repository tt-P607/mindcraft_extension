"""交互类 MC Tool 组件。

对应 Mindcraft 的交互相关动作命令（收集、放置、攻击、合成、熔炼等）。
参考源码：[`E:/mindcraft/src/agent/commands/actions.js`](E:/mindcraft/src/agent/commands/actions.js:28)
"""

from __future__ import annotations

from typing import Annotated

from .base import MCToolBase


class CollectBlocksTool(MCToolBase):
    """收集指定方块。"""

    name: str = "mc_collect_blocks"
    description: str = (
        "收集指定数量的方块。"
        "参数：type 为方块名称（如 oak_log），num 为数量。"
        "超时时间为10分钟。"
    )

    async def execute(
        self,
        type: Annotated[str, "方块名称，如 oak_log"],
        num: Annotated[int, "数量"] = 1,
    ) -> tuple[bool, str]:
        """执行收集方块命令。"""
        return await self._execute_mc("!collectBlocks", [type, num], timeout=600.0)


class PlaceBlockTool(MCToolBase):
    """在当前位置放置方块。"""

    name: str = "mc_place_block"
    description: str = "在当前位置放置方块。参数：type 为方块或物品名称。"

    async def execute(
        self,
        type: Annotated[str, "方块或物品名称"],
    ) -> tuple[bool, str]:
        """执行放置方块命令。"""
        return await self._execute_mc("!placeHere", [type])


class AttackTool(MCToolBase):
    """攻击最近的指定类型实体。"""

    name: str = "mc_attack"
    description: str = "攻击最近的指定类型实体。参数：type 为实体类型（如 zombie）。"

    async def execute(
        self,
        type: Annotated[str, "实体类型，如 zombie"],
    ) -> tuple[bool, str]:
        """执行攻击命令。"""
        return await self._execute_mc("!attack", [type])


class AttackPlayerTool(MCToolBase):
    """攻击指定玩家。"""

    name: str = "mc_attack_player"
    description: str = "攻击指定玩家。参数：player_name 为玩家名称。"

    async def execute(
        self,
        player_name: Annotated[str, "玩家名称"],
    ) -> tuple[bool, str]:
        """执行攻击玩家命令。"""
        return await self._execute_mc("!attackPlayer", [player_name])


class GiveItemTool(MCToolBase):
    """给予玩家物品。"""

    name: str = "mc_give_item"
    description: str = (
        "给予指定玩家物品。"
        "参数：player_name 为玩家名称，item_name 为物品名称，num 为数量。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "玩家名称"],
        item_name: Annotated[str, "物品名称"],
        num: Annotated[int, "数量"] = 1,
    ) -> tuple[bool, str]:
        """执行给予物品命令。"""
        return await self._execute_mc("!givePlayer", [player_name, item_name, num])


class ConsumeTool(MCToolBase):
    """食用或饮用物品。"""

    name: str = "mc_consume"
    description: str = "食用或饮用物品。参数：item_name 为物品名称。"

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
    ) -> tuple[bool, str]:
        """执行食用命令。"""
        return await self._execute_mc("!consume", [item_name])


class EquipTool(MCToolBase):
    """装备物品。"""

    name: str = "mc_equip"
    description: str = "装备指定物品到合适的槽位。参数：item_name 为物品名称。"

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
    ) -> tuple[bool, str]:
        """执行装备命令。"""
        return await self._execute_mc("!equip", [item_name])


class PutInChestTool(MCToolBase):
    """放入箱子。"""

    name: str = "mc_put_in_chest"
    description: str = (
        "将物品放入附近的箱子。"
        "参数：item_name 为物品名称，num 为数量（-1=全部）。"
    )

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
        num: Annotated[int, "数量（-1=全部）"] = -1,
    ) -> tuple[bool, str]:
        """执行放入箱子命令。"""
        return await self._execute_mc("!putInChest", [item_name, num])


class TakeFromChestTool(MCToolBase):
    """从箱子取出。"""

    name: str = "mc_take_from_chest"
    description: str = (
        "从附近的箱子取出物品。"
        "参数：item_name 为物品名称，num 为数量（-1=全部）。"
    )

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
        num: Annotated[int, "数量（-1=全部）"] = -1,
    ) -> tuple[bool, str]:
        """执行从箱子取出命令。"""
        return await self._execute_mc("!takeFromChest", [item_name, num])


class ViewChestTool(MCToolBase):
    """查看附近箱子。"""

    name: str = "mc_view_chest"
    description: str = "查看附近箱子的内容。无参数。"

    async def execute(self) -> tuple[bool, str]:
        """执行查看箱子命令。"""
        return await self._execute_mc("!viewChest", [])


class DiscardTool(MCToolBase):
    """丢弃物品。"""

    name: str = "mc_discard"
    description: str = (
        "丢弃物品。"
        "参数：item_name 为物品名称，num 为数量（-1=全部）。"
    )

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
        num: Annotated[int, "数量（-1=全部）"] = -1,
    ) -> tuple[bool, str]:
        """执行丢弃物品命令。"""
        return await self._execute_mc("!discard", [item_name, num])


class CraftTool(MCToolBase):
    """合成物品。"""

    name: str = "mc_craft"
    description: str = (
        "合成指定物品。"
        "参数：recipe_name 为合成配方名称（如 oak_planks），num 为数量。"
    )

    async def execute(
        self,
        recipe_name: Annotated[str, "合成配方名称"],
        num: Annotated[int, "数量"] = 1,
    ) -> tuple[bool, str]:
        """执行合成命令。"""
        return await self._execute_mc("!craftRecipe", [recipe_name, num])


class SmeltTool(MCToolBase):
    """熔炼物品。"""

    name: str = "mc_smelt"
    description: str = (
        "在附近熔炉中熔炼物品。"
        "参数：item_name 为物品名称，num 为数量。"
    )

    async def execute(
        self,
        item_name: Annotated[str, "物品名称"],
        num: Annotated[int, "数量"] = 1,
    ) -> tuple[bool, str]:
        """执行熔炼命令。"""
        return await self._execute_mc("!smeltItem", [item_name, num])


class ClearFurnaceTool(MCToolBase):
    """清空熔炉。"""

    name: str = "mc_clear_furnace"
    description: str = "清空最近熔炉中的物品。无参数。"

    async def execute(self) -> tuple[bool, str]:
        """执行清空熔炉命令。"""
        return await self._execute_mc("!clearFurnace", [])


class UseOnTool(MCToolBase):
    """对目标使用工具。"""

    name: str = "mc_use_on"
    description: str = (
        "对目标使用指定工具。"
        "参数：tool_name 为工具名称，target 为目标名称。"
    )

    async def execute(
        self,
        tool_name: Annotated[str, "工具名称"],
        target: Annotated[str, "目标名称"],
    ) -> tuple[bool, str]:
        """执行使用工具命令。"""
        return await self._execute_mc("!useOn", [tool_name, target])


class ShowVillagerTradesTool(MCToolBase):
    """查看村民交易。"""

    name: str = "mc_show_villager_trades"
    description: str = "查看指定村民的交易列表。参数：id 为村民编号。"

    async def execute(
        self,
        id: Annotated[int, "村民编号"],
    ) -> tuple[bool, str]:
        """执行查看村民交易命令。"""
        return await self._execute_mc("!showVillagerTrades", [id])


class TradeWithVillagerTool(MCToolBase):
    """与村民交易。"""

    name: str = "mc_trade_with_villager"
    description: str = (
        "与指定村民进行交易。"
        "参数：id 为村民编号，index 为交易序号，count 为交易次数。"
    )

    async def execute(
        self,
        id: Annotated[int, "村民编号"],
        index: Annotated[int, "交易序号"],
        count: Annotated[int, "交易次数"] = 1,
    ) -> tuple[bool, str]:
        """执行与村民交易命令。"""
        return await self._execute_mc("!tradeWithVillager", [id, index, count])


class LookAtPlayerTool(MCToolBase):
    """看向玩家。"""

    name: str = "mc_look_at_player"
    description: str = (
        "看向指定玩家。"
        "参数：player_name 为玩家名称，direction 为看向方式"
        "（at=直视，with=侧看，默认 at）。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "玩家名称"],
        direction: Annotated[str, "看向方式（at=直视，with=侧看）"] = "at",
    ) -> tuple[bool, str]:
        """执行看向玩家命令。"""
        return await self._execute_mc("!lookAtPlayer", [player_name, direction])


class LookAtPositionTool(MCToolBase):
    """看向坐标。"""

    name: str = "mc_look_at_position"
    description: str = "看向指定坐标。参数：x, y, z 为目标坐标。"

    async def execute(
        self,
        x: Annotated[int, "X 坐标"],
        y: Annotated[int, "Y 坐标"],
        z: Annotated[int, "Z 坐标"],
    ) -> tuple[bool, str]:
        """执行看向坐标命令。"""
        return await self._execute_mc("!lookAtPosition", [x, y, z])


class SetModeTool(MCToolBase):
    """开关自动行为模式。"""

    name: str = "mc_set_mode"
    description: str = (
        "开关自动行为模式。"
        "可用模式：self_preservation, unstuck, cowardice, self_defense, "
        "hunting, item_collecting, torch_placing, elbow_room, idle_staring, cheat。"
        "参数：mode_name 为模式名称，on 为是否开启。"
    )

    async def execute(
        self,
        mode_name: Annotated[str, "模式名称"],
        on: Annotated[bool, "是否开启"] = True,
    ) -> tuple[bool, str]:
        """执行开关模式命令。"""
        return await self._execute_mc("!setMode", [mode_name, on])


class GoalTool(MCToolBase):
    """设置自主目标。"""

    name: str = "mc_goal"
    description: str = (
        "设置自主目标，Bot 将自主循环执行任务直到目标完成。"
        "参数：self_prompt 为目标描述。"
        "设置后 Bot 会持续自主行动，使用 mc_end_goal 结束。"
    )

    async def execute(
        self,
        self_prompt: Annotated[str, "目标描述"],
    ) -> tuple[bool, str]:
        """执行设置自主目标命令。"""
        return await self._execute_mc("!goal", [self_prompt])


class EndGoalTool(MCToolBase):
    """结束自主目标。"""

    name: str = "mc_end_goal"
    description: str = "结束当前的自主目标循环。无参数。"

    async def execute(self) -> tuple[bool, str]:
        """执行结束自主目标命令。"""
        return await self._execute_mc("!endGoal", [])


class NewActionTool(MCToolBase):
    """自定义代码生成动作。"""

    name: str = "mc_new_action"
    description: str = (
        "生成并执行自定义代码动作。需要 Mindcraft 开启 allow_insecure_coding。"
        "参数：prompt 为代码需求描述。"
    )

    async def execute(
        self,
        prompt: Annotated[str, "代码需求描述"],
    ) -> tuple[bool, str]:
        """执行自定义代码生成命令。"""
        return await self._execute_mc("!newAction", [prompt], timeout=600.0)


class StartConversationTool(MCToolBase):
    """开始 Bot 间对话。"""

    name: str = "mc_start_conversation"
    description: str = (
        "与另一个 Bot 开始对话。"
        "参数：player_name 为目标 Bot 名称，message 为对话内容。"
    )

    async def execute(
        self,
        player_name: Annotated[str, "目标 Bot 名称"],
        message: Annotated[str, "对话内容"],
    ) -> tuple[bool, str]:
        """执行开始对话命令。"""
        return await self._execute_mc("!startConversation", [player_name, message])


class EndConversationTool(MCToolBase):
    """结束 Bot 间对话。"""

    name: str = "mc_end_conversation"
    description: str = "结束与指定 Bot 的对话。参数：player_name 为目标 Bot 名称。"

    async def execute(
        self,
        player_name: Annotated[str, "目标 Bot 名称"],
    ) -> tuple[bool, str]:
        """执行结束对话命令。"""
        return await self._execute_mc("!endConversation", [player_name])
