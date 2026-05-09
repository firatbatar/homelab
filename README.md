# My Homelab Setup

A personal homelab running self-hosted services via Docker Compose. Each service lives in its own directory and is managed independently.

## Server Specs

**Technopc Mini PC Nano Fanless 2**

---

### Hardware

| Component | Details |
|-----------|---------|
| **CPU** | Intel Celeron N4505 (2C/2T, up to 2.9GHz) |
| **RAM** | 12GB DDR4 (2× DDR4 slots, max 64GB) |
| **Storage** | KIOXIA EXCERIA 960GB SSD – 2.5” SATA III |
| **External Storage** | 120GB SSD – 2.5” SATA III (via USB 3.0) |
| **GPU** | Intel UHD Graphics (Quick Sync support) |
| **Form Factor** | 190 × 165 × 49mm, Fanless, Metal chassis |
| **Power** | 65W Adapter |

---

### Connectivity

| Type | Details |
|------|---------|
| **Ethernet** | 1× GbE RJ-45 |
| **WiFi** | M.2 WiFi/BT socket (internal card) + 1× USB WiFi antenna |
| **Front USB** | 2× USB 3.0, 1× TF Card, 1× 3.5mm Audio, 1× 3.5mm Mic |
| **Rear USB** | 2× USB 2.0, 2× USB 3.0 |
| **Video** | 1× DisplayPort, 1× HDMI, 1× VGA |
| **Serial** | 2× COM |

## Services

### Networking

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/nginx-proxy-manager.svg" width="20"> [Nginx Proxy Manager](https://nginxproxymanager.com) `nginx-proxy-manager/`
Reverse proxy with automatic Let's Encrypt SSL.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/pi-hole.svg" width="20"> [Pi-hole](https://pi-hole.net) `pihole/`
Network-wide DNS ad-blocking and local DNS server.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/wireguard.svg" width="20"> [WireGuard Easy](https://github.com/wg-easy/wg-easy) `wg-easy/`
WireGuard VPN server with a web management UI.

### Monitoring

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/glance.svg" width="20"> [Glance](https://github.com/glanceapp/glance) `glance/`
Central dashboard aggregating server stats, RSS feeds, and service widgets.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/uptime-kuma.svg" width="20"> [Uptime Kuma](https://github.com/louislam/uptime-kuma) `uptime-kuma/`
Service uptime monitoring and status page.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/png/speedtest-tracker.png" width="20"> [Speedtest Tracker](https://github.com/alexjustesen/speedtest-tracker) `speedtest-tracker/`
Scheduled internet speed monitoring.

### Management

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/portainer.svg" width="20"> [Portainer CE](https://www.portainer.io) `portainer/`
Docker container management UI.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/filebrowser.svg" width="20"> [File Browser](https://filebrowser.org) `filebrowser/`
Web-based file manager for browsing and managing files on the server.

### Media

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/jellyfin.svg" width="20"> [Jellyfin](https://jellyfin.org) `jellyfin/`
Media server for movies, TV shows, and music.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/qbittorrent.svg" width="20"> [qBittorrent](https://www.qbittorrent.org) `qbittorrent/`
Torrent client.

### Media Automation

All services in this section run from a single `docker-compose.yml` in `servarr/` and share a common data path (`SERVARR_DATA_PATH`).

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/radarr.svg" width="20"> [Radarr](https://radarr.video) `servarr/`
Automated movie download management.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/sonarr.svg" width="20"> [Sonarr](https://sonarr.tv) `servarr/`
Automated TV show download management.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/bazarr.svg" width="20"> [Bazarr](https://www.bazarr.media) `servarr/`
Subtitle management for Radarr and Sonarr.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/prowlarr.svg" width="20"> [Prowlarr](https://github.com/Prowlarr/Prowlarr) `servarr/`
Indexer aggregator that syncs with Radarr and Sonarr.

#### [Byparr](https://github.com/thephaseless/byparr) `servarr/`
Cloudflare bypass proxy used by Prowlarr to access protected indexers.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/profilarr.svg" width="20"> [Profilarr](https://github.com/Dictionarry-Hub/profilarr) `servarr/`
Quality profile and custom format manager for Radarr and Sonarr.

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/overseerr.svg" width="20"> [Overseerr](https://overseerr.dev) `servarr/`
Media request and discovery UI for users to request movies and TV shows.

### Custom

#### <img src="https://raw.githubusercontent.com/firatbatar/dashboard-icons/refs/heads/main/svg/minecraft.svg" width="20"> MC Aggregator `mc-aggregator/`
Flask app written for this setup that proxies Minecraft server status from `api.mcstatus.io`.

## Structure

```
homelab/
├── .env.example            # Template for all environment variables
├── glance/
│   ├── assets/user.css     # Custom dashboard CSS
│   ├── config/
│   │   ├── glance.yml      # Entry point (auth, theme, page includes)
│   │   ├── hub.yml         # Hub page: server stats, DNS, repos
│   │   └── home.yml        # Home page: to-dos, releases, RSS, media
│   └── docker-compose.yml
├── jellyfin/
│   ├── cache/
│   ├── config/
│   └── docker-compose.yml
├── mc-aggregator/
│   ├── app.py
│   └── docker-compose.yml
├── nginx-proxy-manager/
│   ├── data/
│   ├── letsencrypt/
│   └── docker-compose.yml
├── filebrowser/
│   ├── settings.json
│   └── docker-compose.yml
├── pihole/
│   ├── etc-pihole/
│   └── docker-compose.yml
├── portainer/
│   └── docker-compose.yml
├── speedtest-tracker/
│   ├── speedtest-data/
│   └── docker-compose.yml
├── uptime-kuma/
│   ├── data/
│   └── docker-compose.yml
├── qbittorrent/
│   └── docker-compose.yml
├── servarr/
│   ├── config/
│   │   ├── radarr/
│   │   ├── sonarr/
│   │   ├── bazarr/
│   │   ├── prwolarr/
│   │   ├── profilarr/
│   │   └── overseerr/
│   └── docker-compose.yml
└── wg-easy/
    ├── config/
    └── docker-compose.yml
```

## Configuration

All environment variables are defined in a single `.env` file at the repo root (see `.env.example` for all fields). The `.env` file in each service directory is a symlink pointing to this root file — there is only one place to edit.

Key variables:

| Variable | Purpose |
|---|---|
| `LAB_IP` | LAN IP of the host machine |
| `BASE_DOMAIN` | Root domain (e.g. `example.com`) |
| `TIMEZONE` | Timezone for all services |
| `GITHUB_READONLY_TOKEN` | Used by Glance for GitHub widgets |

Each service follows a consistent naming scheme: `<SERVICE>_PORT`, `<SERVICE>_IP`, `<SERVICE>_DOMAIN`, `<SERVICE>_URL`, `<SERVICE>_DOMAIN_URL`, `<SERVICE>_ICON`.

Dashboard icons reference a [local fork](https://github.com/firatbatar/dashboard-icons) of a community icon set, reducing dependency on third-party sources.

## Usage

```bash
# Start a service
cd <service>/ && docker compose up -d

# Stop a service
cd <service>/ && docker compose down

# View logs
cd <service>/ && docker compose logs -f

# Rebuild after code changes (e.g. mc-aggregator)
cd <service>/ && docker compose up -d --build
```
