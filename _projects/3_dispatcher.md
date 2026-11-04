---
layout: page
title: Dispatcher
description: Team chat bot that assigns tickets round-robin to whoever is on shift, now used by my team at Amadeus
img: assets/img/projects/dispatcher/team-chat.jpg
importance: 3
category: software
---

Code: [github.com/xDMartoxD/dispatcher](https://github.com/xDMartoxD/dispatcher)

**In production at Amadeus:** my team now uses Dispatcher as its bot for internal investigations. Instead of someone triaging the queue by hand, new tickets are handed out automatically and fairly across whoever is on shift that day.

Dispatcher replaces manual ticket triage with a chat room. A poller fetches unowned ServiceNow tickets. Each new ticket goes to the active team member who has gone longest without one, and the bot sends it to them as a direct message. People clock in and out by typing in the chat: `gm`, `brb`, `back`, `gn` and `stats`, in English or Spanish.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/dispatcher/team-chat.jpg" title="Team chat" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    The team channel: people start their shift with "gm" (or "buenos días") and pause with "brb". The sidebar shows the tickets assigned to you, the waiting queue, and who is on shift.
</div>

<div class="row">
    <div class="col-sm-7 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/dispatcher/bot-dm.jpg" title="Assignment DM from the bot" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/dispatcher/stats.jpg" title="Daily stats card" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Left: the bot DMs each assignment to the assignee only, with a chime. Right: <code>stats</code> posts a card with each person's load and shift, assignments by hour and priority, and the latest events.
</div>

<div class="caption">
    Screenshots use the built-in demo tickets and fictional teammates.
</div>

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
