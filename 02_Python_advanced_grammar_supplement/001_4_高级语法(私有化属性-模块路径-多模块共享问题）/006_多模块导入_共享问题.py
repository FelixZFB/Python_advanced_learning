# 多模块导入：使用 import module_name
# 不要使用 from module_name import function_name

# 有1号和2号两个脚本都使用from module_name import function_name
# 实际上是定义了一个新的变量名：function_name指向的导入模块中function_name的值True
# 如果原模块的function_name = True，即是1号脚本中把function_name = False
# 这样只是1号脚本的function_name指向了false，但是原模块中还是指向的True
# 因此，导致2号脚本中的function_name并没有修改，还是指向原始模块的True

# 因此，推荐使用多模块共享时候使用：import module_name，避免入坑找不到原因

# 但是如果function_name = list列表
# 使用function_name  = 新list列表，原模块的function_name任然不变
# 但是使用function_name.append(元素),这样原模块的function_name就会改变
# 添加是指向地址不变，修改里面的值，直接赋值是指向了新值的地址