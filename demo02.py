"""
  变量：在内存中存储的数据

"""
#语法
#变量名 = 对象
name = '张无忌'
age = 20
#内存图
#变量名　对象内存地址的别名
#见名知意

#第一次使用变量　先创建对象然后用变量名绑定
#再次对同名的变量赋值时　不会创建新的变量
#而是修改变量的绑定
name = '周芷若'

name1 = name2 = '赵敏'
print(name1)
print(name2)

teacher1,teacher2 = '老王','小郭'
#画内存图　　休息10:45～11:00
print(teacher1)
print(teacher2)









