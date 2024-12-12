# Lab 2: - Implement intial data or seed

## Task Overview
seed your application with some initial data using fixtures

### initial_data.json
#### path: app/home/fixtures/initial_data.json
The `initial_data.json` add initial data for the following structure:

 - Seed your application with a user called system(username)
 - Seed your application with Company called “HelloWorld Company”, “Second Company”
 - Seed your application with UserProfile called “HelloWorld Profile”, “Second Profile”

[
    {
        "model": "auth.user",
        "pk": 1,
        "fields": {
            "username": "system",
            "password":"pbkdf2_sha256$260000$RyeorYTpeeIWLXT7Sg4eQr$55M9bl3MJbhdEyjxezBCNqqr/oiB21MywY7dwMve1r8=",
            "email": "system@yourcompany.com",
            "first_name": "System",
            "last_name": "User",
            "is_active": true,
            "is_staff": true,
            "is_superuser": true
        }
    },
    {
        "model": "home.company",
        "pk": 1,
        "fields": {
            "name": "HelloWorld Company",
            "location": "Global",
            "created_at": "2002-02-01"
        }
    },
    {   
        "model": "home.company",
        "pk": 2,
        "fields": {
            "name": "Second Company",
            "location": "Global",
            "created_at": "2002-02-01"
        }
    },
    {
        "model": "home.userprofile",
        "pk": 1,
        "fields": {
            "profile": "HelloWorld Profile",
            "language": "en",
            "is_active": "1",
            "company_id": "1",
            "user_id": "1"
        }
    },
    {
        "model": "home.userprofile",
        "pk": 2,
        "fields": {
            "profile": "Second Profile",
            "language": "en",
            "is_active": "0",
            "company_id": "2",
            "user_id": "1"
        }
    }
]

### Command for running the initial.json
    py manage.py loaddata initial_data.json

### Credential for initial user
    username:system
    password:!@#123QWEqwe