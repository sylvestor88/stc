# Slack Technical Challenge

## Application Details

* **Github Url:**  
* **Hosted At:** 
* **API Specs:** 


#### Steps to Run the Application locally

This Application is written in Python3

You can setup a Python virtual environment and run the below commands:

1) ```git pull ```
2)  ```cd ```
3)  ```pip install -r requirements```
4)  ```python app.py```

## Discussion

> Tell us how you anticipate your application would be installed in a production environment, and any changes needed to make it production-ready

```
The application can be served on production environment using gunicorn web-server. It can handle multiple requests, instead of sequentially serving each request.

I have installed my Application in Google Cloud Platform using gunicorn web-server.

Following changes can be made for the application to be production ready:  
 
 * Making Application more configurable, to run on different environments such as stage, production, etc. As of the the DB connection details and port info are hard-coded.
 * Writing unit and intgration tests for the Application
 * Logging to be implemented to debug on errors/failures
```

> Suggest ways in which the performance, reliability, maintainability or other limitations of your implementation could be improved upon in the future

```
This Application was written in a very short period of time and therefore can be improved to a great extend to make it scalable and reliable.
  
Performance
    * The DB queries can be optimized to reduce retrieval/insertion time. 
    * Caching mechanism for DBs such as MySQL, Postgres, etc. can be implemented for faster retreival of the data.
  
Reliability
    * Testing Infrastructure needs to be put in place to ensure the reliability of the Application.
    * Error Handling can be improved for the APIs. Ex: If the DB is down for some reason, application should be able to re-try connection.
    * Refactoring to handle invalid requests by the users
    
Scalability
    * Multiple instances on different servers can be started and put behing HA Proxy for load-balancing.
    * Could be deployed using Kubernetes or Mesos to automatically scale.
  
Maintainability
    * Documentation needs to be improved for the code to be readable by other Developers.
    * API Documentation can be done using Swagger (Used flasgger to achieve that)
    
```

## Authors:

* Sylvestor George (sylvestor.george88@gmail.com)