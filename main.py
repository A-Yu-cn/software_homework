from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET


def create_code(model_name: str, template_name: str) -> None:
    """
    此函数通过传入模型名称以及源代码模板路径，实现aquila模型转为JAVA源代码的功能
    源代码将生成到项目路径下code文件夹下
    """
    tree = ET.ElementTree(file=model_name)
    # 获取根节点
    root = tree.getroot()
    # 循环写好多个不同的类
    classnames = []
    for child_of_root in root:
        # 这里进行每个类所有信息的构造
        classnames.append(child_of_root.attrib['name'])
        s_abstract = ''
        classname = child_of_root.attrib['name']
        extendname = 'Object'
        attrs = []
        is_call = ''
        funcs = []
        # 判断是否为抽象类
        if (child_of_root.attrib.get('abstract') == 'true'):
            s_abstract = 'abstract'
        # 判断是否继承自其他类
        if (child_of_root.attrib.get('superTypes') != None):
            extendname = classnames[int(child_of_root.attrib.get('superTypes')[-1])]
        # 获取该类的各种属性，属性类型在完善后可从默认String改为从xml文档中读出
        for elem in child_of_root.iterfind('structuralFeatures'):
            attr = {}
            attr['name'] = elem.attrib['name']
            attr['pb'] = 'private'
            attr['type'] = 'String'
            attrs.append(attr)
        # 获取该类的各种操作，属性类型同上可改
        for elem in child_of_root.iterfind('operations'):
            func = {}
            func['name'] = elem.attrib['name']
            func['pb'] = 'public'
            func['type'] = 'void'
            funcs.append(func)
        # 判断该类是否需要call
        for elem in child_of_root.iterfind('dependencies'):
            if (elem.attrib['kind'] == 'call'):
                is_call = '//call function is till not finished'
        # 渲染模板
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_name)
        text = template.render(is_abstract=s_abstract, classname=classname, extendname=extendname, attrs=attrs,
                               funcs=funcs, is_call=is_call)
        # 保存到JAVA源代码文件中
        with open('./code/'+classname + '.java', 'w+') as f:
            f.write(text)


if __name__ == '__main__':
    #将两个路径都从方法中抽取出来，便于对不同模型和模板进行函数调用实现功能
    model_name = 'testt.aquila'
    template_name = 'test.txt'
    create_code(model_name, template_name)
