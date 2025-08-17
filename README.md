# Capstone Project Part 3: Build

## Project Idea
**Thots** — Build a custom Django REST API to power your Thots, a social media feed app that lets users view posts, like, comment, and share content.

---

## Progress Report
With more clarity about my project, I have made the necessary changes as seen in my API endpoints and ERD.  
Next week I’ll start with building the API endpoints.

---

## ERD (Updated)
**UPDATED ERD**

*(Insert ERD diagram here)*

---

## API Endpoints (Updated)

### Initial Endpoints
| Endpoint         | Method | Description                     | Request Body                                                                 | Response               |
|------------------|--------|---------------------------------|----------------------------------------------------------------------------|------------------------|
| `/users/`        | GET    | Get all mock users              | None                                                                       | List of users          |
| `/posts/`        | GET    | Get all posts                   | None                                                                       | List of posts          |
| `/posts/`        | POST   | Create a new post               | `{ "user_id": 1, "content": "...", "hashtag": "#tag" }`                     | Created post           |
| `/posts/{id}/`   | GET    | Get single post                 | None                                                                       | Post object            |
| `/likes/`        | POST   | Like a post increment (like_amount) | `{ "post_id": 1, "user_id": 1 }`                                           | Updated like count     |
| `/comments/`     | POST   | Add a comment to a post         | `{ "post_id": 1, "user_id": 1, "content": "Nice post!" }`                   | Created comment        |
| `/comments/{post_id}/` | GET | Get comments for a specific post | None                                                                       | List of comments       |
| `/feed/`         | GET    | Get posts with likes & comments included | None                                                                   | Full feed data         |

---

### Updated Endpoints
| Endpoint         | Method   | Description                   | Auth Required |
|------------------|----------|-------------------------------|---------------|
| `/auth/register/`| POST     | Register new user             | ❌            |
| `/auth/login/`   | POST     | Login and get token           | ❌            |
| `/users/`        | GET      | List all users                | ✅            |
| `/users/{id}/`   | GET      | Get user profile              | ✅            |
| `/users/{id}/`   | PUT/PATCH| Update own profile            | ✅            |
| `/posts/`        | GET      | List all posts (or own posts) | ✅            |
| `/posts/`        | POST     | Create post                   | ✅            |
| `/posts/{id}/`   | GET      | Get post details              | ✅            |
| `/posts/{id}/`   | PUT/PATCH| Update post (author only)     | ✅            |
| `/posts/{id}/`   | DELETE   | Delete post (author only)     | ✅            |
| `/follow/`       | POST     | Follow another user           | ✅            |
| `/unfollow/`     | POST     | Unfollow another user         | ✅            |
| `/feed/`         | GET      | View feed of followed users   | ✅            |
