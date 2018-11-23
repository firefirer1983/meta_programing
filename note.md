# sqlalchemy


```python
engine = create_engine('sqlite:///:memory:', echo=True)
```
>  创建一个在内存中的sqlite数据库
> echo 标志用于控制生成的 SQL 语句的 logging

```
engine -> dialect -> DBAPI (sqlite3)
```
> Lazy Connecting: 
>
> * create_engine 的时候，并不会立刻去连接数据库，而是待有实际操作数据库任务的时候才连接。
>
> engine 是用于发出 SQL 命令的，但如果使用了 ORM，所有的 engine 操作都被封装


1. MetaData object (metadata)

    Base contains a MetaData object(metadata)
    All newly defined Table objects collected by metadata

```
Base = declarative_base()
Base.metadata.create_all(engine)
```
```
metadata = MetaData
Base = declarative_base(metadata=metadata)
``` 


    
