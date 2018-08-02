# Slack Technical Challenge

## Application Details

* **Github Repo Url:**[https://github.com/sylvestor88/stc.git](https://github.com/sylvestor88/stc.git)
* **Hosted at:** [http://35.235.69.140:8888](http://35.235.69.140:8888)
* **API Specs:** [http://35.235.69.140:8888/apidocs](http://35.235.69.140:8888/apidocs)

#### Steps to Run the Application locally

This Application is written in Python3.

You can either create a Python virtualenv or run on any environment that has Python3 and pip installed.

You may get the source code from Github Repository or use the .zip.
Execute below commands:
  
1) ```git pull https://github.com/sylvestor88/stc.git``` or ```unzip stc.zip -d stc```
2) ```cd stc```
3) ```pip install -r requirements```
4) ```python app.py```


You should see the API docs in [http://localhost:8888/apidocs/](http://localhost:8888/apidocs/)

## Discussion

> Tell us how you anticipate your application would be installed in a production environment, and any changes needed to make it production-ready

```
The application can be served on production environment using gunicorn web-server. It can handle multiple requests, instead of sequentially serving each request.

I have installed my Application in Google Cloud Platform using gunicorn web-server.
  
Following changes can be made for the application to be production ready:  
 
 * Making Application more configurable, to run on different environments such as stage, production, etc. As of the the DB connection details and port info are hard-coded.
 * We would also need to add validations on all the query parameters being used in the APIs, which would make our application more reliable.
 * Writing unit and integration tests for the Application.
 * Logging to be implemented to debug on errors/failures and dumping all the logs at central location for monitoring purposes.
 * We can also add some monitoring client in our application (like datadog) to send metrics.
```

> Suggest ways in which the performance, reliability, maintainability or other limitations of your implementation could be improved upon in the future

```
This Application was written in a very short period of time and therefore can be improved to a great extend to make it scalable and reliable.
  
Performance
    * The DB queries can be optimized to reduce retrieval/insertion time. 
    * Caching mechanism for DBs such as MySQL, Postgres, etc. can be implemented for faster retreival of the data (however, this would lead to compromise in consistency unless cache is frequently updated).
    * We can also add API pagination to limit the number of records retrieved in a single call, to handle large data set.
  
Reliability
    * Testing Infrastructure needs to be put in place to ensure the reliability of the Application.
    * Error Handling can be improved for the APIs. Ex: If the DB is down for some reason, application should be able to re-try connection or emitting readable exceptions in case of bad requests.
    * Handling invalid requests by the users.
    
Scalability
    * Multiple instances on different servers can be started and put behing HA Proxy for load-balancing.
    * Could be deployed using Kubernetes or Mesos to automatically scale.
  
Maintainability
    * Documentation needs to be improved for the code to be readable by other Developers.
    * API Documentation can be done using Swagger (Used flasgger to achieve that).
    * Adding better in-code comments would also help in maintaining the code.
```

## Authors:

* Sylvestor George (sylvestor.george88@gmail.com)