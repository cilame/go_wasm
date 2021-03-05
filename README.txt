从官网上找 golang 1.15 版本安装 （ tinygo 目前只能支持 1.11-1.15 ）
从 git 上找到 tinygo 0.16 安装 （ 必须使用 tinygo 来编译 wasm 不然，go 编译的 wasm 体积太大了。 ）

工具若是下载慢可以考虑直接在下面的地址下载。
链接：https://pan.baidu.com/s/1Jiz9x2VZxIEi7VP7Zb3xog 
提取码：3bda 
下载完分别解压到不同路径，将 go.exe 和 tinygo.exe 的路径加入环境变量即可使用。

双击 run.bat 或者在命令行执行 run.bat 即可编译并启动 127.0.0.1:80 端口进行调试。