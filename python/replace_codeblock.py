import os

'''
hexo里可以使用 {% codeblock %}来表示代码块，但是这在一般的markdown中是不支持的
这个函数将 {% codeblock %} ... {% codeblock %} 替换为 ```cpp  ... ```
'''
def replace_codeblock(filename):
    f1 = open(filename, 'r',encoding='utf-8')
    f2 = open(filename+"_",'w',encoding='utf-8')

    for line in f1:
        if(line.__contains__("codeblock")):
            if(line.__contains__("endcodeblock")):
                f2.write("```\n")
            else:
                f2.write("```cpp\n")
        else:
            f2.write(line)

    f1.close()
    f2.close()
    os.remove(filename)
    os.rename(filename+"_",filename)


'''
对目录下所有的markdown文件进行修改
'''
def dfs(name):
    if(os.path.isdir(name)):
        paths = os.listdir(name)
        for path in paths:
            dfs(name + "/" + path)
    else:
        if(name[-2:] == 'md'):
            replace_codeblock(name)


dfs(".")
