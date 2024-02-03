### Week 2 at DTC Data Engineering Zoomcamp: Workflow Orchestration with Mage

#### Overview 

In the second week of our Data Engineering Zoomcamp, we dove into the essentials of workflow orchestration, utilizing Mage as our primary tool.

#### Practical Applications

* Configuring Mage and PostgreSQL: Set up our environment for workflow orchestration, including configuring Mage and establishing a PostgreSQL database connection.
* Building an ETL Pipeline with Mage: Utilized Mage to construct an ETL pipeline that processes and exports New York Taxi data, showcasing the power of Mage blocks (Data Loader, Transformer, Data Exporter) in streamlining data processing tasks.

#### Steps taken in detail to complete Week-2 
The week commenced with the configuration of Mage, guided by the comprehensive setup instructions provided by [@mattpalmer](https://www.linkedin.com/in/matt-palmer/). While the initial configuration facilitated a seamless startup, certain adjustments were deemed necessary to better align with specific requirements.

##### Changing the metadata database
We streamlined our database setup by transitioning Mage's metadata storage from MySQL to PostgreSQL, the primary database used in the course. This change aimed to simplify the environment by using a single database system.

To integrate Mage's metadata into PostgreSQL, we utilized `docker-entrypoint-initdb.d` directory to automate the creation of a new database for Mage upon the container's startup. This process ensured that the necessary database for storing Mage's metadata was ready immediately after the container was launched.

The final step in the integration was updating the .env file with the PostgreSQL connection URL for Mage, following the format:

```
MAGE_DATABASE_CONNECTION_URL=postgresql+psycopg2://mage:mage@database:5432/mage
```

##### Spinning up Mage 

To initiate Mage, we begin by launching the database and Adminer containers, which are categorized under the db profile within the Docker Compose configuration:

```
docker compose --profile db up 
```

This command activates all components reliant on PostgreSQL, effectively setting up the necessary database environment.

Subsequently, to start Mage, a specific consideration must be addressed: the absence of a .env file in the root directory can lead to Docker Compose environment variables being interpreted as blank strings. To circumvent this issue, it is crucial to explicitly specify the correct location of the .env file as follows:

this command sets everything up that uses postgres 

Next we similarly need to start Mage,but a small problem taht you would encounter will be that if there is no .env file in the root directory the variables assigned in docker compose turn out to be blank strings to prevent this we need to substitute the correct location of the .env file 

```
docker compose --profile mage --env-file ./docker-envs/mage.env up 
```

With this approach, Mage successfully establishes a metadata database within PostgreSQL. The successful creation and integration of this database can be confirmed through Adminer, accessible at port `8080`.

Furthermore, the operational status of Mage can be verified by navigating to [localhost:6789](http://localhost:6789), where the Mage interface should be accessible.


#### Resources and Tools
* DataTalksClub: Provided invaluable resources, including a slack channel for community support and learning resources.
* GitHub Repository: Encouraged to utilize the Zoomcamp GitHub repository for accessing course materials and contributing.

#### Challenges and Solutions
Encountered challenges in configuring environmental variables and managing dependencies between different components of the ETL pipeline. Overcame these by closely following documentation, leveraging community support, and experimenting with Mage's GUI for a more intuitive understanding of pipeline construction and execution.


#### Looking Ahead
As we proceed, the foundational skills acquired in workflow orchestration set the stage for more advanced data engineering practices, including data modeling and analytics at scale. Excited to explore further how these practices can be applied to real-world data challenges in upcoming modules.

#### Conclusion
This week's focus on workflow orchestration has been both challenging and rewarding, offering deep insights into the complexities of data engineering. Through hands-on projects and guided learning, we've laid a solid foundation.
