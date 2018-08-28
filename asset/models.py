# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
store_type =(
    (0, u"加盟"),
    (1, u"直营"),
)
dev_status=(
    (0, u"未激活"),
    (1, u"离线"),
    (2, u"在线"),
)
customer_level=(
    (0, u"普通"),
    (1, u"等级1"),
    (2, u"等级2"),
    (3, u"等级3"),
    (4, u"等级4"),
    (5, u"等级5"),
)
BOOL_CHOICES = ((True, '使用中'), (False, '空闲'))
class CUSTOMER(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'客户名称')
    phone = models.CharField(max_length=32, verbose_name=u'联系电话')
    level = models.IntegerField(verbose_name="客户等级",choices=customer_level,default=0,blank=True)
    creat_date = models.DateTimeField('客户创建时间')
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"客户"
        verbose_name_plural = verbose_name
        #app_label = 'assets'
class STORE(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1(), editable=False, primary_key=True)
    customerid = models.ForeignKey(CUSTOMER, blank=True, verbose_name=u'所属客户', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=u'门店名称')
    bandwidth = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'门店带宽')
    phone = models.CharField(max_length=32, verbose_name=u'联系电话')
    linkman = models.CharField(max_length=32, null=True, verbose_name=u'联系人')
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"门店地址")
    #network = models.TextField(blank=True, null=True, verbose_name=u"IP地址段")
    create_time = models.DateField(auto_now=True)
    #operator = models.IntegerField(verbose_name=u"运营商", choices=idc_operator, max_length=32, blank=True, null=True)
    type = models.IntegerField(verbose_name=u"门店类型", choices=store_type,  blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"客户门店"
        verbose_name_plural = verbose_name
        #app_label = 'assets'

class DEV(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1(), editable=False, primary_key=True)
    storeid =  models.ForeignKey(STORE, blank=True, verbose_name=u'所属门店', on_delete=models.CASCADE,null=True)
    node_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"终端名称")
    eth1 = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'网卡1')
    eth2 = models.GenericIPAddressField(blank=True, null=True, verbose_name=u'网卡2')
    mac = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"MAC")
    #internal_ip = models.IPAddressField(blank=True, null=True, verbose_name=u'远控卡')
    #brand = models.CharField(max_length=64, choices=Server_System, blank=True, null=True, verbose_name=u'硬件厂商')
    #cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    #hard_disk = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'硬盘')
    #memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    #system = models.CharField(verbose_name=u"系统类型", max_length=32, choices=System_os, default="CentOS", blank=True,
    #                          null=True, )
    #system_cpuarch = models.CharField(max_length=32, blank=True, null=True, choices=system_arch, verbose_name=u"系统版本")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"版本号")
    create_time = models.DateTimeField(auto_now_add=True)
    guarantee_date = models.DateField(blank=True, null=True, verbose_name=u'保修时间')
    #cabinet = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'机柜号')
    dev_cabinet_id = models.CharField(max_length =200,blank=True, null=True, verbose_name=u'设备位置')
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    editor = models.TextField(blank=True, null=True, verbose_name=u'备注')
    #business = models.ManyToManyField(Project, blank=True, null=True, verbose_name=u'所属业务')
    status = models.IntegerField(verbose_name=u"机器状态", choices=dev_status, default=0, blank=True)
    #vm = models.ForeignKey("self", blank=True, null=True, verbose_name=u"虚拟机父主机")
    type = models.IntegerField(verbose_name=u'主机类型', default=1, blank=True)
    #Services_Code = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"快速服务编码")
    #env = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"环境", choices=ENVIRONMENT)
    #room_number = models.CharField(verbose_name=u"房间号", max_length=32, choices=room_hours, blank=True, null=True)
    server_sn = models.CharField(verbose_name=u"SN编号", max_length=32, blank=True, null=True)
    switch_port = models.CharField(verbose_name=u"端口号", max_length=12, blank=True, null=True)
    #service = models.ManyToManyField(Service, verbose_name=u'运行服务', blank=True, null=True)
    idle = models.BooleanField(verbose_name=u'状态', default=1, choices=BOOL_CHOICES)

    def __unicode__(self):
        return self.node_name

    class Meta:
        verbose_name = u"设备"
        verbose_name_plural = verbose_name