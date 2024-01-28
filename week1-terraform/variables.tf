variable "instance_name" {
  description = "The name of the instance you wanna create"
  type        = string
  default     = "gcp-instance"

}

variable "gcs_bucket_name" {
  description = "The name of the GCS bucket. Make sure the name is unique"
  default     = "dezoomcamp-bucket-sai"
}

variable "gcs_bucket_storage_class" {
  description = "The storage class of the created bucket"
  default     = "STANDARD"
}

variable "bq_dataset_name" {
  description = "The name of a Bigquery Dataset"
  default     = "bq_dataset_sai"
}

variable "location" {
  description = "The location parameter required for the gcs bucket. Regional Buckets cost the lowest So go with that"
  default     = "US-CENTRAL1"
}