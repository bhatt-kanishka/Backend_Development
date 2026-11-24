# Unit 4: Docker Compose — Multi-Service Database Stack

## Purpose
A **Docker Compose** configuration that spins up a complete backend database environment with **PostgreSQL**, **MongoDB**, and their respective web admin interfaces (**pgAdmin** and **Mongo Express**) — all in one command.

---

## What This Code Does
This `docker-compose.yml` file defines four containerized services that run together:

1. **PostgreSQL** (`postgres_db`) — Relational database server
2. **pgAdmin** (`pgadmin`) — Web-based GUI for managing PostgreSQL (accessible at `http://localhost:8094`)
3. **MongoDB** (`mongo_db`) — NoSQL document database server
4. **Mongo Express** (`mongo_express`) — Web-based GUI for managing MongoDB (accessible at `http://localhost:8081`)

All services communicate over a private Docker network (`backend`), and database data is persisted in Docker volumes so it survives container restarts.

---

## Concepts Covered

| Concept | Where It Appears |
|:--------|:-----------------|
| **Docker Compose** | Multi-service orchestration in a single YAML file |
| **Container Networking** | `networks: backend` — services discover each other by container name |
| **Persistent Volumes** | `postgres_data`, `pgadmin_data`, `mongo_data` — data survives `docker compose down` |
| **Environment Variables** | Configurable credentials with `${VAR:-default}` syntax |
| **Service Dependencies** | `depends_on` ensures databases start before their admin UIs |
| **Port Mapping** | `127.0.0.1:8094:80` — binds to localhost only (security best practice) |
| **Restart Policies** | `restart: unless-stopped` — auto-restart on failure |
| **Database Security** | Databases are NOT exposed on the host — only accessible within the Docker network |

---

## Prerequisites and Dependencies

- **Docker Desktop** (Windows/Mac) or **Docker Engine** (Linux)
- **Docker Compose** v2+ (bundled with Docker Desktop)
- Ports `8094` and `8081` available on your machine

---

## Installation and Run Steps

```bash
# Navigate to the docker-compose directory
cd "Theory/unit-4/docker/docker-compose"

# Start all services in detached mode
docker compose up -d

# Check that all containers are running
docker compose ps

# View logs (follow mode)
docker compose logs -f
```

### Access the Admin Interfaces

| Service | URL | Default Login |
|:--------|:----|:--------------|
| **pgAdmin** | `http://localhost:8094` | Email: `admin@example.com`, Password: `StrongPass123` |
| **Mongo Express** | `http://localhost:8081` | Username: `admin`, Password: `StrongPass123` |

### Connecting to PostgreSQL from pgAdmin
1. Open pgAdmin at `http://localhost:8094`
2. Add New Server → Connection tab:
   - Host: `postgres_db` (the Docker container name)
   - Port: `5432`
   - Username: `admin`
   - Password: `StrongPass123`
   - Database: `main_db`

---

## File Structure

```text
Theory/unit-4/
└── docker/
    └── docker-compose/
        └── docker-compose.yml    # Multi-service Docker Compose configuration
```

---

## Code Walkthrough

### Services Architecture

```text
┌──────────────────────────────────────────────┐
│             Docker Network: backend          │
│                                              │
│  ┌─────────────┐       ┌─────────────┐      │
│  │ postgres_db  │       │  mongo_db   │      │
│  │ PostgreSQL   │       │  MongoDB    │      │
│  │ :5432        │       │  :27017     │      │
│  └──────┬──────┘       └──────┬──────┘      │
│         │                      │              │
│  ┌──────┴──────┐       ┌──────┴──────┐      │
│  │   pgadmin   │       │mongo_express│      │
│  │ :80 → :8094 │       │:8081 → :8081│      │
│  └─────────────┘       └─────────────┘      │
└──────────────────────────────────────────────┘
         ↕                        ↕
    localhost:8094           localhost:8081
```

### Key Configuration Details

**Security:** Both database containers do NOT publish their ports to the host. Only the admin web interfaces are exposed, and they're bound to `127.0.0.1` (localhost only) — not accessible from other machines on the network.

**Volumes:** Named volumes (`postgres_data`, `pgadmin_data`, `mongo_data`) persist data:
- `docker compose down` — stops containers, keeps data
- `docker compose down -v` — stops containers AND **permanently deletes all data**

**Environment Variables:** All credentials use the `${VAR:-default}` pattern, so you can override them with a `.env` file:
```env
POSTGRES_USER=myuser
POSTGRES_PASSWORD=MySecurePassword
MONGO_ROOT_USERNAME=myuser
MONGO_ROOT_PASSWORD=MySecurePassword
```

---

## Useful Commands

```bash
# Start all services
docker compose up -d

# Stop all services (keeps data)
docker compose down

# Stop and DELETE all data (destructive!)
docker compose down -v

# View specific service logs
docker compose logs -f pgadmin
docker compose logs -f mongo_express

# Restart a specific service
docker compose restart postgres_db

# Execute a command inside a container
docker compose exec postgres_db psql -U admin -d main_db
docker compose exec mongo_db mongosh -u admin -p StrongPass123
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|:------|:------|:----|
| `port is already allocated` | Port 8094 or 8081 in use | Stop the conflicting service or change the port in `docker-compose.yml` |
| pgAdmin can't connect to PostgreSQL | Wrong hostname | Use `postgres_db` (container name), not `localhost` |
| Mongo Express shows "connection refused" | MongoDB not ready yet | Wait a few seconds and refresh; `depends_on` doesn't wait for readiness |
| Data disappeared after restart | Used `docker compose down -v` | The `-v` flag deletes volumes; omit it to keep data |
| `docker compose` command not found | Old Docker version | Update Docker Desktop or install Docker Compose v2 |

---

## Key Takeaways

1. **Docker Compose** lets you define and run multi-container applications with a single YAML file
2. **Container networking** allows services to discover each other by name (e.g., `postgres_db:5432`)
3. **Named volumes** provide data persistence — your database data survives container restarts
4. **Binding to 127.0.0.1** instead of `0.0.0.0` is a security best practice for development tools
5. This stack gives you a complete local database environment for backend development without installing PostgreSQL or MongoDB on your machine directly
