## 10.2 控制模块被全部导入的内容 ##
### 问题 ###
当使用'from module import *' 语句时，希望对从模块或包导出的符号进行精确控制。
### 解决方案 ###
在你的模块中定义一个变量 __all__ 来明确地列出需要导出的内容。
举个例子:
```python
    # somemodule.py
    def spam():
        pass

    def grok():
        pass

    blah = 42
    # Only export 'spam' and 'grok'
    __all__ = ['spam', 'grok']

```
### 讨论 ###
尽管强烈反对使用 'from module import *', 但是在定义了大量变量名的模块中频繁使用。
如果你不做任何事, 这样的导入将会导入所有不以下划线开头的。
另一方面,如果定义了 __all__ , 那么只有被列举出的东西会被导出。
如果你将 __all__ 定义成一个空列表, 没有东西将被导入。
如果 __all__ 包含未定义的名字, 在导入时引起AttributeError。
