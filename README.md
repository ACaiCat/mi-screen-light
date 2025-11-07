# mi-screen-light

根据用户活动自动控制电脑的屏幕挂灯或者桌面台灯!

> [!IMPORTANT]
> 本项目只支持Windows

## 功能

- 当检测到用户活动时，自动打开米家智能灯
- 当用户空闲一段时间，自动关闭米家智能灯

## 快速开始

1. 在Release中下载控制程序

2. 导出设备IP和Token (最好在路由器中固定设备IP)
   使用[[Xiaomi-cloud-tokens-extractor]](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)
   导出米家设备的内网地址和密钥  
   ![](https://github.com/user-attachments/assets/e2351f86-f641-4a74-9200-61601b23566d)

3. 运行一次控制程序，生成配置文件
4. 修改配置文件

   ```jsonc
   {
   "light_ip": "192.168.xx.xx",           // 米家设备的IP地址
   "light_token": "xxxxxx",               // 设备认证Token
   "auto_open": true,                     // 检测到用户活动时自动开灯
   "auto_close": true,                    // 用户空闲超时后自动关灯
   "sync_status_interval": 15,            // 状态同步间隔（秒）
   "auto_close_idle_timeout": 10          // 空闲超时时间（秒）
   }
   ```

5. 将`mi-screen-light.exe`添加到启动项或者计划任务的系统启动中

```xml
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2025-11-07T00:29:45.1348228</Date>
    <Author>Cai</Author>
    <URI>\屏幕挂灯</URI>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-3449202476-435703035-151111829-1001</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\mi-screen-light\dist\mi-screen-light.exe</Command>
      <WorkingDirectory>C:\mi-screen-light\dist</WorkingDirectory>
    </Exec>
  </Actions>
</Task>
```

> [!NOTE]
> 计划任务设置  
> "只在用户登录时运行"  
> "用户登录时运行"  
> 注意配置其实目录为程序根目录
