"""Mindcraft 扩展能力插件配置。

参考 [`plugins/snowluma_adapter/config.py`](plugins/snowluma_adapter/config.py:9) 的配置模式。
"""

from __future__ import annotations

from typing import ClassVar

from src.core.components.base.config import BaseConfig, Field, SectionBase, config_section


class MindcraftExtensionConfig(BaseConfig):
    """Mindcraft 扩展能力配置。

    配置文件路径：``config/plugins/mindcraft_extension/config.toml``
    """

    name: ClassVar[str] = "config"
    description: ClassVar[str] = "Mindcraft 扩展能力配置"

    @config_section("plugin", title="插件设置", tag="plugin")
    class PluginSection(SectionBase):
        """插件基本配置。"""

        enabled: bool = Field(
            default=True,
            description="是否启用 Mindcraft 扩展能力",
            label="启用",
            tag="plugin",
        )
        config_version: str = Field(
            default="0.1.0",
            description="配置版本号",
            label="配置版本",
            tag="plugin",
        )

    # 实例字段声明：让 Pydantic 能正确实例化配置节
    plugin: PluginSection = Field(default_factory=PluginSection)
