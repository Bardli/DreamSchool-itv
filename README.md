# DreamSchool-itv

question1.py 包含一下问题解

外汇牌价查询

 

这是中国银行外汇牌价网站：https://www.boc.cn/sourcedb/whpj/

 

请使用python3 和 selenium库写一个程序，实现以下功能：

 

输入：日期、货币代号

输出：该日期该货币的“现汇卖出价”

 

示例：

python3 yourcode.py 20211231 USD

输出：

636.99

 

该日期有很多个价位，只需要输出任意一个时间点的价位即可。

货币代号为USD、EUR这样的三位英文代码，请参考这里的标准符号：https://www.11meigui.com/tools/currency

 

要求：

1， 将selenium爬到的数据打印到一个result.txt 文件里

2， 代码规范，注释清晰，变量命名合理易读，无不必要的冗余

3，有适当的异常处理

 

question2.py 包含以下问题解

给你一个字符串，如果一个字符在它前面k个字符中已经出现过了，就把这个字符改成’-’。

比如

Input: abcdefaxc 10

Output abcdef-x-

Input: abcdefaxcqwertba 10

Output abcdef-x-qw-rtb-
