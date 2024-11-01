# You and your teammates need to write a service to:

# read the grade information in the table.

# Calculate the total score and maximum score difference of each individual.

# generate a statistical table for these two data items.

import pandas as pd

def read_grade_data(file_path):
    """读取成绩数据文件"""
    return pd.read_csv(file_path)

def calculate_statistics(df):
    """计算每个学生的统计数据"""
    grade_columns = ['Chinese', 'Math', 'English', 'CloudComputing']
    
    # 计算总分和最大分差
    df['Total'] = df[grade_columns].sum(axis=1)
    df['Score_Gap'] = df[grade_columns].max(axis=1) - df[grade_columns].min(axis=1)
    
    return df

def main():
    # 读取数据并计算
    df = read_grade_data('Grade Table.csv')
    df = calculate_statistics(df)
    
    # 保存需要的列，不排序
    output_columns = ['Name', 'Total', 'Score_Gap']
    df[output_columns].to_csv('result.csv', index=False)
    print("\n统计完成，结果已保存到'result.csv'")

if __name__ == '__main__':
    main()