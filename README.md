# Thots API

Thots API is a **social media backend** built with **Django + Django REST Framework**  
It provides endpoints for **users, posts, comments, likes, and follows**.  

The API powers a React frontend but can be used by any client (mobile, SPA, etc.).

---

## Features
- User authentication (Register, Login, Logout, Current User)
- Create, Read, Update, Delete (CRUD) for Posts
- Comment on posts
- Like and unlike posts
- Follow / unfollow users
- REST API (default) + GraphQL endpoint (optional)
- Token & Session authentication
- CORS enabled for local frontend dev

---

## Tech Stack
- **Backend:** Django, Django REST Framework, Graphene-Django
- **Auth:** TokenAuthentication & SessionAuthentication
- **Database:** PostgreSQL (via `DATABASE_URL`)
- **Frontend:** React + Apollo Client (GraphQL) or Axios/Fetch (REST)
- **Other:** Django CORS Headers

---


## Endpoints

### Auth
POST /api/register/ → Register new user

POST /api/login/ → Login (returns token)

POST /api/logout/ → Logout

### Users
GET /api/users/ → List all users
GET /api/me/ → Get current logged-in user

### Posts
GET /api/posts/ → List all posts

POST /api/posts/ → Create a post

GET /api/posts/{id}/ → Get single post

PUT /api/posts/{id}/ → Update a post

DELETE /api/posts/{id}/ → Delete a post

### Comments
GET /api/comments/ → List all comments

POST /api/comments/ → Create a comment

GET /api/comments/{id}/ → Get single comment

### Likes
GET /api/likes/ → List likes

POST /api/likes/ → Like a post

DELETE /api/likes/{id}/ → Unlike

### Follows
GET /api/follows/ → List follows

POST /api/follows/ → Follow a user

DELETE /api/follows/{id}/ → Unfollow
