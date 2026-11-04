---
layout: page
title: Passi
description: Event ticketing app for Colombia, with QR tickets and a door scanner for organizers
img: assets/img/projects/passi/home.jpg
img_alt: "Passi mobile app home screen showing a search bar, event categories and a featured stand-up comedy event"
importance: 2
category: software
---

Code: [flutter_passi](https://github.com/xDMartoxD/flutter_passi) · [passi_scan](https://github.com/xDMartoxD/passi_scan) (original scanner app)

Passi is a Flutter app for Colombia's live-events scene (concerts, parties, comedy, food festivals). You can discover events, buy tickets and get in with a QR code. It also has an **organizer mode** for scanning tickets at the door. The UI is in Spanish and prices are in COP.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/passi/home.jpg" title="Explore" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/passi/event.jpg" title="Event detail" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/passi/checkout.jpg" title="Checkout" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Explore, event detail, and checkout with a discount code applied.
</div>

## Features

- **Explore**: featured carousel, category chips, accent-insensitive search ("medellin" finds "Medellín"), skeleton loading and pull-to-refresh.
- **Checkout**: per-tier steppers with live limits, discount and invitation codes checked as you type, saved cards (Luhn check and brand detection) or Nequi.
- **My tickets**: tickets appear as tear-off stubs with swipeable QR codes. A "USADA" stamp appears once a ticket has been scanned.
- **Organizer mode**: a camera QR scanner with a debounced, single-use check (valid / already used / wrong event / unknown), plus manual short-code entry.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/passi/ticket.jpg" title="Ticket QR" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/passi/organizer.jpg" title="Organizer mode" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/projects/passi/scan-valid.jpg" title="Valid ticket scanned" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    A ticket's QR code, the organizer's event list, and a successful scan at the door.
</div>

## History

Passi started as a college project backed by **AWS Amplify**: Cognito auth, AppSync GraphQL over DynamoDB, S3, and Node.js Lambdas that charged cards through **Wompi**. Door scanning was a separate app, [passi_scan](https://github.com/xDMartoxD/passi_scan).

Once the AWS backend was shut down, the app could no longer start. In 2026 I revived it:

- The Amplify layer was replaced with repository interfaces and an **on-device demo backend** that keeps the original Lambda business rules. Along the way I fixed two backend bugs: tier capacity checks never ran, and discount usage limits were only checked on the client.
- The app was restructured into feature folders, with `provider` + `ChangeNotifier` state, `go_router` navigation and a Material 3 dark design system.
- The scanner app was merged in as Organizer mode, and the UI was redesigned from scratch.
- It has 79 unit and widget tests plus an end-to-end purchase integration test, and CI runs format, analyze and test on every push.
