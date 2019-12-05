# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中
# 索引和内容构成一个tuple类型，然后所有tuple数据生成一个元组列表
# 索引位于元组第一个元素位置，内容位于第二个元素位置

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# 默认从0开始添加索引（下标）
print(enumerate(seasons))
print(list(enumerate(seasons)))
for i in enumerate(seasons):
    print(i)

# 添加起始下标位置
new_seasons = list(enumerate(seasons, start=100))
print(new_seasons)
# 取出索引及其值
for index, season in new_seasons:
    print(index, season)




