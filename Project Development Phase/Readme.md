
![Logo](https://cloud-object-storage-18-cos-standard-yx0.s3.jp-tok.cloud-object-storage.appdomain.cloud/Logo.png)


## Project Description:

As our lives are very busy these days, we often feel we need more than 24 hrs. a day to cope up with everything we have in our schedule. Well, that's not possible but reducing the time by changing the conventional method of reading news can help. Just tell us what market news you're interested in and get a quick peek for the day. Only read what you feel is relevant and save your time. This app helps you to query for all information about Indices, Commodities, Currencies, Future Rates, Bonds, etc.… as on official websites.
## Skills Required:
IBM Cloud,HTML,Javascript,IBM Cloud Object Storage,Python-Flask,Kubernetes,Docker,IBM DB2,IBM Container Registry.
## sprint delivery Plan 
### Sprint 1 :
- Signup page
- Login page
- Aboutus page
- IBM Cloud object storage
- pushed images in Cloud object storage which are needed

### Sprint 2 :
- Home page
- API Fetching
- Page that showing API responses
- Existing bugs were removed
- pushed images in Cloud object storage which are needed

### sprint3 :
- IBM Cloud db2 table creation
- Database Connectivity
- Sendgrid integration
- pushed images in Cloud object storage which are needed
- Existing bugs were removed

### Sprint 4 :
- Docker 
- Kubernetes
- Specialized Weather module
- Existing bugs were removed
- Report creation

### final 


## Run the project file
 Run the project by starting server using this command

```bash
  python server.py
```


## Features

- Light/dark mode toggle
- Responsive Design
- UI & Animation
- Cross platform
- Specialized Weather module
- Offline Detection
- Voice Recognition Features
- Push mails & Notifications
## Installation

Python package requirements

```bash
  pip install flask
  pip install bcrypt
  pip install ibm_db
  pip install sendgrid
  pip install requests
```
    
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter |   Type   |                Description               |
| :-------- | :------- | :--------------------------------------- |
| `api_key` | `string` |               Secret API key             |
| `query `  | `string` |                Type of NEWS              |
| `from`    | `date`   |To select the news from some specific date|



## Demo

bucket video link


## Optimizations
- Performance improvements
- Accessibility
- API responses will be fetched at that time immediately, So we don't need to store that in database.


## Tech Stack

**Client:** HTML, CSS, BOOTSTRAP5, JavaScript

**Server:** Flask, Nginx

