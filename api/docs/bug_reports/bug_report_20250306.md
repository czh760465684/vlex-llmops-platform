# Bug Report - 2025年03月06日

## Bug 1: 辅助Agent智能体的消息调用来源修正

### 问题描述

在辅助Agent智能体对话页面，对话添加的消息来源是 `debugger`，后端进行语音输出时会对debugger的应用进行检测，会提示找不到该应用。

### 复现步骤

1.打开 LLMOps 站点主页，随意发送一条消息；
2.然后点击 `语音播放`，会提示"该消息会话归属应用不存在或校验失败，请核实后重试";

### 影响访问

站点辅助Agent页面无法播放语音。

### 解决方案

修正 `assistant_agent_service.py` 的 `chat()` 方法中的调用来源即可，从 `InvokeFrom.DEBUGGER`
改成 `InvokeFrom.ASSISTANT_AGENT`。

```python
# internal/service/assistant_agent_service.py

message = self.create(
    Message,
    app_id=assistant_agent_id,
    conversation_id=conversation.id,
    invoke_from=InvokeFrom.ASSISTANT_AGENT,
    created_by=account.id,
    query=req.query.data,
    image_urls=req.image_urls.data,
    status=MessageStatus.NORMAL,
)
```