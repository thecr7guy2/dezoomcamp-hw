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

##### Creating ETL pipeline

The concept of mage primarily works on blocks. Once you get mage up and running, we need to create a pipeline for the project.

To create a new Pipeline:

* Click "New Pipeline" or navigate to the Pipeline page via the left navigation panel.
* On the Pipeline Overview page, an "example_pipeline" is available for reference. Open it by clicking, and access the pipeline details by selecting "Edit Pipeline" from the left navigation.

Once you are in the pipeline interface:

* The left side displays the file structure and a list of current blocks in the pipeline.
* The center shows the blocks and their code, where you can individually edit and execute each block or run all blocks together by executing the last block with all upstream blocks.
* The right side features the Pipeline Tree, showing connections between blocks. You can add or delete these connections directly in the tree, enabling the output of one block to serve as the input for the next.


Once the pipeline is setup, Mage has predefined blocks that you can make use of to complete these pipelines. For the ETL pipeline we are building there are three blocks that we will want to use: 

* Data loader block 
* Transformer block 
* Data exporter block 

##### Loading the Data from API to pandas Dataframe 

We utilize the code from the previous week and modify a bit to complete this code block.

##### Transforming the loaded data 
After loading the data, the transformation block is utilized for any necessary modifications. For instance, with a dataset like taxi trips, this block allows for data manipulation, the creation of new columns based on conditions, and the elimination of irrelevant data.

This stage is crucial for refining your dataset. Assertions can also be integrated within this block to verify data integrity or conditions, although they're primarily recommended for deployment stages to ensure the data meets expected standards.


##### Exporting the data

Once you're confident in the quality and accuracy of your data, you have the option to export it to various destinations.

This week, we focused on two primary outlets for data exportation:
* The local postgres instance 
* Google Bigquery

To begin with the process of exporting data to PostgreSQL, one would start by adding a new block specifically designed for this purpose. **Thats one fanastic thing about mage. You get predefined templates for everything. This makes you life so much easier.** Within this block, certain variables need to be defined to tailor the export process to your specific needs. These include setting the schema_name and defining the table_name. These configurations ensure that the data export aligns precisely with the intended database schema and table.


Following the export, it's crucial to confirm that the data load was successful. This verification step can be done in two ways. You use adminer or pgsql to manually go and check if the data is really present in the first way. The more methodical way which is the second way involves you to create a predefined dataloading block which loads data from postgres database.


##### Using GCP

The configuration of the Google Cloud Platform (GCP) forms another critical component of the setup process. This begins with the setup of Google Cloud Storage, where a cloud storage bucket is created in a selected region, adhering to standard settings to facilitate smooth interaction. Subsequently, a new service account is generated, granting edit permissions and accompanied by the downloading of a JSON key. This key is essential for authentication purposes and must be placed within the Mage project directory. The io_config.yaml file is then updated to include this authentication information, either directly through key values or via the file path to the JSON key.


This block can be tailored to export data directly or implement partitioning for more extensive datasets, depending on the project's requirements. Data partitioning is particularly useful for managing large datasets, where custom Python blocks can be employed to segment the data by specific attributes, such as date, using the **pyarrow** library for efficient handling.


Lastly, the final step involves setting up a pipeline to load, transform, and write data from GCS to BigQuery. This stage is crucial for preparing the data in a format suitable for OLAP (Online Analytical Processing) usage, ensuring that the data is ready for in-depth analysis and insights generation. This comprehensive process, from data export to transformation and final loading into BigQuery, encapsulates the end-to-end workflow required to effectively manage and utilize data within a cloud-based environment.

<img src ="./images/pipeline_tree.png" width = "auto" height = "auto">


#### Scheduling and Parameterized Execution in Mage
In Mage, workflows are scheduled using triggers, which can be set based on events, schedules, or API webhooks. This flexibility allows workflows to run automatically under specific conditions, enhancing efficiency and automation.

##### Parameterization Techniques
Parameterized execution is crucial for loading datasets that depend on certain parameters, such as date. Mage supports various methods for passing parameters, including through API triggers, runtime variables during trigger setup, and global variables via the Pipeline Editor. This capability is essential for workflows that require flexibility and dynamic data handling.

##### Efficient Pipeline Backfills
Backfilling is a critical feature for addressing lost or missing data. Mage simplifies the backfill process, especially for date-parameterized pipelines, by allowing users to easily simulate and execute pipelines for past dates. This functionality ensures that no data is permanently lost and that datasets remain complete and accurate over time.

By streamlining these processes, Mage provides a comprehensive and flexible platform for scheduling, parameterizing, and executing data pipelines, catering to a wide range of data handling and analysis needs.


#### Resources and Tools
* DataTalksClub: Provided invaluable resources, including a slack channel for community support and learning resources.
* GitHub Repository: Encouraged to utilize the Zoomcamp GitHub repository for accessing course materials and contributing.

#### Challenges and Solutions
Encountered challenges in configuring environmental variables and managing dependencies between different components of the ETL pipeline. Overcame these by closely following documentation, leveraging community support, and experimenting with Mage's GUI for a more intuitive understanding of pipeline construction and execution.


#### Looking Ahead
As we proceed, the foundational skills acquired in workflow orchestration set the stage for more advanced data engineering practices, including data modeling and analytics at scale. Excited to explore further how these practices can be applied to real-world data challenges in upcoming modules.

#### Conclusion
This week's focus on workflow orchestration has been both challenging and rewarding, offering deep insights into the complexities of data engineering. Through hands-on projects and guided learning, we've laid a solid foundation.
