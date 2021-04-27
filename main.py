from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree as ET


def create_code(model_name: str, template_name: str) -> None:
    """test"""
    tree = ET.ElementTree(file=model_name)
    # 获取根节点
    root = tree.getroot()
    # 循环写好多个不同的类
    classnames = []
    for child_of_root in root:
        # 这里进行每个类信息的构造
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
        # 获取该类的各种属性
        for elem in child_of_root.iterfind('structuralFeatures'):
            attr = {}
            attr['name'] = elem.attrib['name']
            attr['pb'] = 'private'
            attr['type'] = 'String'
            attrs.append(attr)
        # 获取该类的各种操作
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

        for elem in child_of_root.iterfind('dependencies'):
            if (elem.attrib['kind'] == 'call'):
                is_call = '//call function is till not finished'
        # 渲染模板
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template_name)
        text = template.render(is_abstract=s_abstract, classname=classname, extendname=extendname, attrs=attrs,
                               funcs=funcs, is_call=is_call)
        # 保存文件
        with open('./code/'+classname + '.java', 'w+') as f:
            f.write(text)


if __name__ == '__main__':
    model_name = 'testt.aquila'
    template_name = 'test.txt'
    create_code(model_name, template_name)
