
# Django Rest Apis Back-end

## Overview

These are APIs that Django App will export

### API USER

| Methods       | Urls                              | Actions                   |
| --------------| ----------------------------------| ------------------------- |
| POST          | /api/v1/accounts/create/          | create new User           |
| GET           | /api/v1/accounts/update/<int:pk>  | retrieve a User by :id    |
| PUT           | /api/v1/accounts/update/<int:pk>  | update a User by :id      |
| PUT           | /api/v1/accounts/profile/<int:pk> | update a profile by :id   |
