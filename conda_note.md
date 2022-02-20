# conda指令
>可以通过-n指定环境，否则在当前活跃的环境下执行相应命令
1. 查看已有环境		`conda env list`
2. 创建环境		`conda cteate -n <env_name>(<packages> eg.python=3.6)`
3. 激活环境		`conda activate <env_name>`
4. 退出环境		`conda deactivate`
5. 删除环境		`conda env remove -n <env_name>`
6. 查看已安装包(base)	`conda list`
7. 查看指定环境下的包	`conda list -n <env_name>`
9. 查询包		`conda search <package_name>`
10. 安装包		`conda install <package_name>`
11. 更新包		`conda update <package_name>`
12. 卸载包		`conda remove <package_name>`
