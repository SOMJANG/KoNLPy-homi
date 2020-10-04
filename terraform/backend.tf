terraform {
  backend "remote" {
    organization = "konlpy-homi"

    workspaces {
      prefix = "konlpy_homi_"
    }
  }
}
