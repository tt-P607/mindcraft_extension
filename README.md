# mindcraft_extension

Minecraft（Mindcraft）MoFox 扩展能力插件：提供 Minecraft 的游戏动作、查询和系统能力作为 MoFox Tool 组件。

## 功能

约 40 个 MC Tool 组件，覆盖：

- **移动类**：前往玩家 / 瞬移（`!tpToPlayer`）/ 跟随 / 前往坐标 / 搜索方块 / 搜索实体 / 远离 / 前往地点 / 睡觉 / 停留 / 下挖 / 上浮 / 记忆地点
- **交互类**：采集方块 / 放置方块 / 攻击实体 / 攻击玩家 / 给予物品 / 食用 / 装备 / 箱子存取 / 丢弃 / 合成 / 熔炼 / 清理熔炉 / 使用工具 / 村民交易 / 看向玩家 / 看向坐标 / 模式开关 / 设定目标 / 结束目标 / 自定义代码动作 / Bot 间对话
- **查询类**：状态 / 背包 / 附近方块 / 可合成物 / 附近实体 / 模式 / 已存地点 / 合成计划
- **系统类**：停止 / 清空聊天 / 闭嘴 / 重启

所有工具通过 `mindcraft_adapter` 的 WebSocket 通道下发 `execute_action` 到 Mindcraft JS 侧执行。

## 依赖

- MoFox 核心 `>= 1.2.0-rc.2`
- 配套插件：[`mindcraft_adapter`](https://github.com/tt-P607/mindcraft_adapter)（WebSocket 通信通道）
- 配套插件：[`mindcraft_chatter`](https://github.com/tt-P607/mindcraft_chatter)（Actor / GameAgent 会话）
- Mindcraft 本体：[`mindcraft`](https://github.com/tt-P607/mindcraft)（MoFox 定制版 JS Bridge）

## 安装

将本插件目录放入 MoFox 的 `plugins/` 目录，确保 `mindcraft_adapter` 已启用且 Mindcraft Bridge 已连接。

## 组件

所有组件 signature 形如 `mindcraft_extension:tool:mc_<name>`，完整清单见 [`manifest.json`](manifest.json:1)。

## 配置

见 [`config.py`](config.py:1)，主要为插件总开关。

## 验证

```bash
uv run ruff check plugins/mindcraft_extension
```

启动后在 MC 中让 Bot 执行任意动作（如"过来我这里"、"挖 10 个石头"、"去睡觉"），
Bot 应能通过 Tool 调用完成对应操作。

## 开源协议

[MIT](LICENSE)
