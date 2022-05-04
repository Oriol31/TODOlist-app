from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer


class TaskListView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class TaskDetailView(APIView):

    def get(self, request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(tasks)
        return Response(serializer.data)

    def patch(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskDetailSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()

