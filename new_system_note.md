## ubuntu18.04双系统

- Device for boot loader (EFI分区与Win10在一起)
- sda4 选择 ext4 格式 &emsp;|&emsp; 挂载在 / &emsp;|&emsp; 并选择格式化掉该分区 

## graphics driver

- graphics driver ppa &emsp;添加nvidia官方库
- 在软件更新器中选择显驱版本
- nvidia-prime，设置独显为默认显卡:
	- sudo apt install nvidia-prime
	- sudo prime-select nvidia
- 在 /etc/modprobe.d/blacklist-nouveau.conf 中禁用默认显卡

## cuda cudnn
- add PATH
- cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2

## clash
p
- github : clash -> release -> amd64
- gunzip
- cp to /usr/bin
- mv ./软件 ./clash &emsp;相当于在本文件夹中重命名
- chmod 755 clash &emsp;更改clash权限
- (chown /root /root 更改累和组)
- 配置systemd的启动 -> clash.service  `见图片`
- clash 配置文件  &emsp;from cylink  `见文件`
- cp to /etc/clash
- ln -sf ./配置文件 ./config.yaml
- yacd可看了（正常的话）
- 配置本地代理127.0.0.1:7890，yacd socks:7891
- etc/environment `见图片`

- git config proxy: git config --global https.proxy http://127.0.0.1:7890

- install gh: https://github.com/cli/cli/blob/trunk/docs/install_linux.md

## 取消sudo密码
- sudo EDITOR=vim visudo
- 添加`NOPASSWD: `

## others
- deb：sudo apt install
- run：sudo
- chmod rwx | rwx | rwx
    - `+x` root、group、user全部增加执行权限
    - `777` r4 w2 x1
- htop 任务管理器
- sudo fdisk -l查看硬盘管理
