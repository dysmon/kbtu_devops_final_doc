# kafka-management

This repository contains Terraform configurations for managing Kafka topics and ACLs. It includes modules for creating Kafka topics and configuring ACLs for Kafka users.

## Pre-requisites

- Terraform installed
- Kafka cluster up and running

### Usage

This section contains a step-by-step guide on how to set up Kafka topics and ACLs using Terraform on your local machine.

## Initialize terraform

To initialize Terraform, you need to comment out the backend configuration in the `backend.tf` file. This is necessary to avoid conflicts with remote state management during local development.

```bash
terraform init
```

## Plan Terraform Changes

To see the changes that will be applied, run:

```bash
terraform plan
```

## Apply Terraform Changes

To apply the changes, run:

```bash
terraform apply -auto-approve
```

By default, it uses localhost for the Kafka broker. Ensure that your Kafka broker is running on localhost:9092.

## Configuration

#### Kafka-Topic Module

The kafka-topic module is used to create Kafka topics.

```terraform
module "amplitude_topic" {
  source      = "./modules/kafka-topic"
  hostname    = var.hostname
  name        = "amplitude-kbtu"
  partitions  = 8
  retain_days = 7
}
```

#### Kafka-User Module

The kafka-user module is used to configure ACLs for Kafka users.

```terraform
module "amplitude_app" {
  source   = "./modules/kafka-user"
  hostname = var.hostname
  role     = "kbtu-user"
  groups = [
    "consumer-group-1",
    "consumer-group-2",
    "consumer-group-3",
  ]
  consumes = [
    module.amplitude_topic.name
  ]
  produces = [
    module.amplitude_topic.name
  ]
}
```

To use it in GitLab CI/CD, you need to change the variable `TF_VAR_hostname` accordingly to kafka address and setup gitlab-runner.
