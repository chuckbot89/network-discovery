# Network Discovery & Topology Platform

Network devices are automatically discovered and their operational data is collected to build an actual network topology.

## Initial MVP

The initial MVP targets Cisco IOS / IOS-XE devices and focuses on:

* SSH-based device collection
* CDP neighbor discovery
* Recursive network discovery
* Device and interface inventory
* Topology generation

## Planned Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* NetworkX

### Network Automation

* Netmiko
* TextFSM
* NAPALM
* pyATS / Genie

### Frontend

* React
* TypeScript
* Cytoscape.js

### Infrastructure

* Docker
* PostgreSQL
* GitHub Actions
* GitHub Container Registry

### Integration

* NetBox

## Security Principles

* Network credentials must never be stored in source code.
* NetBox integration starts in read-only mode.
* Network access is not allowed from GitHub-hosted CI runners.
* NetBox write operations will later require dry-run and approval workflows.
