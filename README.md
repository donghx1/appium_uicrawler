# appium_uicrawler
python appium 实现UI遍历



appium --base-path /wd/hub --port 4723 --allow-insecure adb_connect


# 错误： import cv2

pip uninstall numpy
pip install --upgrade numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
pip uninstall opencv-python
pip install --upgrade opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

# 错误：from androguard.core.bytecodes.apk import APK

from androguard.misc import AnalyzeAPK
 apk, _, _ = AnalyzeAPK(filepath)

------------------------------------------------------------------------------------------------

# 安装 ADB


# 错误 failed to open device: Access denied (insufficient permissions) 表示 ADB 无法访问你的 USB 设备，通常是因为权限问题。以下是解决方法：

# 下载 ADB 工具的压缩包（Linux 版本）
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
# 解压下载的文件
unzip platform-tools-latest-linux.zip -d .

# 将 platform-tools 路径写入到环境变量
echo 'export PATH=$PATH:~/workspace/platform-tools' >> ~/.bashrc

# 使配置生效
source ~/.bashrc


1. 检查 udev 规则（Linux 权限管理）

步骤 1: 创建 ADB 规则文件

在 CentOS 下，为 ADB 设备设置 udev 规则，允许当前用户访问 USB 设备：

sudo nano /etc/udev/rules.d/51-android.rules

在文件中添加以下内容（用于识别 Android 设备）：

SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="12d1", MODE="0666", GROUP="plugdev"

	•	idVendor 是 Android 设备的厂商 ID（Vendor ID）。
	•	你可以通过 lsusb 命令找到你的设备的 Vendor ID：

lsusb

步骤 2: 修改文件权限

确保 udev 规则文件具有正确的权限：

sudo chmod a+r /etc/udev/rules.d/51-android.rules

步骤 3: 重启 udev 服务

使规则生效，重启 udev：

sudo udevadm control --reload-rules
sudo udevadm trigger

步骤 4: 重启 ADB 服务

重新启动 ADB 服务并查看设备：

adb kill-server
adb start-server
adb devices

2. 添加用户到 plugdev 组

如果你的系统使用 plugdev 组来管理 USB 权限，确保你的用户属于 plugdev 组：

sudo usermod -aG plugdev $USER

然后重新登录当前用户会话或重启系统。

3. 运行 ADB 服务为 root 用户（临时解决）

如果权限问题依旧存在，可以尝试以 root 身份启动 ADB 服务：

sudo adb kill-server
sudo adb start-server
adb devices

4. 检查 SELinux 状态

在 CentOS 上，SELinux 可能会阻止 ADB 访问 USB 设备。可以将 SELinux 暂时设为 permissive 模式测试：

sudo setenforce 0
adb kill-server
adb start-server
adb devices

注意：设置为 0 后 SELinux 会进入宽松模式，重启后会恢复默认配置。

5. 验证设备连接

重新连接 Android 设备，并确认 USB 调试 已开启。使用以下命令查看设备连接状态：

adb devices

总结

通常，设置正确的 udev 规则后即可解决 ADB 设备权限问题。如果问题仍然存在，可以尝试临时使用 root 权限运行 ADB 服务。如果有进一步错误，请分享详细日志。

------------------------------------------------------------------------------------------------


# 安装 Android SDK


要在 CentOS Stream 9 上安装 Android SDK，你可以按照以下步骤进行：

1. 准备系统环境

首先确保系统已经安装必要的软件依赖和工具。

更新系统

sudo dnf update -y

安装必备工具

sudo dnf install -y wget unzip java-11-openjdk-devel

	Android SDK 需要 Java 环境，java-11-openjdk-devel 提供了 JDK 11。

2. 下载 Android SDK 命令行工具

Android SDK 命令行工具（Command Line Tools）是 Android SDK 的一部分。你可以通过官方网站或以下命令直接下载。

创建 SDK 目录

mkdir -p ~/workspace/android-sdk/cmdline-tools
cd ~/workspace/android-sdk/cmdline-tools

下载命令行工具（适用于 Linux）

wget https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip

	注意：commandlinetools-linux 的版本号可能会更新，可以从 Android SDK 下载页面 获取最新链接。

解压压缩包

unzip commandlinetools-linux-*.zip
mv cmdline-tools tools

3. 配置环境变量

为 Android SDK 配置环境变量，以便可以从命令行访问 sdkmanager 和其他工具。

编辑用户的 Shell 配置文件（如 .bashrc 或 .zshrc）

nano ~/.bashrc

添加以下内容

export ANDROID_HOME=~/workspace/android-sdk
export ANDROID_SDK_ROOT=~/workspace/android-sdk
export PATH=$ANDROID_HOME/cmdline-tools/tools/bin:$ANDROID_HOME/platform-tools:$PATH

使配置立即生效

source ~/.bashrc

4. 安装 SDK 平台工具

使用 sdkmanager 安装必要的 SDK 组件。

验证 sdkmanager

sdkmanager --version

接受许可协议

首次运行时，执行以下命令以接受协议：

sdkmanager --licenses

根据提示输入 y 来接受协议。

安装平台工具和构建工具

sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"

	•	platform-tools：包含 adb 等常用工具。
	•	platforms;android-XX：指定 Android API 版本。
	•	build-tools;XX.0.0：Android 构建工具。

5. 验证安装

检查 adb 命令是否可用

adb version

检查 SDK 路径和组件

sdkmanager --list

6. 使用 Android SDK

现在 Android SDK 已安装完成，你可以使用 adb、sdkmanager 等工具进行 Android 开发或测试。

例如：
	•	通过 adb 管理连接的 Android 设备。
	•	通过 sdkmanager 安装更多组件或升级 SDK。

完整路径示例
	•	SDK 路径：~/android-sdk
	•	平台工具路径：~/android-sdk/platform-tools

以上步骤适用于 CentOS Stream 9，确保网络畅通，并根据需求安装特定的 Android 组件。