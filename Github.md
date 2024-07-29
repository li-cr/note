### <font color="red">proxy</font>

```shell file="~"
# 查看代理
git config --global l
# 修改代理
git config --global http.proxy http://127.0.0.1:7890
# 取消代理
git config --global --unset http.proxy
```

### <font color="red">回退版本</font>

```shell file="~";
# 创建新分支
git checkout -b "dawdaw"
# reset hard
git reset commit-name hard
# 强制提交， 记得保存下仓库
git pull --force
``` 

	
