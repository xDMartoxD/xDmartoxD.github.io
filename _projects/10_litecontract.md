---
layout: page
title: LiteContract
description: "1st place, Systems and Computing Engineering projects, LA MUESTRA innovation fair 2022: contracts explained in plain language"
img: assets/img/awards/litecontract-certificate.jpg
importance: 5
category: academic
---

🏆 **1st place among Systems and Computing Engineering projects** at _LA MUESTRA_, the innovation fair of Universidad de los Andes' Innovation Week (Semana de la Innovación), November 2022.

Most people sign employment contracts they don't fully understand. LiteContract is a web app where you upload your contract as a PDF and get back its key terms in plain language:

- who the employer and the employee are,
- where and when the contract was signed, and where the work happens,
- the type of contract and the job,
- pay and payment schedule,
- working hours and who your manager is.

Each extracted term is shown with a confidence score, so you know which parts to double-check.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/awards/litecontract-certificate.jpg" title="LiteContract award certificate" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>

## The prototype

For the fair I built the front end that demonstrated the full user experience: drag-and-drop PDF upload with progress, then a timeline that reveals each term as it is "read" from the document. It was built with React 18, TypeScript and Vite, with an Ant Design dark theme, and AWS Amplify (AppSync GraphQL) for the backend wiring.

**Stack:** React, TypeScript, Vite, Ant Design, AWS Amplify.
Code: [github.com/xDMartoxD/lite-contract](https://github.com/xDMartoxD/lite-contract)
