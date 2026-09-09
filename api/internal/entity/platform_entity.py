#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/01/18 19:35
@Author  : thezehui@gmail.com
@File    : platform_entity.py
"""
from enum import Enum


class WechatConfigStatus(str, Enum):
    """微信配置状态"""
    CONFIGURED = "configured"  # 已配置
    UNCONFIGURED = "unconfigured"  # 未配置
