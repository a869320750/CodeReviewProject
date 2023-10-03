# 教学关卡， https://zhuanlan.zhihu.com/p/340119918

import pandas as pd
import os

print(pd.Series([2,4,6,8,10]))
print(pd.Series([2,4,6,8,10], index=['a', 'b', 'c', 'd', 'e']))

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.DataFrame({'辣条':[14,20], '面包':[7,3], '可乐':[8,13], '烤肠':[10,6]})

# 查列
print(df)
print(df['可乐'])

# 修改列
df['可乐'] = [18,23]
print(df)

# 增加列
df['糖果'] = [114,514]
print(df)

# 删除列
# drop() 方法的第一个参数是要删除的列名或索引。axis 表示针对行或列进行删除，axis = 0 表示删除对应的行，axis = 1 表示删除对应的列，axis 默认为 0。
# 最后的 inplace = True 表示直接修改原数据，否则 drop() 方法只是返回删除后的表格，对原表格没有影响。因此上面两种写法的结果是一样的。
df.drop('面包', axis=1, inplace=True)
print(df)

# 路径问题
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)

df = pd.read_csv(os.path.join(current_directory ,'tutorial.csv'))
print(df.head())

# 显示前两条数据
print(df.head(2))

# 查看大致信息
print(df.info())

# 快速查看数据的统计摘要
# 生成的摘要从上往下分别表示数量、平均数、标准差、最小值、25% 50% 75% 位置的值和最大值。
print(df.describe())

# 在末尾添加一行
new_row = pd.Series({
    '销售员':'野兽先辈',
    '团队':'D',
    '第一季度':11451,
    '第二季度':14514,
    '第三季度':19198,
    '第四季度':19810
    })
df.loc[len(df)] = new_row

# 谁是销售冠军

df['总和'] = df['第一季度'] + df['第二季度'] + df['第三季度'] + df['第四季度']
df.head()
df.sort_values('总和', ascending=False, inplace=True)
print(df)


print(df)
# 写文件
target_path = os.path.join(current_directory ,'tutorial_result.csv')
if(os.path.exists(target_path)):
    os.remove(target_path)
df.to_csv(target_path, index=False)