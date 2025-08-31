from django.core.management.base import BaseCommand
from django.utils import timezone
from posts.models import Post
from users.models import User

class Command(BaseCommand):
    help = "Create 11 mock posts"

    def handle(self, *args, **kwargs):
        # Delete previous mock posts
        Post.objects.filter(is_mock=True).delete()

        mock_posts = [
            {"first_name":"Michael","last_name":"Steve","username":"msflow","content":"ALX Capstone: I just finished the Pro Frontend Development program by ALX. It ended with a social media project. View here and #LetMeKnowYourThots"},
            {"first_name":"Adaeze","last_name":"Nwoko","username":"theada","content":"Just completed my first React project and I'm buzzing with ideas already. Shout out to the community! #FrontendVibes"},
            {"first_name":"Tomiwa","last_name":"Afolabi","username":"tomcode","content":"GraphQL feels like magic. Querying just what I need is so efficient. Can’t go back now. #DevLife"},
            {"first_name":"Ngozi","last_name":"Chukwu","username":"ngozitech","content":"Infinite scrolling finally working! Apollo Client for the win. #ReactWins"},
            {"first_name":"Jide","last_name":"Balogun","username":"codejide","content":"Sharing your thoughts is more powerful than we think. Let’s build open communities. #LetMeKnowYourThots"},
            {"first_name":"Sarah","last_name":"Edet","username":"sarah_edet","content":"Building responsive UIs is an art. Tailwind makes it fun and fast! #TailwindMagic"},
            {"first_name":"Ifeanyi","last_name":"Okeke","username":"ife_ok","content":"From zero to deploying my first GraphQL app in 3 days. ALX really prepared me well! #CapstoneComplete"},
            {"first_name":"Amina","last_name":"Yusuf","username":"aminacodes","content":"Still wrapping my head around optimistic UI updates. When it clicks, it really clicks. #GraphQLNuggets"},
            {"first_name":"Chuka","last_name":"Eze","username":"chukaeze","content":"There’s something satisfying about seeing your own post shared by others. #SharedTots"},
            {"first_name":"Lola","last_name":"Adebayo","username":"loladev","content":"Anyone else addicted to coding dark mode UIs? 👀 #DevConfessions"},
            {"first_name":"David","last_name":"Onoh","username":"onohd","content":"The capstone project pushed me harder than I expected. But look at this — it’s working! #LetMeKnowYourThots"},
        ]

        for data in mock_posts:
            user, _ = User.objects.get_or_create(
                email=f"{data['username']}@mock.com",
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "password": "mockpass123",  # default password
                    "is_mock": True
                }
            )
            Post.objects.create(
                user=user,
                content=data["content"],
                is_mock=True,
                created_at=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS("11 mock posts created successfully!"))
