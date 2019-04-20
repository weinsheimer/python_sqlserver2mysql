# python_sqlserver2mysql
**sqlconvert** 从sql server -> mysql

sql server 的初级转换结果
<pre><code>
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (25104, 0, '陕西省侨联');
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (26304, 0, '上海发展研究基金会会员 bashusong@drc.gov.cn');
GO
print 'Processed 100 total records'
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (26305, 0, 'BaekChunhwa@baekc.com
h.saori2010@gmail.com
浦东新区欧美同学会会员
欧美同学会浦东分会');
GO
print 'Processed 100 total records'
</code></pre>

用python转换成

```
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (25104, 0, '陕西省侨联');		
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (26304, 0, '上海发展研究基金会会员\nbashusong@drc.gov.cn');
INSERT INTO `paros_customer_org` (`CustomerID`, `UserID`, `Remark`) VALUES (26305, 0, 'BaekChunhwa@baekc.com\nh.saori2010@gmail.com\n浦东新区欧美同学会会员\n欧美同学会浦东分会');
```
