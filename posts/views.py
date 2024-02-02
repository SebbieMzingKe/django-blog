from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404




@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    if request.method == "POST":
        data = request.data 
        response = {"message" : "Hello World!", "data":data}
        return Response(data = response, status = status.HTTP_201_CREATED)
    response = {"message" : "Hello World!"}
    return Response(data = response, status=status.HTTP_200_OK)
class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     a view for creating and listing posts
    """
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
    
            
    
class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return sel.update(request, *args, **Kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

        

# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404



# @api_view(http_method_names=["GET", "POST"])
# def homepage(request: Request):
#     if request.method == "POST":
#         data = request.data 
#         response = {"message" : "Hello World!", "data":data}
#         return Response(data = response, status = status.HTTP_201_CREATED)
#     response = {"message" : "Hello World!"}
#     return Response(data = response, status=status.HTTP_200_OK)

# @api_view(http_method_names=["GET", "POST"])
# def list_post(request: Request):
#     posts = Post.objects.all()
    
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data = data)
        
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message":"Post Created", "data":serializer.data
#             }
            
#             return Response(data = response, status=status.HTTP_201_CREATED)
#         return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
#     serializer = PostSerializer(instance = posts, many = True)
#     response = {
#         "message":"posts",
#         "data":serializer.data
#     }
#     return Response(data = response, status=status.HTTP_200_OK)

# #returning individual posts
# @api_view(http_method_names=["GET"])
# def post_detail(request: Request, post_id: int):
#     post =get_object_or_404(Post, pk = post_id)
#     serializer = PostSerializer(instance = post)
    
#     response = {
#         "message":"post",
#         "data":serializer.data
#     }
    
    
#     return Response(data = response, status=status.HTTP_404_NOT_FOUND)    

# # getting a post by id
# @api_view(http_method_names=["GET"])
# def get_post_by_id(request:Request, post_id:int):
#     pass


# #updating a post
# @api_view(http_method_names=["PUT"])
# def update_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk = post_id)
    
#     data = request.data

#     serializer = PostSerializer(instance=post, data = data)
#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message":"post updated successfully",
#             "data":serializer.data
#         }

#         return Response(data = response, status = status.HTTP_200_OK)
#     return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # deleting a post
# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request, post_id:int):
#     post = get_object_or_404(Post, pk = post_id)
#     post.delete()
#     return Response(status = status.HTTP_204_NO_CONTENT)
