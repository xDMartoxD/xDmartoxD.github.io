---
layout: page
title: Dispatcher
description: Live team chat where a bot assigns ServiceNow tickets round-robin to whoever is on shift
importance: 3
category: software
---

Code: [github.com/xDMartoxD/dispatcher](https://github.com/xDMartoxD/dispatcher)

Dispatcher replaces manual ticket triage with a chat room. A poller fetches unowned ServiceNow tickets. Each new ticket goes to the active team member who has gone longest without one, and the bot sends it to them as a direct message. People clock in and out by typing in the chat: `gm`, `brb`, `back`, `gn` and `stats`, in English or Spanish.

- **Fair assignment**: round-robin by "longest without a ticket", with a per-person cooldown. When there are more tickets than people, the extras queue up and are handed out as people come off cooldown.
- **Live sync**: claims, the roster and the ticket queue update for everyone over Socket.IO.
- **Daily roster**: a shift roster stored in SQLite rolls over at midnight in the team's timezone.

## Stack

| Part           | Stack                                                                  |
| -------------- | ---------------------------------------------------------------------- |
| Backend        | Python 3.12, uv, python-socketio on uvicorn, pydantic-settings, SQLite |
| Frontend       | Vite, React 19, TypeScript, Tailwind 4, shadcn/ui, socket.io-client    |
| Infrastructure | AWS CDK (TypeScript): ECS Fargate, ALB, S3 + CloudFront, EFS, Route 53 |

## Deployment

CloudFront serves the frontend from a private S3 bucket and routes `/socket.io/*` to an ALB in front of a single Fargate task. Because the page and the socket share one origin, there is no CORS to configure, and the ALB only accepts traffic from CloudFront's IP ranges. The SQLite roster lives on an encrypted EFS volume, so it survives redeploys. CDK creates the ACM certificate in us-east-1 and the DNS records for the custom domain.
