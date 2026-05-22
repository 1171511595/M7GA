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

# class BLiveModel(QThread):
class BLiveModel():
    def __init__(self,bliveID:int,bliveSESSDATA:str):
        # super.__init__()
        # 初始化各类内变量
        self._bliveID = bliveID
        self._bliveSESSDATA = bliveSESSDATA
        self._session: Optional[aiohttp.ClientSession] = None
        self._count = 0

    # 信号：返回直播间心跳信息
    result_heart = Signal(str);

    def run(self):
        """
        启动异步任务
        """
        asyncio.run(self.main())

    async def main(self):
        """
        主任务
        """
        # 初始化aiohttp session 并注入cookie
        # 先创建一个cookie容器
        self._cookies = http.cookies.SimpleCookie()
        # 构建B站登录态的Cookie
        self._cookies['SESSDATA'] = self._bliveSESSDATA
        self._cookies['SESSDATA']['domain'] = 'bilibili.com'
        # 创建异步HTTP会话
        self._session = aiohttp.ClientSession()
        # 把Cookie注入到session中
        self._session.cookie_jar.update_cookies(self._cookies)

        # 对单个直播间的监听
        try:
            await self.run_single_client()
        # 无论是否报错，最后都确保关闭了session
        finally:
            await self._session.close()


    async def run_single_client(self):
        """
        演示监听一个直播间
        """
        # 以登录态session创建一个B站的直播客户端
        client = blivedm.BLiveClient(self._bliveID, session=self._session)
        # 绑定弹幕处理器
        handler = self.MyHandler()
        client.set_handler(handler)
        #启动弹幕监听
        client.start()
        try:
            # 永远运行，知道Ctrl+C
            await asyncio.Future()
        finally:
            # 用于确保资源真的被释放
            await client.stop_and_close()

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
            普通弹幕消息,uname:用户名,msg:弹幕内容
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


if __name__ == '__main__':
    # Python异步程序的标准启动方式
    # 自动创建事件循环并运行main
    # asyncio.run(main())
    threadBlive = BLiveModel(24056350,'8d936c43%2C1795006570%2Cca220%2A51')
    threadBlive.run()
