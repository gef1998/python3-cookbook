## 10.13 安装私有的包 ##
### 问题 ###
你想要安装一个第三方包，但是没有权限将它安装到系统Python库中去。
或者，你可能想要安装一个供自己使用的包，而不是系统上面所有用户。
### 解决方案 ###
Python有一个用户安装目录，通常类似"~/.local/lib/python3.3/site-packages"。
要强制在这个目录中安装包，可使用安装选项“--user”。例如：
```python
    python3 setup.py install --user

```
或者
```python
    pip install --user packagename

```
在sys.path中用户的“site-packages”目录位于系统的“site-packages”目录之前。
因此，你安装在里面的包就比系统已安装的包优先级高
（尽管并不总是这样，要取决于第三方包管理器，比如distribute或pip）。
### 讨论 ###
通常包会被安装到系统的site-packages目录中去，路径类似“/usr/local/lib/python3.3/site-packages”。
不过，这样做需要有管理员权限并且使用sudo命令。
就算你有这样的权限去执行命令，使用sudo去安装一个新的，可能没有被验证过的包有时候也不安全。
安装包到用户目录中通常是一个有效的方案，它允许你创建一个自定义安装。
另外，你还可以创建一个虚拟环境，这个我们在下一节会讲到。
