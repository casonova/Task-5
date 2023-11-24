
# Timezone Update Project


The Project creates dummy data of 100 customers and update their time from utc to pst after every 5 minutes thorough cron job. 

## Key Features

- **Create Records of Customer** Create dummy data of 100 customers by runing custom management command.
- **Update Records** Fetch records of 10 customer and update their timeformat from utc to pst after every 5 minutes through implementation of cronjob.






## Installation
To install and run the project locally, follow the steps:

1. Clone the repository:


```bash
git clone https://github.com/casonova/Task-5.git
```
2. Make Virtual environment:

```bash
python3 -m venv env
```  

3. Install dependencies:

```bash
pip install -r requirements.txt
```    
4. Apply database migrations:
```bash
python manage.py makemigrations
```  

```bash
python manage.py migrate
```    
5.  Add cronjob:
```bash
python manage.py crontab add
```  
 
## Usage
1. Create a superuser:

```javascript
python manage.py createsuperuser
```

2. Access the admin panel at `http://127.0.0.1:8000/admin/` to see the timeformat of dummy customers that were created.





## Credits

- [Django Framework](https://www.djangoproject.com/)





## Log
There is a log folder in which a log file is present. This log file contain the actions of projects and log time in which customer records get updated.