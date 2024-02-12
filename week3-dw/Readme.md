### Week 3 at DTC Data Engineering Zoomcamp: Data warehouses 


#### Overview 
This week offers an in-depth look at Google BigQuery, highlighting its role as a serverless data warehouse optimized for large-scale data analytics. It covers key concepts such as OLTP vs OLAP, data warehousing, partitioning, clustering, and best practices for cost reduction and performance improvement. Additionally, it delves into BigQuery's unique architecture, including its storage, network, and query execution engines, alongside an introduction to its machine learning capabilities for data analysts and managers.


#### Introduction


##### OLTP vs OLAP: Understanding the differences and use cases

Online Transaction Processing (OLTP) - Designed to manage transaction oriented applications. Thy are used for real time scenarios where there is a need to manage and process high volumes of data. They are more focused on operational effeciency and the transactiions involve simple queries (INSERT, UPDATE, DELETE). Main UseCases are in banking, ecommerce and CRM where the keyword "real-time" means a lot 

Online Analytical Processing (OLAP) - OLAP systems are mainly designed to process huge columes of data for the purpose of analyzing and finding insights from them. They are used mainly for strategic planning and decision making. Unlike OLTP, these systems allow for more complex queries through which the analytical insights are discovered.

##### What is a Data Warehouse 

Data Warehouse is a OLAP solution. It stores structured data from multiple sources as  optimized for fast retrieval. It is designed to support Business Intelligence, Reporting and Analytics. The main purpose of data warehouses is to aggregate data from multiple sources into a single coherent database structured source and then used for query and analysis puroses.

##### How a Data warehouse is different from Data lake

Datalake unlike a Datawarehouse can store different files. It is a repository that is designed mainly to store files in there native format. To insert data, there is no predefined schema that is required. They are mainly used in scnarios where you the data and the questions being asked in the data are eveolving. 

##### Examples 

* Data warehouses: Amazon Redshift, Google BigQuery, Snowflake etc.

* Data lakes: AWS S3, GCS, Azure Blob Storage.


#### Google Bigquery

Since in this course, we are dealing with the Google cloud eco system - we use Google Bigquery for this course.

* it is a serverless data warehouse
* It is easily scalable and highly available 
* BigQuery separates compute from storage, which maximizes flexibility and ensures that the compute engine's performance is primarily influenced by query complexity rather than the size of the data stored.


##### Cost 

* On demand pricing : 1 TB of data processed - 5$
* Flat rate pricing : Based on number of pre 
requested slots 

##### Query Caching
BigQuery enhances query performance and optimizes costs by caching the results of queries. This feature can lead to unexpected results if not properly understood, especially when recent data changes are expected to reflect immediately in query outputs. To ensure your queries always return the most current data:

Disable Caching Temporarily: Add a directive to your query to bypass the cache, ensuring you're always querying fresh data.

##### Partioning in BigQuery
Partitioning in BigQuery is a technique used to divide a table into smaller segments, called partitions, based on a specific column, such as a date or timestamp. This approach is highly effective for managing large datasets by reducing the amount of data scanned during queries, which in turn optimizes query performance and cost. Partitioning is particularly beneficial for time-series data, where queries often target specific time ranges. By partitioning a table on a date or timestamp column, BigQuery can limit the data it needs to scan to just the partitions that fall within the query's specified time range. This not only speeds up query execution but also significantly lowers costs by avoiding full table scans. Partitioning is most effective when you have a clear partitioning column that aligns with your query patterns, ensuring that your queries can take full advantage of the partitioned structure to optimize performance.

##### Clustering in BigQuery
Clustering in BigQuery complements partitioning by further organizing data within each partition into clusters based on the values of one or more columns. This allows BigQuery to efficiently filter and aggregate data by quickly homing in on the relevant clusters without scanning the entire table or partition. Clustering is especially useful when dealing with large datasets where queries frequently filter or aggregate on specific column values. It enhances query performance by reducing the amount of data processed and can lead to significant cost savings. Unlike partitioning, which is based on a single column, clustering can be applied to up to four columns, offering more flexibility in organizing data. Clustering is ideal when your queries involve multiple columns for filtering or sorting, as it provides a more granular level of data organization compared to partitioning alone.


##### When to use partioning over clustering 
Choosing between partitioning and clustering in BigQuery depends on your specific dataset and query patterns. Partitioning is the preferred approach when your data has a natural partitioning key, such as a date, and your queries frequently filter by this key. It's particularly effective for datasets with a large volume of data added daily or for time-series analyses. On the other hand, clustering should be considered when your queries commonly filter or sort by multiple columns, but do not have a clear partitioning column, or when you want to enhance the performance of queries within already partitioned tables. For the best performance and cost efficiency, combining partitioning with clustering often yields the best results, allowing you to leverage the benefits of both techniques by partitioning on a primary key (like a date) and clustering within those partitions on additional columns relevant to your queries.


##### Best practices to reduce costs 

* Avoid SELECT * 

* Price your queries (right side top corner as shown in the video.)

* Use INSERT 's with caution 

* Materialize your query results in different stages 

##### Best practices to improve query performance

* Always filter on partitoned columns (WHERE sale_date BETWEEN '2021-01-01' AND '2021-01-31';)

* Denormalize data (combine multiple tables/ add redundant data to improve the query performance)

* Avoid external sources if a very high query performance is needed 

* Reduce data before you use a join 

##### Internals of Bigquery 

* Colossus - Bigquery storage- Seperation of storage and compute. If storage increase pay for collosus 

* Jupiter network - provides high network speed and enables communication between compute and storage

* Dremel - Query execution engine - Seperates the query into multiple nodes.


##### Machine learning in Bigquery 

* Mainly for Data analysts and managers for low level ML 

* Exporting of data is removed as we use the data that is residing in Bigquery



