# coding=utf-8
# 将未验证的用户，验证后，移动到已验证列表

# 首先，创建一个待验证的用户列表
# 再创建一个用于存储已验证用户的空列表


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每一个用户，直到没有未验证的用户为止，将每一个验证过的列表都移动到已验证列表中
# 从未验证列表最后一个开始，未验证列表删除一个，已验证列表添加一个
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confimed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print(confirmed_users)
