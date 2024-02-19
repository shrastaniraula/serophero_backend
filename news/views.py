from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from business.serializers import UserSerializer
from news.models import News
from news.serializers import NewsSerializer
from user.models import User

class NewsView(APIView):
    def get(self, request):
        news = News.objects.filter(is_verified = True)
        news_data = []

        for each_news in news:
            serialized_news_data = NewsSerializer(each_news).data

            author = serialized_news_data['author']
            user = User.objects.get(id = author )
            serialized_user_data = UserSerializer(user).data
            
            news_user_data = {
                "user": serialized_news_data,
                "news": serialized_user_data
            }
            news_data.append(news_user_data)

        return Response(news_data)
    


    def post(self, request):
        try:
            user_id = request.data['author']
            news_heading = request.data['news_heading']
            news_description = request.data['news_description']
            news_image = request.FILES['news_image']

            author = User.objects.get(id=user_id)


        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=400)
        except KeyError as e:
            return Response({"error": f"Missing required field: {str(e)}"}, status=400)

        news = News.objects.create(
            author=author,
            news_heading=news_heading,
            news_description=news_description,
            news_image=news_image
        )
        
        return Response({"success": "Successfully posted news"})