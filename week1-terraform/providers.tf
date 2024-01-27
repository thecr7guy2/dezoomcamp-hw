terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  credentials = "./keys/dezoomcamp-experiment-d1a7e8818501.json"
  project     = "dezoomcamp-experiment"
  region      = "us-central1"
}