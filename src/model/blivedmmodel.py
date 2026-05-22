# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread, Signal
# asyncio是Python的异步编程核心库，用来async/await、协程、并发任务
import asyncio
# 用于操作HTTP cookie，用于设置B站登录状态
import http.cookies
# 随机模块
import random
# 类型注解支持
from typing import Optional
# 异步HTTP客户端，用于WebSocket/长连接
import aiohttp
# blivedm：核心客户端
import blivedm
# web_models：存放各种弹幕消息的数据结构
import blivedm.models.web as web_models

# 测试用的直播间ID，ID来源于直播间的URL
# 直播间ID的取值看直播间URL
TEST_ROOM_IDS = [
    12235923,
    14327465,
    21396545,
    21449083,
    23105590,
]

# 这里填一个已登录账号的cookie的SESSDATA字段的值
# 不填也可以连接，但是收到弹幕的用户名会打码，UID会变成0
# ==============================================================================
#      如果你是从 `Chrome开发者工具 - 应用` 复制cookie的，不要勾选“显示已解码的网址”
# ==============================================================================
# 登录态SESSDATA，有SESSDATA才能看到真实的用户名
SESSDATA = ''
#全局共享的aiohttp Session，全局共享的HTTP/WS会话
session: Optional[aiohttp.ClientSession] = None

# 程序入口，异步主函数
async def main():
    # 初始化aiohttp session 并注入cookie
    init_session()
    # 演示对单个直播间的监听和对多个直播间的监听
    try:
        await run_single_client()
        await run_multi_clients()
    # 无论是否报错，最后都确保关闭了session
    finally:
        await session.close()


def init_session():
    """
    初始化session
    """
    # 先创建一个cookie容器
    cookies = http.cookies.SimpleCookie()
    # 构建B站登录态的Cookie
    cookies['SESSDATA'] = SESSDATA
    cookies['SESSDATA']['domain'] = 'bilibili.com'
    # 创建异步HTTP会话
    global session
    session = aiohttp.ClientSession()
    # 把Cookie注入到session中
    session.cookie_jar.update_cookies(cookies)


async def run_single_client():
    """
    演示监听一个直播间
    """
    # 随机选择一个直播间
    room_id = random.choice(TEST_ROOM_IDS)
    # 以登录态session创建一个B站的直播客户端
    client = blivedm.BLiveClient(room_id, session=session)
    # 绑定弹幕处理器
    handler = MyHandler()
    client.set_handler(handler)
    #启动弹幕监听
    client.start()
    try:
        # 演示5秒后停止
        await asyncio.sleep(5)
        client.stop()
        # 等待客户端真正退出
        await client.join()
    finally:
        # 用于确保资源真的被释放
        await client.stop_and_close()


async def run_multi_clients():
    """
    演示同时监听多个直播间
    """
    # 为每个直播间都创建一个客户端
    clients = [blivedm.BLiveClient(room_id, session=session) for room_id in TEST_ROOM_IDS]
    # 绑定弹幕处理器
    handler = MyHandler()
    # 将直播客户端全部启动
    for client in clients:
        client.set_handler(handler)
        client.start()

    try:
        # 并发的等待所有客户端，只要有一个客户端退出，整体就结束
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        # 安全的关闭所有的资源
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))


class MyHandler(blivedm.BaseHandler):
    """
    弹幕事件处理类
    blivedm.BaseHandler 继承blivedm的事件基类
    """
    # # 演示如何添加自定义回调
    # _CMD_CALLBACK_DICT = blivedm.BaseHandler._CMD_CALLBACK_DICT.copy()
    #
    # # 看过数消息回调
    # def __watched_change_callback(self, client: blivedm.BLiveClient, command: dict):
    #     print(f'[{client.room_id}] WATCHED_CHANGE: {command}')
    # _CMD_CALLBACK_DICT['WATCHED_CHANGE'] = __watched_change_callback  # noqa

    def _on_heartbeat(self, client: blivedm.BLiveClient, message: web_models.HeartbeatMessage):
        """
        心跳包
        """
        print(f'[{client.room_id}] 心跳')

    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        """
        普通弹幕消息，uname：用户名，msg：弹幕内容
        """
        print(f'[{client.room_id}] {message.uname}：{message.msg}')

    def _on_gift(self, client: blivedm.BLiveClient, message: web_models.GiftMessage):
        """
        礼物消息，送礼人、礼物名、数量、价格
        """
        print(f'[{client.room_id}] {message.uname} 赠送{message.gift_name}x{message.num}'
              f' （{message.coin_type}瓜子x{message.total_coin}）')

    # def _on_buy_guard(self, client: blivedm.BLiveClient, message: web_models.GuardBuyMessage):
    #     print(f'[{client.room_id}] {message.username} 上舰，guard_level={message.guard_level}')

    def _on_user_toast_v2(self, client: blivedm.BLiveClient, message: web_models.UserToastV2Message):
        """
        上舰消息（大航海）
        """
        # 过滤掉某些重复/系统通知
        if message.source != 2:
            print(f'[{client.room_id}] {message.username} 上舰，guard_level={message.guard_level}')

    def _on_super_chat(self, client: blivedm.BLiveClient, message: web_models.SuperChatMessage):
        """
        付费醒目留言
        """
        print(f'[{client.room_id}] 醒目留言 ¥{message.price} {message.uname}：{message.message}')

    # def _on_interact_word_v2(self, client: blivedm.BLiveClient, message: web_models.InteractWordV2Message):
    #     if message.msg_type == 1:
    #         print(f'[{client.room_id}] {message.username} 进入房间')

class BLiveModel:
    # def __init__(self, room_id):
    #     self.room_id = room_id
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def decrement(self):
        self._count -= 1

    @property
    def count(self):
        return self._count
    

if __name__ == '__main__':
    # Python异步程序的标准启动方式
    # 自动创建事件循环并运行main
    asyncio.run(main())