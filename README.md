# mi-screen-light

根据用户活动自动控制电脑的屏幕挂灯或者桌面台灯!

> [!IMPORTANT]
> 本项目只支持Windows

## 功能

- 当检测到用户活动时，自动打开米家智能灯
- 当用户空闲一段时间，自动关闭米家智能灯

## 快速开始

1. 克隆仓库

   ```shell
   git clone https://github.com/ACaiCat/mi-screen-light.git
   cd mi-screen-light
   uv sync
   ```

2. 导出设备IP和Token (最好在路由器中固定设备IP)
   使用[[Xiaomi-cloud-tokens-extractor]](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)导出米家设备的内网地址和密钥  
   ![](https://github.com/user-attachments/assets/e2351f86-f641-4a74-9200-61601b23566d)

3. 运行启动脚本`run_monitor.bat`
4. 修改配置文件

   ```json
   {
   "light_ip": "192.168.31.43",           // 米家设备的IP地址
   "light_token": "a950e512ab0a8ef64300be4fb5a64525",  // 设备认证Token
   "auto_open": true,                     // 检测到用户活动时自动开灯
   "auto_close": true,                    // 用户空闲超时后自动关灯
   "sync_status_interval": 15,            // 状态同步间隔（秒）
   "auto_close_idle_timeout": 10          // 空闲超时时间（秒）
   }
   ```

5. 将`run_monitor.bat`添加到启动项或者计划任务的系统启动中

> [!NOTE]
> 计划任务设置
> "只在用户登录时运行"
