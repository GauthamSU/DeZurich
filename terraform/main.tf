resource "google_service_account" "service_account" {
  account_id   = var.project_service_account_id
  display_name = var.project_service_account_name
}

resource "google_project_iam_member" "cloudsql_storage_admin_binding" {
  project = var.google_project_id
  for_each = toset(var.cloudsql_storage_admin_roles)
  role = each.value
  member  = "serviceAccount:${google_service_account.service_account.email}"
}

resource "google_service_account_key" "mykey" {
  service_account_id = google_service_account.service_account.name
}

resource "local_file" "myaccountjson" {
content     = base64decode(google_service_account_key.mykey.private_key)
filename = "${var.service_account_key_path}"
}

resource "google_storage_bucket" "static_media_storage_bucket" {
  for_each = toset(var.storage_bucket_names)
  name          = each.value
  location      = var.provider_region_id
  force_destroy = true

  uniform_bucket_level_access = true

#   website {
#     main_page_suffix = "index.html"
#     not_found_page   = "404.html"
#   }
  cors {
    origin          = var.allowed_cors_origin_list
    method          = ["GET", "HEAD", "PUT", "POST", "DELETE"]
    response_header = ["*"]
    max_age_seconds = 3600
  }
}

resource "google_artifact_registry_repository" "my-repo" {
  location      = var.provider_region_id
  repository_id = var.artifact_registry_repository_id
  description   = var.artifact_registry_repository_description
  format        = "DOCKER"
}

resource "google_sql_database_instance" "cloudsql_instance" {
  name             = var.sql_database_instance_name
  database_version = var.sql_database_version
  region           = var.provider_region_id
  deletion_protection = false

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = var.sql_database_instance_tier
    edition = "ENTERPRISE"
    availability_type = "ZONAL"
    disk_size = 10
  }
}

resource "google_sql_database" "cloud_sql_database" {
  name     = var.sql_database_name
  instance = google_sql_database_instance.cloudsql_instance.name
}

resource "google_sql_user" "cloud_sql_user" {
  name     = var.cloudsql_user_name
  instance = google_sql_database_instance.cloudsql_instance.name
  password = var.cloudsql_user_password
}

resource "google_container_cluster" "primary" {
  name               = var.kubernetes_cluster_name
  location           = var.storage_cloudsql_zone
  initial_node_count = 2
  deletion_protection = false
  
  node_config {
    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    # service_account = google_service_account.default.email
    disk_size_gb = 20
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
}
}