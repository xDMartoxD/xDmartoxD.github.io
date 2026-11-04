---
layout: page
title: PlaylistMaster
description: Clean up, merge and build playlists across YouTube, Spotify, Apple Music and more
img: assets/img/projects/playlistmaster/home.jpg
importance: 1
category: software
---

[**playlistsmaster.com**](https://playlistsmaster.com) · code: [backend](https://github.com/xDMartoxD/youtube-auto-delete) · [client](https://github.com/xDMartoxD/youtube-auto-delete-client) · [infrastructure](https://github.com/xDMartoxD/youtube-auto-delete-cdk)

PlaylistMaster is a web app for people whose playlists have grown out of control. You sign in with Google, pick a streaming service and use one of three tools:

- **Clean up**: find duplicates and bulk-remove tracks.
- **Merge**: combine several playlists into a new or existing one.
- **Create**: build a playlist from others using union, intersection or difference.

YouTube and YouTube Music use the real YouTube Data API, and Spotify works once a user links their account. Apple Music and Amazon Music run as demo providers behind the same interface until their integrations are built.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/playlistmaster/duplicates.jpg" title="Duplicate tracks selected for removal" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Clean up: duplicates are detected and selected for removal in one click.
</div>
<div class="row">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/playlistmaster/merged.jpg" title="Merging playlists" class="img-fluid rounded z-depth-1" zoomable=true %}
        {% include figure.liquid path="assets/img/projects/playlistmaster/created.jpg" title="Creating a playlist from other playlists" class="img-fluid rounded z-depth-1 mt-3" zoomable=true %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/playlistmaster/mobile.jpg" title="Mobile layout" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Merge and Create tools on desktop, and the responsive layout on mobile.
</div>

## How it's built

**Backend:** FastAPI (Python 3.13) with Clean Architecture / DDD layering: routers, application services, a domain layer (user aggregate, value objects, playlist composition services) and infrastructure adapters. Each streaming service implements one `PlaylistProvider` port, so adding a real integration means writing one adapter. Data lives in a single DynamoDB table with GSIs, and Redis/Valkey provides cache-aside caching. Auth exchanges a Google OAuth code for tokens and issues an HTTP-only JWT session cookie. Spotify linking uses a signed OAuth `state`. The API also has per-IP rate limiting.

**Client:** React 19, Vite and TypeScript, with Zustand stores, Tailwind v4 and shadcn/ui. The API client is generated from the backend's OpenAPI spec, so the frontend and backend contracts can't silently drift apart.

**Infrastructure:** AWS CDK in TypeScript, in two stacks. The API runs on ECS Fargate behind an ALB at `api.playlistsmaster.com`. The frontend is served from S3 through CloudFront. Secrets come from AWS Secrets Manager.
