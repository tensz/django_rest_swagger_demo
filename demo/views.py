# encoding=utf-8
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from django_rest_swagger_demo.mixins import RequestLogViewMixin
from .models import ResourceModel


# Create your views here.

class Resource(RequestLogViewMixin, APIView):
    def get(self, request):
        """
            获取资源
            ---
            parameters:
                - name: resource_id
                  description: 资源id
                  required: false
                  type: string
                  paramType: query
        """
        params = request.query_params.dict()
        resource_list = ResourceModel.objects.filter(**params).values()
        return Response({"result": "success",
                         "data": {"resource_list": resource_list}})

    def post(self, request):
        """
            新建资源
            ---
            parameters:
                - name: resource_id
                  description: 资源id
                  required: true
                  type: string
                  paramType: form
                - name: resource_remark
                  description: 资源备注
                  required: true
                  type: string
                  paramType: form
        """
        form = request.POST.dict()
        try:
            ResourceModel(**form).save()
        except Exception, e:
            raise APIException(detail='重复资源id')
        return Response({"result": "success", "data": {}})

    def put(self, request):
        """
            更新资源
            ---
            parameters:
                - name: resource_id
                  description: 资源id
                  required: true
                  type: string
                  paramType: query
                - name: resource_remark
                  description: 资源备注
                  required: true
                  type: string
                  paramType: query
        """
        params = request.query_params.dict()
        update_dict = {"resource_remark": params.pop('resource_remark')}
        ResourceModel.objects.filter(**params).update(**update_dict)
        return Response({"result": "success", "data": {}})

    def delete(self, request):
        """
            删除资源
            ---
            parameters:
                - name: resource_id
                  description: 资源id
                  required: true
                  type: string
                  paramType: query
        """
        params = request.query_params.dict()
        ResourceModel.objects.filter(**params).delete()
        return Response({"result": "success", "data": {}})
