# Appium UI Automation Demo

用于给公司测试同学的Appium-UI自动化示例（Android）

## 项目结构

- `DemoTrade` 类：包含主要的测试逻辑。
- `test_demo_trade` 方法：执行 UI 自动化测试。

## 环境要求

- Python 3.x
- Appium Server
- Android SDK
- 已连接的 Android 设备或模拟器

## 安装依赖

首先，确保你已经安装了 `Appium` 和 `selenium` Python 包。你可以使用以下命令安装这些依赖项：

```bash
pip install requirements.txt
```

## 使用方法
启动 Appium Server：确保 Appium Server 已经在本地运行，默认端口为 4723。

连接设备或启动模拟器 ：确保你的设备通过 USB 连接到计算机，或者启动一个 Android 模拟器。

运行测试脚本 ： 克隆这个仓库，然后在项目目录下运行以下命令：
```bash
python test.py
```
查看输出结果 ：脚本会输出测试的结果，包括识别到的页面元素及其对应的操作。


## 示例功能
启动指定的 Android 应用

识别并点击页面上的特定元素

获取并比较页面元素的文本值

输出测试结果

