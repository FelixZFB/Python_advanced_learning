# 多模块导入：使用 import module_name
# 不要使用 from module_name import function_name

# 多个py文件在import的时候,会先去sys.module里面检查是否已经import了,
# 如果已经import了,就不再重复import,否则就import进来

# from aaa.yyy import x则不一样，test.py中这样from import，
# 此时x就是test自己命名空间中的变量。所以x只在test.py中有效，无论如何对x修改，都无法影响yyy中的x


# 有py1和py2两个脚本都使用from module_name import function_name
# 上述导入：实际上是定义了一个新的变量名：function_name指向的导入模块中function_name的值True

# 如果原模块的function_name = True，即是py1脚本中把function_name = False
# 这样只是py1脚本的function_name指向了false，但是原始模块中还是指向的True
# 因此，导致py2脚本中的function_name并没有修改(实际我们也是希望一起指向False)，还是指向原始模块的True

# 因此，推荐使用多模块共享时候使用：import module_name，避免入坑找不到原因

# 但是如果function_name = list列表
# 使用function_name  = 新list列表，原模块的function_name任然不变
# 但是使用function_name.append(元素),这样原模块的function_name就会改变
# 添加是指向地址不变，修改里面的值，直接赋值是指向了新值的地址