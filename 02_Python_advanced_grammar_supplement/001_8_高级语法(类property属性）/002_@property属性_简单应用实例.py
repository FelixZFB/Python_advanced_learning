# 对于京东商城中显示电脑主机的列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，
# 而是通过分页的功能局部显示，所以在向数据库中请求数据时就要显示的
# 指定获取从第m条到第n条的所有数据 这个分页的功能包括：

# 根据用户请求的当前页和总数据条数计算出m和n
# 根据m和n去数据库中请求数据

class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    # 将起始页码封装到property属性中
    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    # 将结束页码封装到property属性中
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(2)

# 调用属性比调用方法代码简单多了，不需要传参数也不需要括号了
# 如果用调用方法的方式，需要考虑传参数的问题
print(p.start)  # 就是起始值，即：m
print(p.end)  # 就是结束值，即：n
