# pandas2mongo
将dataframe 转换成mongodb 中的doucuments，并进行批量更新或插入。
（陆续更新中）
1. to_base_type()：将numpy 或pandas 的类型转换为对应的基本类型
``` Python
to_base_type(x: Union[None, np.integer, np.floating, pd.Timestamp]) -> Union[None, int, float, datetime]
```
2. insert()：将dataframe 插入至对应的collection 中
3. update()：依据dataframe 的记录批量更新collection 中相应的document
