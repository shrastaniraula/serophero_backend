from rest_framework.response import Response
from rest_framework.views import APIView
from news.models import News
from news.serializers import NewsSerializer
from user.models import User

class NewsView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            news = News.objects.filter(is_verified = True)
            news_data = []

            for each_news in news:
                user = User.objects.get(email = each_news.author )
                news_data.append({"news_id": each_news.id,
                                    "news_title": each_news.news_heading,
                                    "news_description": each_news.news_description,
                                    "news_image": f"media/{each_news.news_image}",
                                    "news_date": each_news.post_date,
                                    "user_name": f"{user.first_name} {user.last_name}",
                                    "user_id": user.id
                                    })
                
            serialized_news_data = NewsSerializer(news_data, many= True).data
                
            return Response(serialized_news_data)
        # return Response("token unauthorized",status = status.HTTP_401_UNAUTHORIZED)
    

class PostNewsView(APIView):

    def post(self, request):
        try:
            print("post news")
            user = request.user
            if user.is_authenticated:
                news_heading = request.data['news_heading']
                news_description = request.data['news_description']
                news_image = request.FILES['news_image']
            

                news = News.objects.create(
                    author=user,
                    news_heading=news_heading,
                    news_description=news_description,
                    news_image=news_image
                )
                

        except KeyError as e:
            return Response({"error": f"Missing required field: {str(e)}"}, status=400)

        
        return Response({"success": "Successfully posted news"})