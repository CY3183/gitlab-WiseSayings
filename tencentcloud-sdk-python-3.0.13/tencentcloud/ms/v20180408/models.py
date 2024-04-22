# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AdInfo(AbstractModel):
    """广告信息

    """

    def __init__(self):
        """
        :param Spots: 插播广告列表
        :type Spots: list of PluginInfo
        :param BoutiqueRecommands: 精品推荐广告列表
        :type BoutiqueRecommands: list of PluginInfo
        :param FloatWindowses: 悬浮窗广告列表
        :type FloatWindowses: list of PluginInfo
        :param Banners: banner广告列表
        :type Banners: list of PluginInfo
        :param IntegralWalls: 积分墙广告列表
        :type IntegralWalls: list of PluginInfo
        :param NotifyBars: 通知栏广告列表
        :type NotifyBars: list of PluginInfo
        """
        self.Spots = None
        self.BoutiqueRecommands = None
        self.FloatWindowses = None
        self.Banners = None
        self.IntegralWalls = None
        self.NotifyBars = None


    def _deserialize(self, params):
        if params.get("Spots") is not None:
            self.Spots = []
            for item in params.get("Spots"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Spots.append(obj)
        if params.get("BoutiqueRecommands") is not None:
            self.BoutiqueRecommands = []
            for item in params.get("BoutiqueRecommands"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.BoutiqueRecommands.append(obj)
        if params.get("FloatWindowses") is not None:
            self.FloatWindowses = []
            for item in params.get("FloatWindowses"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.FloatWindowses.append(obj)
        if params.get("Banners") is not None:
            self.Banners = []
            for item in params.get("Banners"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Banners.append(obj)
        if params.get("IntegralWalls") is not None:
            self.IntegralWalls = []
            for item in params.get("IntegralWalls"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.IntegralWalls.append(obj)
        if params.get("NotifyBars") is not None:
            self.NotifyBars = []
            for item in params.get("NotifyBars"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.NotifyBars.append(obj)


class AppDetailInfo(AbstractModel):
    """app的详细基础信息

    """

    def __init__(self):
        """
        :param AppName: app的名称
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppSize: app的大小
        :type AppSize: int
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param FileName: app的文件名称
        :type FileName: str
        """
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppSize = None
        self.AppMd5 = None
        self.AppIconUrl = None
        self.FileName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppSize = params.get("AppSize")
        self.AppMd5 = params.get("AppMd5")
        self.AppIconUrl = params.get("AppIconUrl")
        self.FileName = params.get("FileName")


class AppInfo(AbstractModel):
    """提交的app基本信息

    """

    def __init__(self):
        """
        :param AppUrl: app的url，必须保证不用权限校验就可以下载
        :type AppUrl: str
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param FileName: app的文件名，指定后加固后的文件名是{FileName}_legu.apk
        :type FileName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param AppName: app的名称
        :type AppName: str
        """
        self.AppUrl = None
        self.AppMd5 = None
        self.AppSize = None
        self.FileName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppIconUrl = None
        self.AppName = None


    def _deserialize(self, params):
        self.AppUrl = params.get("AppUrl")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.FileName = params.get("FileName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")


class AppScanSet(AbstractModel):
    """扫描后app的信息，包含基本信息和扫描状态信息

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识
        :type ItemId: str
        :param AppName: app的名称
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param ScanCode: 扫描结果返回码
        :type ScanCode: int
        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param TaskTime: 提交扫描时间
        :type TaskTime: int
        :param AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param AppSid: 标识唯一该app，主要用于删除
        :type AppSid: str
        :param SafeType: 安全类型:1-安全软件，2-风险软件，3病毒软件
        :type SafeType: int
        :param VulCount: 漏洞个数
        :type VulCount: int
        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ScanCode = None
        self.TaskStatus = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.AppSid = None
        self.SafeType = None
        self.VulCount = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ScanCode = params.get("ScanCode")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppSid = params.get("AppSid")
        self.SafeType = params.get("SafeType")
        self.VulCount = params.get("VulCount")


class AppSetInfo(AbstractModel):
    """加固后app的信息，包含基本信息和加固信息

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识
        :type ItemId: str
        :param AppName: app的名称
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param ServiceEdition: 加固服务版本
        :type ServiceEdition: str
        :param ShieldCode: 加固结果返回码
        :type ShieldCode: int
        :param AppUrl: 加固后的APP下载地址
        :type AppUrl: str
        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param ClientIp: 请求的客户端ip
        :type ClientIp: str
        :param TaskTime: 提交加固时间
        :type TaskTime: int
        :param AppIconUrl: app的图标url
        :type AppIconUrl: str
        :param ShieldMd5: 加固后app的md5
        :type ShieldMd5: str
        :param ShieldSize: 加固后app的大小
        :type ShieldSize: int
        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ServiceEdition = None
        self.ShieldCode = None
        self.AppUrl = None
        self.TaskStatus = None
        self.ClientIp = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.ShieldMd5 = None
        self.ShieldSize = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ServiceEdition = params.get("ServiceEdition")
        self.ShieldCode = params.get("ShieldCode")
        self.AppUrl = params.get("AppUrl")
        self.TaskStatus = params.get("TaskStatus")
        self.ClientIp = params.get("ClientIp")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.ShieldSize = params.get("ShieldSize")


class CreateScanInstancesRequest(AbstractModel):
    """CreateScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AppInfos: 待扫描的app信息列表，一次最多提交20个
        :type AppInfos: list of AppInfo
        :param ScanInfo: 扫描信息
        :type ScanInfo: :class:`tencentcloud.ms.v20180408.models.ScanInfo`
        """
        self.AppInfos = None
        self.ScanInfo = None


    def _deserialize(self, params):
        if params.get("AppInfos") is not None:
            self.AppInfos = []
            for item in params.get("AppInfos"):
                obj = AppInfo()
                obj._deserialize(item)
                self.AppInfos.append(obj)
        if params.get("ScanInfo") is not None:
            self.ScanInfo = ScanInfo()
            self.ScanInfo._deserialize(params.get("ScanInfo"))


class CreateScanInstancesResponse(AbstractModel):
    """CreateScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识
        :type ItemId: str
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param AppMd5s: 提交成功的app的md5集合
        :type AppMd5s: list of str
        :param LimitCount: 剩余可用次数
        :type LimitCount: int
        :param LimitTime: 到期时间
        :type LimitTime: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ItemId = None
        self.Progress = None
        self.AppMd5s = None
        self.LimitCount = None
        self.LimitTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.Progress = params.get("Progress")
        self.AppMd5s = params.get("AppMd5s")
        self.LimitCount = params.get("LimitCount")
        self.LimitTime = params.get("LimitTime")
        self.RequestId = params.get("RequestId")


class CreateShieldInstanceRequest(AbstractModel):
    """CreateShieldInstance请求参数结构体

    """

    def __init__(self):
        """
        :param AppInfo: 待加固的应用信息
        :type AppInfo: :class:`tencentcloud.ms.v20180408.models.AppInfo`
        :param ServiceInfo: 加固服务信息
        :type ServiceInfo: :class:`tencentcloud.ms.v20180408.models.ServiceInfo`
        """
        self.AppInfo = None
        self.ServiceInfo = None


    def _deserialize(self, params):
        if params.get("AppInfo") is not None:
            self.AppInfo = AppInfo()
            self.AppInfo._deserialize(params.get("AppInfo"))
        if params.get("ServiceInfo") is not None:
            self.ServiceInfo = ServiceInfo()
            self.ServiceInfo._deserialize(params.get("ServiceInfo"))


class CreateShieldInstanceResponse(AbstractModel):
    """CreateShieldInstance返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param ItemId: 任务唯一标识
        :type ItemId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.ItemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.ItemId = params.get("ItemId")
        self.RequestId = params.get("RequestId")


class DeleteScanInstancesRequest(AbstractModel):
    """DeleteScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param AppSids: 删除一个或多个扫描的app，最大支持20个
        :type AppSids: list of str
        """
        self.AppSids = None


    def _deserialize(self, params):
        self.AppSids = params.get("AppSids")


class DeleteScanInstancesResponse(AbstractModel):
    """DeleteScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteShieldInstancesRequest(AbstractModel):
    """DeleteShieldInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ItemIds: 任务唯一标识ItemId的列表
        :type ItemIds: list of str
        """
        self.ItemIds = None


    def _deserialize(self, params):
        self.ItemIds = params.get("ItemIds")


class DeleteShieldInstancesResponse(AbstractModel):
    """DeleteShieldInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type Progress: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeScanInstancesRequest(AbstractModel):
    """DescribeScanInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过app名称，app包名进行筛选
        :type Filters: list of Filters
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 数量限制，默认为20，最大值为100。
        :type Limit: int
        :param ItemIds: 可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。
        :type ItemIds: list of str
        :param OrderField: 按某个字段排序，目前仅支持TaskTime排序。
        :type OrderField: str
        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeScanInstancesResponse(AbstractModel):
    """DescribeScanInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app数量
        :type TotalCount: int
        :param ScanSet: 一个关于app详细信息的结构体，主要包括app的基本信息和扫描状态信息。
        :type ScanSet: list of AppScanSet
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScanSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = AppScanSet()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanResultsRequest(AbstractModel):
    """DescribeScanResults请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识
        :type ItemId: str
        :param AppMd5s: 批量查询一个或者多个app的扫描结果，如果不传表示查询该任务下所提交的所有app
        :type AppMd5s: list of str
        """
        self.ItemId = None
        self.AppMd5s = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppMd5s = params.get("AppMd5s")


class DescribeScanResultsResponse(AbstractModel):
    """DescribeScanResults返回参数结构体

    """

    def __init__(self):
        """
        :param ScanSet: 批量扫描的app结果集
        :type ScanSet: list of ScanSetInfo
        :param TotalCount: 批量扫描结果的个数
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ScanSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = ScanSetInfo()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeShieldInstancesRequest(AbstractModel):
    """DescribeShieldInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过app名称，app包名，加固的服务版本，提交的渠道进行筛选。
        :type Filters: list of Filters
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 数量限制，默认为20，最大值为100。
        :type Limit: int
        :param ItemIds: 可以提供ItemId数组来查询一个或者多个结果。注意不可以同时指定ItemIds和Filters。
        :type ItemIds: list of str
        :param OrderField: 按某个字段排序，目前仅支持TaskTime排序。
        :type OrderField: str
        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc。
        :type OrderDirection: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeShieldInstancesResponse(AbstractModel):
    """DescribeShieldInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app数量
        :type TotalCount: int
        :param AppSet: 一个关于app详细信息的结构体，主要包括app的基本信息和加固信息。
        :type AppSet: list of AppSetInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AppSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AppSet") is not None:
            self.AppSet = []
            for item in params.get("AppSet"):
                obj = AppSetInfo()
                obj._deserialize(item)
                self.AppSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShieldResultRequest(AbstractModel):
    """DescribeShieldResult请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 任务唯一标识
        :type ItemId: str
        """
        self.ItemId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")


class DescribeShieldResultResponse(AbstractModel):
    """DescribeShieldResult返回参数结构体

    """

    def __init__(self):
        """
        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param AppDetailInfo: app加固前的详细信息
        :type AppDetailInfo: :class:`tencentcloud.ms.v20180408.models.AppDetailInfo`
        :param ShieldInfo: app加固后的详细信息
        :type ShieldInfo: :class:`tencentcloud.ms.v20180408.models.ShieldInfo`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.ShieldInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("ShieldInfo") is not None:
            self.ShieldInfo = ShieldInfo()
            self.ShieldInfo._deserialize(params.get("ShieldInfo"))
        self.RequestId = params.get("RequestId")


class Filters(AbstractModel):
    """筛选数据结构

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段
        :type Name: str
        :param Value: 需要过滤字段的值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class PluginInfo(AbstractModel):
    """插件信息

    """

    def __init__(self):
        """
        :param PluginType: 插件类型，分别为 1-通知栏广告，2-积分墙广告，3-banner广告，4- 悬浮窗图标广告，5-精品推荐列表广告, 6-插播广告
        :type PluginType: int
        :param PluginName: 插件名称
        :type PluginName: str
        :param PluginDesc: 插件描述
        :type PluginDesc: str
        """
        self.PluginType = None
        self.PluginName = None
        self.PluginDesc = None


    def _deserialize(self, params):
        self.PluginType = params.get("PluginType")
        self.PluginName = params.get("PluginName")
        self.PluginDesc = params.get("PluginDesc")


class ScanInfo(AbstractModel):
    """需要扫描的应用的服务信息

    """

    def __init__(self):
        """
        :param CallbackUrl: 任务处理完成后的反向通知回调地址,批量提交app每扫描完成一个会通知一次,通知为POST请求，post信息{ItemId:
        :type CallbackUrl: str
        :param ScanTypes: VULSCAN-漏洞扫描信息，VIRUSSCAN-返回病毒扫描信息， ADSCAN-广告扫描信息，PLUGINSCAN-插件扫描信息，可以自由组合
        :type ScanTypes: list of str
        """
        self.CallbackUrl = None
        self.ScanTypes = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ScanTypes = params.get("ScanTypes")


class ScanSetInfo(AbstractModel):
    """app扫描结果集

    """

    def __init__(self):
        """
        :param TaskStatus: 任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时
        :type TaskStatus: int
        :param AppDetailInfo: app信息
        :type AppDetailInfo: :class:`tencentcloud.ms.v20180408.models.AppDetailInfo`
        :param VirusInfo: 病毒信息
        :type VirusInfo: :class:`tencentcloud.ms.v20180408.models.VirusInfo`
        :param VulInfo: 漏洞信息
        :type VulInfo: :class:`tencentcloud.ms.v20180408.models.VulInfo`
        :param AdInfo: 广告插件信息
        :type AdInfo: :class:`tencentcloud.ms.v20180408.models.AdInfo`
        :param TaskTime: 提交扫描的时间
        :type TaskTime: int
        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.VirusInfo = None
        self.VulInfo = None
        self.AdInfo = None
        self.TaskTime = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("VirusInfo") is not None:
            self.VirusInfo = VirusInfo()
            self.VirusInfo._deserialize(params.get("VirusInfo"))
        if params.get("VulInfo") is not None:
            self.VulInfo = VulInfo()
            self.VulInfo._deserialize(params.get("VulInfo"))
        if params.get("AdInfo") is not None:
            self.AdInfo = AdInfo()
            self.AdInfo._deserialize(params.get("AdInfo"))
        self.TaskTime = params.get("TaskTime")


class ServiceInfo(AbstractModel):
    """提交app加固的服务信息

    """

    def __init__(self):
        """
        :param ServiceEdition: 服务版本，基础版basic,专业版Professional
        :type ServiceEdition: str
        :param CallbackUrl: 任务处理完成后的反向通知回调地址,通知为POST请求，post信息{ItemId:"xxxduuyt-ugusg"}
        :type CallbackUrl: str
        :param SubmitSource: 提交来源 YYB-应用宝 RDM-rdm MC-控制台 MAC_TOOL-mac工具 WIN_TOOL-window工具
        :type SubmitSource: str
        """
        self.ServiceEdition = None
        self.CallbackUrl = None
        self.SubmitSource = None


    def _deserialize(self, params):
        self.ServiceEdition = params.get("ServiceEdition")
        self.CallbackUrl = params.get("CallbackUrl")
        self.SubmitSource = params.get("SubmitSource")


class ShieldInfo(AbstractModel):
    """加固后app的信息

    """

    def __init__(self):
        """
        :param ShieldCode: 加固结果的返回码
        :type ShieldCode: int
        :param ShieldSize: 加固后app的大小
        :type ShieldSize: int
        :param ShieldMd5: 加固后app的md5
        :type ShieldMd5: str
        :param AppUrl: 加固后的APP下载地址
        :type AppUrl: str
        :param TaskTime: 加固的提交时间
        :type TaskTime: int
        :param ItemId: 任务唯一标识
        :type ItemId: str
        """
        self.ShieldCode = None
        self.ShieldSize = None
        self.ShieldMd5 = None
        self.AppUrl = None
        self.TaskTime = None
        self.ItemId = None


    def _deserialize(self, params):
        self.ShieldCode = params.get("ShieldCode")
        self.ShieldSize = params.get("ShieldSize")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.AppUrl = params.get("AppUrl")
        self.TaskTime = params.get("TaskTime")
        self.ItemId = params.get("ItemId")


class VirusInfo(AbstractModel):
    """病毒信息

    """

    def __init__(self):
        """
        :param SafeType: 软件安全类型，分别为0-未知、 1-安全软件、2-风险软件、3-病毒软件
        :type SafeType: int
        :param VirusName: 病毒名称， utf8编码，非病毒时值为空
        :type VirusName: str
        :param VirusDesc: 病毒描述，utf8编码，非病毒时值为空
        :type VirusDesc: str
        """
        self.SafeType = None
        self.VirusName = None
        self.VirusDesc = None


    def _deserialize(self, params):
        self.SafeType = params.get("SafeType")
        self.VirusName = params.get("VirusName")
        self.VirusDesc = params.get("VirusDesc")


class VulInfo(AbstractModel):
    """漏洞信息

    """

    def __init__(self):
        """
        :param VulList: 漏洞列表
        :type VulList: list of VulList
        :param VulFileScore: 漏洞文件评分
        :type VulFileScore: int
        """
        self.VulList = None
        self.VulFileScore = None


    def _deserialize(self, params):
        if params.get("VulList") is not None:
            self.VulList = []
            for item in params.get("VulList"):
                obj = VulList()
                obj._deserialize(item)
                self.VulList.append(obj)
        self.VulFileScore = params.get("VulFileScore")


class VulList(AbstractModel):
    """漏洞信息

    """

    def __init__(self):
        """
        :param VulId: 漏洞id
        :type VulId: str
        :param VulName: 漏洞名称
        :type VulName: str
        :param VulCode: 漏洞代码
        :type VulCode: str
        :param VulDesc: 漏洞描述
        :type VulDesc: str
        :param VulSolution: 漏洞解决方案
        :type VulSolution: str
        :param VulSrcType: 漏洞来源类别，0默认自身，1第三方插件
        :type VulSrcType: int
        :param VulFilepath: 漏洞位置
        :type VulFilepath: str
        :param RiskLevel: 风险级别：1 低风险 ；2中等风险；3 高风险
        :type RiskLevel: int
        """
        self.VulId = None
        self.VulName = None
        self.VulCode = None
        self.VulDesc = None
        self.VulSolution = None
        self.VulSrcType = None
        self.VulFilepath = None
        self.RiskLevel = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulCode = params.get("VulCode")
        self.VulDesc = params.get("VulDesc")
        self.VulSolution = params.get("VulSolution")
        self.VulSrcType = params.get("VulSrcType")
        self.VulFilepath = params.get("VulFilepath")
        self.RiskLevel = params.get("RiskLevel")