#定义索引类 ,此文件名为固定的
#建立索引目录也是固定的, templates/search/indexes/goods(索引模型所在的appa)/goodssku_text.txt(好像可以随便起，但还是遵循比较好)
from haystack import indexes
#导入模型类
from goods.models import GoodsSKU

# 指定于某个类的某些数据建立索引，一般命名：模型类名+Index
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
    #document=True 表示text是一个索引字段.use_template=True指定根据表中的哪些字段建立索引文件，把说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    # author = indexes.CharField(model_attr='user')
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        # 返回你的模型类
        return GoodsSKU

    # 建立索引的数据
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()  # filter(pub_date__lte=datetime.datetime.now())