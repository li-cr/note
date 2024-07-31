```shell file:"docker"
// 运行
docker run [OPTIONS] IMAGE [COMMAND] [ARG...] 

// 列出所有镜像
docker images [OPTIONS] [REPOSITORY[:TAG]]
// 列出所有运行的容器
docker ps [OPTIONS]

// 停止 重启 删除 容器
docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker restart [OPTIONS] CONTAINER [CONTAINER...]
docker kill [OPTIONS] CONTAINER [CONTAINER...]

// 删除容器（rm） 镜像（rmi）
docker rm [OPTIONS] CONTAINER [CONTAINER...]   docker rmi [OPTIONS] IMAGE [IMAGE...]

```