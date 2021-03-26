# -*-coding:utf-8 -*-
# @name ：Python万年历
# @author ：loading_miracle

class Calendar(object):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year=2017):  # 初始化默认2017年
        self.year = year
        if self.year_days(year) == 366:
            self.days[1] = 29

        '''公元1年1月1日是星期1'''
        self.week = 1       # 星期几
        self.totalDays = 1  # 公元第几天
        for i in range(1, self.year):
            self.totalDays += self.year_days(i)

    # 判断每年的天数
    @staticmethod
    def year_days(year):
        return 366 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 365

    # 查看某个月的日历
    def months(self, month):
        _totalDays_ = self.totalDays
        for i in range(1, month):
            _totalDays_ += self.days[i-1]

        # 计算确定月份的第一天为周几
        self.week = _totalDays_ % 7
        self.show(month)

    # 查看全年日历
    def whole_year(self):
        # 计算确定年份的一月一日为周几
        self.week = self.totalDays % 7
        for i in range(1, 13):
            self.show(i)

    # 显示输出函数
    def show(self, month):
        print('\t\t{}年{}月份日历'.format(self.year, month))
        print(' Sun  Mon Tues  Web Thur  Fri  Sat')
        print('-----------------------------------------')
        begin = 1   # 每个月从 1号 开始

        for j in range(0, self.week):
            print('%5s' % '', end='')

        while begin <= self.days[month - 1]:
            print('{:^5d}'.format(begin), end='')
            begin += 1

            self.week = (self.week + 1) % 7
            if self.week % 7 == 0:
                print()
        print('\n')


if __name__ == "__main__":
    data = Calendar(2021)
    data.whole_year()
    data.months(3)
