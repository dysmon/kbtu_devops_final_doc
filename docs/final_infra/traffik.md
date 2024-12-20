# Traefik Nomad Job

## Overview
This document provides a Nomad job definition for deploying Traefik in the "kbtu" datacenter as a system job.

## Job Details

- **Configuration Templates**:
    - Main Traefik configuration (`traefik.yml`)
    - Dynamic routing configuration (`traefik-dynamic.yml`)

## Makefile
- **Target**: `run`
    - Deploys the Traefik job using a shell script

## Shell Script
- Stops any existing Traefik job
- Validates the job file
- Runs the new Traefik job
- Checks the job status
