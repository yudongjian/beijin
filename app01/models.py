from django.db import models


# 创建用户表
class userinfo(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    # 保存用户自己需要的字段信息
    sales_column = models.CharField(max_length=256, default='')
    buy_column = models.CharField(max_length=256, default='')
    goods_column = models.CharField(max_length=256, default='')
    customer_column = models.CharField(max_length=256, default='')


# 创建销售信息表
class sales_info(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    company_name = models.CharField(max_length=64)  # 公司名称
    link_man = models.CharField(max_length=64)      # 联系人
    link_tel = models.CharField(max_length=64)      # 电话
    email = models.CharField(max_length=64)           # 邮箱
    company_addr = models.CharField(max_length=64)      # 公司地址
    duty_num = models.CharField(max_length=64)             # 税号
    bank_addr = models.CharField(max_length=64)            # 开户行地址
    bank_num = models.IntegerField()                       # 银行卡号
    contract_no = models.IntegerField()                    # 合同号
    product_name = models.CharField(max_length=64)          # 产品名称
    product_num = models.IntegerField()                     # 产品数量
    contract_menoy = models.IntegerField()                  # 合同金额
    pay_menoy = models.IntegerField()                       # 已付金额
    no_pay_meony = models.IntegerField()                     # 未付金额
    delivery_date = models.DateTimeField(max_length=64)    # 交货时间
    isno_bill = models.CharField(max_length=64)            # 是否开具发票
    bill_date = models.DateTimeField(max_length=64)        # 开票日期
    pay_type = models.CharField(max_length=64)             # 付款方式
    send_goods_addr = models.CharField(max_length=64)      # 发货地址
    bill_addr = models.CharField(max_length=64)            # 发票地址
    note = models.CharField(max_length=64)                 # 备注
    status = models.CharField(max_length=16, default='否')       # 状态
    img_path = models.CharField(max_length=64, default='')       # 合同照片的路径


# 创建采购信息表
class buy_info(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()                        # 采购日期
    company_name = models.CharField(max_length=64)  # 公司名称
    link_man = models.CharField(max_length=64)      # 联系人
    link_tel = models.CharField(max_length=64)      # 电话

    product_name = models.CharField(max_length=64)          # 产品名称
    product_num = models.IntegerField()                     # 产品数量

    contract_no = models.IntegerField()                    # 合同号
    contract_menoy = models.IntegerField()                   # 合同金额
    pay_menoy = models.IntegerField()                         # 已付金额
    no_pay_meony = models.IntegerField()                      # 未付金额
    delivery_date = models.DateTimeField(max_length=64)    # 交货时间

    isno_bill = models.CharField(max_length=64)            # 是否开具发票
    bill_date = models.DateTimeField(max_length=64)        # 开票日期

    send_goods_addr = models.CharField(max_length=64)      # 发货地址
    bill_addr = models.CharField(max_length=64)            # 发票地址


# 商品表
class goods_info(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=128)                           # 产品名称
    product_num = models.CharField(max_length=128, default='')                 # 商品编号
    product_specification = models.CharField(max_length=128, default='')        # 产品规格
    product_unit = models.CharField(max_length=128, default='')                   # 产品单位
    product_color = models.CharField(max_length=128, default='')               # 产品颜色
    product_model = models.CharField(max_length=128, default='')                     # 产品型号
    product_type = models.CharField(max_length=64, default='')                    # 产品分类
    product_weight = models.CharField(max_length=64, default='')               # 产品重量
    product_brand = models.CharField(max_length=64, default='')               # 产品品牌
    product_attribute1 = models.CharField(max_length=64, default='')          # 自定义属性1
    product_attribute2 = models.CharField(max_length=64, default='')          # 自定义属性2
    product_attribute3 = models.CharField(max_length=64, default='')          # 自定义属性3
    product_note = models.CharField(max_length=64, default='')                   # 备注


# 客户表
class cunstomer_info(models.Model):
    id = models.AutoField(primary_key=True)
    cunstomer_name = models.CharField(max_length=128)                           # 客户名称
    cunstomer_addr = models.CharField(max_length=128, default='')               # 客户地址
    link_name = models.CharField(max_length=128, default='')                    # 联系人名称
    link_tel = models.CharField(max_length=128, default='')                     # 联系人电话
    link_email = models.CharField(max_length=128, default='')                   # 联系人邮箱
    bank_num = models.CharField(max_length=128, default='')                     # 银行卡号


# 库存信息表
class stock_info(models.Model):
    id = models.AutoField(primary_key=True)
    send_addr = models.CharField(max_length=128)



# 创建其他支出表
class pay_info(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    item = models.CharField(max_length=32)
    menoy = models.IntegerField()
    note = models.CharField(max_length=32)