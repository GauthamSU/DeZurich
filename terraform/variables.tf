variable "google_project_id" {
  type = string
  description = "Google Project ID"
}

variable "provider_region_id" {
  type = string
  description = "Default region id to be mention in provider"
}

variable "project_service_account_id" {
  type = string
  description = "Unique service account id for the project"
}

variable "project_service_account_name" {
  type = string
  description = "Display name for service account"
}

variable "cloudsql_storage_admin_roles" {
  type = list(string)
  description = "Admin roles of CloudSQL and Cloud storage"
}

variable "service_account_key_path" {
  type = string
  description = "Path to store service account key in local system"
}

variable "storage_bucket_names" {
  type = list(string)
  description = "List of names of buckets to be created"
}

variable "storage_cloudsql_zone" {
  type = string
  description = "Zonal ID of the cloud storage"
}

variable "allowed_cors_origin_list" {
  type = list(string)
  description = "List of values of host to be allowed for cross origin resource sharing"
}

variable "artifact_registry_repository_id" {
  type = string
  description = "Repository ID for artifact registry"
}

variable "artifact_registry_repository_description" {
  type = string
  description = "Description for the repository"
}

variable "sql_database_instance_name" {
  type = string
  description = "SQL Database Instance name"
}

variable "sql_database_version" {
  type = string
  description = "Version of SQL Database"
}

variable "sql_database_instance_tier" {
  type = string
  description = "Database instance tier"
}

variable "sql_database_name" {
  type = string
  description = "Name of the SQL database"
}

variable "cloudsql_user_name" {
  type = string
  description = "CloudSQL user name"
}

variable "cloudsql_user_password" {
  type = string
  description = "Password for cloud SQL instance"
}

variable "kubernetes_cluster_name" {
  type = string
  description = "Kubernetes cluster name"
}