def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)

def demo1(num, *args, **kwargs):
    print(num, *args, **kwargs)
    print(num)
    print(*args)
    print(**kwargs)


demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
demo(1, 2, 3, 4, 5, name="小明", age=18)
