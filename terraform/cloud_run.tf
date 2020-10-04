resource "google_cloud_run_service" "default" {
  name     = "konlpy-homi-${terraform.workspace}"
  location = "asia-northeast1"

  template {
    spec {
      containers {
        image = "gcr.io/konlpy/konlpy_homi:0.0.2"
        resources {
          limits={
            cpu = "2"
            memory="1.5Gi"
          }
        }
      }
    }
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.default.location
  project     = google_cloud_run_service.default.project
  service     = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}

locals {
  domain = terraform.workspace == "prod" ? "konlpy.whatilearened.today" : "dev.konlpy.whatilearened.today"
}

resource "google_cloud_run_domain_mapping" "default" {
  location = "asia-northeast1"
  name     =  local.domain

  metadata {
    namespace = "konlpy"
  }

  spec {
    route_name = google_cloud_run_service.default.name
  }
}