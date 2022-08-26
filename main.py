import sys

from typing import List

from alibabacloud_dingtalk.swform_1_0.client import Client as dingtalkswform_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.swform_1_0 import models as dingtalkswform__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkswform_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkswform_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_form_instances_headers = dingtalkswform__1__0_models.ListFormInstancesHeaders()
        list_form_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_form_instances_request = dingtalkswform__1__0_models.ListFormInstancesRequest(
            biz_type=0,
            action_date='2019-01-01',
            next_token=0,
            max_results=10
        )
        try:
            client.list_form_instances_with_options('PROC-8DBC8FEB-18B8xxxxx', list_form_instances_request, list_form_instances_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_form_instances_headers = dingtalkswform__1__0_models.ListFormInstancesHeaders()
        list_form_instances_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_form_instances_request = dingtalkswform__1__0_models.ListFormInstancesRequest(
            biz_type=0,
            action_date='2019-01-01',
            next_token=0,
            max_results=10
        )
        try:
            await client.list_form_instances_with_options_async('PROC-8DBC8FEB-18B8xxxxx', list_form_instances_request, list_form_instances_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass


if __name__ == '__main__':
    Sample.main(sys.argv[1:])