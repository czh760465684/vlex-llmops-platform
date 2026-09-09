# Bug Report - 2025年02月01肉

## Bug 1: 应用编排页面内置工具图标获取异常

### 问题描述

在应用编排页面中，添加内置工具后，在编排页面 icon 图标显示不正常。

### 复现步骤

1.打开应用编排，点击 `添加工具`，选择任意 `内置工具`；
2.在应用编排页面可以看到 `工具图标` 显示异常；

### 影响访问

应用编排页面添加内置工具时，图标显示异常。

### 解决方案

在前面的课时中，我们使用 Nginx 将 UI 与 API 服务统一到统一域名下，不过没有修改内置工具图标的 URL 地址，导致实际并没有使用正确的
URL 获取图标。
修改后端返回的 `图标URL` 地址即可。

```python
# internal/service/app_config_service.py

def _process_and_validate_tools(self, origin_tools: list[dict]) -> tuple[list[dict], list[dict]]:
    ...
    tools.append({
        "type": "builtin_tool",
        "provider": {
            "id": provider_entity.name,
            "name": provider_entity.name,
            "label": provider_entity.label,
            "icon": f"/api/builtin-tools/{provider_entity.name}/icon",
            "description": provider_entity.description,
        },
        "tool": {
            "id": tool_entity.name,
            "name": tool_entity.name,
            "label": tool_entity.label,
            "description": tool_entity.description,
            "params": tool["params"],
        }
    })
    ...
```