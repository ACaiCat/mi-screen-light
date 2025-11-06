# mi-screen-light

根据用户活动自动控制电脑的屏幕挂灯或者桌面台灯!

## 功能

- 当检测到用户活动时，自动打开米家智能灯
- 当用户空闲一段时间，自动关闭米家智能灯

## 快速开始

1. 克隆仓库
   ``shell
   git clone https://github.com/ACaiCat/mi-screen-light.git
   cd mi-screen-light
   uv sync
   ``
2. 导出设备IP和Token
   使用https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor导出米家设备的内网地址和密钥
3. 运行启动脚本`run_monitor.bat`
4. 修改配置文件
5. 将`run_monitor.bat`添加到启动项或者计划任务的系统启动中