from pathlib import Path

def rst2md(line):
    global codetag, tag1, tag2
    if ".. code-block:: python" in line:
        codetag = True
        return "```python" 
    elif not line.startswith("    ") and codetag:
        
        if line != "\n":
            codetag = False
            if  "===============" in line:
                tag1 = True
                return "```\n## "
            elif "--------" in line:
                tag2 = True
                return "```\n### "            
            return "```\n" + line
        else:
            return line
    elif "===============" in line:
        if tag1:
            tag1 = False
            return " ##\n"
        else:
            tag1 = True
            return "## "
    elif tag1 and not ("===============" in line):
        return line.strip()
    elif "--------" in line:
        if tag2:
            tag2 = False
            return " ###\n"
        else:
            tag2 = True
            return "### "
    elif tag2 and not ("--------" in line):
        return line.strip()
    elif line == "\n":
        return ""
    elif line == "代码示例：\n":
        return "**代码示例：**\n"
    else:
        return line



def save_md(output, input):
    with open(output, "a",encoding='utf-8') as f1:
        with open(input, 'r', encoding='utf-8') as file:
            for line in file:
                f1.write(rst2md(line))



def list_files_recursive(directory_path):
    directory = Path(directory_path)

    # 获取指定目录及其子目录下的所有文件
    files = [file for file in directory.rglob('*') if file.is_file()]

    # 打印文件名及其完整路径
    for file in files:
        yield file

# 用法示例
directory_path = 'source'

for file_path in list_files_recursive(directory_path):
    codetag = False
    tag1 = False
    tag2 = False
    if file_path.parent.name == "source":
        continue

    save_path = Path("mdsource") / file_path.parent.name 
    save_path.mkdir(parents=True, exist_ok=True)
    save_md(save_path / file_path.with_suffix(".md").name, file_path)
