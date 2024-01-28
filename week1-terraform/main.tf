resource "google_compute_instance" "tf_gcp_instance" {
  name         = var.instance_name
  machine_type = "e2-standard-4"
  zone         = "us-central1-b"

  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-2204-lts"
      size  = 30
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }
}

resource "google_storage_bucket" "tf_gcs_bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  storage_class = var.gcs_bucket_storage_class
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}



resource "google_bigquery_dataset" "tf_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}