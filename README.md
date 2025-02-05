# Testing with Cypress and Typescript 

## Contents.
This project delivers a test automation examples for 2 static html pages.

It is an example of Cypress framework capabilities, it contains add-on cypress library mochawesome-reporter

it uses various Cypress utility functions like: commands, fixtures, config urls

The project is made partially in Page Object Model (POM) design pattern

## Requirements.
1) Download and install Node.js LTS on your operating system
2) Install dependencies in project main folder type in terminal: npm i

## How to run.
To run in browser type "npx cypress open" it should open Cypress window
  
      choose E2E Testing and click on it
  
      choose a browser and click "Start e2e Testing in Electron" button
  
      in new window select suite you want to run



To run in headless mode type "npx cypress run" it should start runing all tests in terminal
  
      after tests are finished you can check the web page with report summary in cypress/reports index.html (open in browser)
  
      tests failures screenshots in cypress/screenshots/{suite name}

## Technologies.
TypeScript - https://www.typescriptlang.org/

Node.js - https://nodejs.org/en

Cypress - https://www.cypress.io/

Mochawesome-reporter - https://www.npmjs.com/package/cypress-mochawesome-reporter
